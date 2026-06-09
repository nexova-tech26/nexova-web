from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlmodel import Session, select
from app.database import create_db_and_tables, engine
from app import models  # Importamos los modelos para que SQLModel los reconozca
import shutil
import os
import uuid
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pydantic import BaseModel
from app.models import ContactoForm


# Este ciclo de vida asegura que la base de datos se configure antes de recibir tráfico
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# Inicializamos la API 
app = FastAPI(title="API CMS - Mi Startup", lifespan=lifespan)

#Configura las políticas de red (CORS)
# En desarrollo permitimos "*" (todo). En producción pondremos tu dominio real.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#MONTAR CARPETA ESTÁTICA (Para que el navegador pueda ver las imágenes)
# Si no existe la carpeta, la creo de inmediati
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

#Endpoint para subir imagenes
@app.post("/upload-imagen/")
async def upload_imagen(file: UploadFile = File(...)):
    try:
        # Generamos un nombre único para evitar que fotos con el mismo nombre se sobreescriban
        extension = file.filename.split(".")[-1]
        nombre_unico = f"{uuid.uuid4()}.{extension}"
        ruta_archivo = f"static/{nombre_unico}"

        # Guardamos el archivo físico en el servidor
        with open(ruta_archivo, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Devolvemos la URL pública que Vue guardará en la base de datos
        #  backend corriendo en localhost:8000
        url_publica = f"http://127.0.0.1:8000/static/{nombre_unico}"
        return {"url": url_publica}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Nuestra primera ruta de prueba
@app.get("/")
def read_root():
    return {"titulo": "Sistema de Control de Acceso",
  "descripcion": "Gestión de cafetería y acceso con reconocimiento facial.",
  "imagen_url": "./uploads/card_casino_final.svg",
  "demo_url": "https://midemo.com",
  "repositorio_url": "https://github.com/tuusuario/repo",
  "tecnologias": "FastAPI, Vue.js, OpenCV"}

#endopoint para agregar proyectos

#@app.post porque va a recibir datos
#con response_model le decimos a fastapi como formatear la respuesta final
@app.post("/proyectos/", response_model = models.Proyecto)

def crear_proyecto(proyecto: models.Proyecto):
    #abrir una conexion temporal (una sesion) con la bd
    with Session(engine) as session:
        #se transforma el objeto de fasapi en un objeto de base de datos
        db_proyecto = models.Proyecto.model_validate(proyecto)
        #añadimos el objeto correcto a la sesión
        session.add(db_proyecto)
        session.commit()
        session.refresh(db_proyecto)
        
        # Devolvemos el objeto que ya tiene su id generado
        return db_proyecto
    
    #ENDPOINT PARA LEER PROYECTOS ---

# Usamos list[models.Proyecto] porque ahora devolveremos un arreglo (lista) de proyectos, no solo uno.
@app.get("/proyectos/", response_model=list[models.Proyecto])
def obtener_proyectos():
    with Session(engine) as session:
        # select() prepara la consulta: "SELECT * FROM Proyecto"
        statement = select(models.Proyecto)
        
        # session.exec() envía la consulta a SQLite, y .all() trae todos los resultados
        resultados = session.exec(statement).all()
        
        return resultados
    
# --- NUEVO ENDPOINT PARA ACTUALIZAR (PUT) ---

# Usamos PUT para reemplazar información. Notarás el {proyecto_id} en la URL.
@app.put("/proyectos/{proyecto_id}", response_model=models.Proyecto)
def actualizar_proyecto(proyecto_id: int, proyecto_actualizado: models.Proyecto):
    with Session(engine) as session:
        # 1. Buscamos si el proyecto existe en la base de datos
        db_proyecto = session.get(models.Proyecto, proyecto_id)
        
        # 2. Si no existe, lanzamos un error 404 formal
        if not db_proyecto:
            raise HTTPException(status_code=404, detail="Proyecto no encontrado")
        
        # 3. Extraemos los datos del JSON que nos enviaron
        datos_nuevos = proyecto_actualizado.model_dump(exclude_unset=True)
        
        # 4. Actualizamos dinámicamente los campos en el objeto de la base de datos
        for key, value in datos_nuevos.items():
            setattr(db_proyecto, key, value)
        
        # 5. Confirmamos los cambios
        session.add(db_proyecto)
        session.commit()
        session.refresh(db_proyecto)
        return db_proyecto

# --- NUEVO ENDPOINT PARA ELIMINAR (DELETE) ---

# Usamos DELETE. Aquí no recibimos JSON, solo el ID por la URL.
@app.delete("/proyectos/{proyecto_id}")
def eliminar_proyecto(proyecto_id: int):
    with Session(engine) as session:
        db_proyecto = session.get(models.Proyecto, proyecto_id)
        
        if not db_proyecto:
            raise HTTPException(status_code=404, detail="Proyecto no encontrado")
        
        # Le decimos a la sesión que elimine el registro
        session.delete(db_proyecto)
        session.commit()
        
        return {"estado": "Éxito", "mensaje": f"Proyecto {proyecto_id} eliminado correctamente"}    
    
@app.post("/contacto/")
async def procesar_contacto(contacto: ContactoForm):
    # === CONFIGURACIÓN DE TU CORREO (Ejemplo usando Gmail) ===
    # El correo desde donde el sistema enviará el mensaje
    REMITENTE = "contacto.nexovatech@gmail.com" 
    # ¡OJO! No es tu contraseña normal. Es una "Contraseña de Aplicación" generada en Google.
    PASSWORD = "bmki mjtv nknf revv" 
    # El correo al que quieres que lleguen los mensajes de los clientes
    DESTINATARIO = "contacto.nexovatech@gmail.com" 

    # Construimos la estructura del correo electrónico
    msg = MIMEMultipart()
    msg['From'] = REMITENTE
    msg['To'] = DESTINATARIO
    msg['Subject'] = f"🚀 Nuevo prospecto Nexova Tech: {contacto.nombre}"

    # El cuerpo del mensaje con los datos del formulario
    cuerpo = f"""
    ¡Hola Equipo Nexova! Han recibido un nuevo requerimiento web:

    - Nombre o Empresa: {contacto.nombre}
    - Correo del Cliente: {contacto.email}
    - Área de Interés: {contacto.servicio}

    Mensaje del cliente:
    {contacto.mensaje}
    """
    msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

    try:
        # Usamos SMTP_SSL para una conexión directa y más segura por el puerto 465
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(REMITENTE, PASSWORD)
        server.sendmail(REMITENTE, DESTINATARIO, msg.as_string())
        server.quit()
        
        return {"mensaje": "Correo enviado y procesado exitosamente"}
        
    except Exception as e:
        print(f"Error enviando correo: {e}")
        # Le decimos al Front que algo falló para que no muestre la alerta de éxito
        raise HTTPException(status_code=500, detail="Error interno al enviar el correo")