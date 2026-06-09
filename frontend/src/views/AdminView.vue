<script setup>
import { ref, onMounted } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Message from 'primevue/message';

// ESTADO GLOBAL DE LA VISTA
// Almacena la lista reactiva de proyectos obtenidos desde FastAPI para renderizar la tabla principal.
const proyectos = ref([]);
// Controla los indicadores visuales de carga para evitar que el usuario interactúe mientras hay peticiones en curso.
const cargando = ref(false);
// Controla la visibilidad del componente Dialog (Modal) que contiene el formulario.
const mostrarModal = ref(false);
// Bandera lógica que determina si el formulario ejecutará un método POST (creación) o PUT (actualización).
const modoEdicion = ref(false);
const error = ref('');

// ESTADO DEL FORMULARIO
// Estructura base requerida por el esquema de Pydantic en el backend.
const proyectoInicial = {
    titulo: '',
    descripcion: '',
    tecnologias: '',
    imagen_url: '',
    demo_url: '',
    repositorio_url: ''
};

// Variable reactiva unida mediante v-model a los inputs del formulario.
const proyectoActual = ref({ ...proyectoInicial });

// ESTADO DE ARCHIVOS (UPLOAD)
// Referencia directa al elemento DOM <input type="file"> oculto.
const archivoImagen = ref(null);
// Almacena el objeto File (binario) en la memoria del navegador antes de ser enviado al servidor.
const archivoSeleccionado = ref(null);

// OPERACIONES DE RED (API FETCH)

// Sincroniza la tabla del panel de administración con los registros actuales de la base de datos.
const cargarProyectos = async () => {
    cargando.value = true;
    error.value = '';
    try {
        const res = await fetch('/api/proyectos/');
        if (!res.ok) throw new Error('Fallo en la comunicación con el servidor FastAPI.');
        proyectos.value = await res.json();
    } catch (err) {
        error.value = "Error de conexión: Verifica que el backend esté ejecutándose en el puerto 8000.";
    } finally {
        cargando.value = false;
    }
};

// Intercepta la selección de archivos del sistema operativo para generar una previsualización local.
const manejarSeleccionImagen = (event) => {
    const file = event.target.files[0];
    if (file) {
        archivoSeleccionado.value = file;
        // Genera un blob URL temporal en la memoria del navegador para mostrar la imagen sin haberla subido aún.
        proyectoActual.value.imagen_url = URL.createObjectURL(file); 
    }
};

// Orquesta el proceso de guardado en dos fases transaccionales:
// 1. Carga del archivo físico (multipart/form-data) al directorio estático.
// 2. Registro de los metadatos (application/json) en la base de datos.
const guardarProyecto = async () => {
    try {
        cargando.value = true;
        
        // Fase 1: Subida de imagen si el usuario seleccionó un nuevo archivo.
        if (archivoSeleccionado.value) {
            const formData = new FormData();
            formData.append('file', archivoSeleccionado.value);

            const uploadRes = await fetch('/api/upload-imagen/', {
                method: 'POST',
                body: formData
            });

            if (uploadRes.ok) {
                const data = await uploadRes.json();
                // Reemplazamos el blob temporal local por la URL pública definitiva devuelta por el servidor.
                proyectoActual.value.imagen_url = data.url; 
            } else {
                alert("La carga de la imagen falló en el servidor. Operación cancelada.");
                cargando.value = false;
                return; 
            }
        }

        // Fase 2: Ejecución de la operación CRUD.
        const url = modoEdicion.value 
            ? `/api/proyectos/${proyectoActual.value.id}`
            : '/api/proyectos/';
        const metodo = modoEdicion.value ? 'PUT' : 'POST';

        const res = await fetch(url, {
            method: metodo,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(proyectoActual.value)
        });

        if (res.ok) {
            mostrarModal.value = false;
            archivoSeleccionado.value = null; 
            cargarProyectos();
        } else {
            alert("Error al registrar los metadatos del proyecto en la base de datos.");
        }
    } catch (err) {
        console.error("Excepción en el flujo de guardado:", err);
    } finally {
        cargando.value = false;
    }
};

// Ejecuta una petición DELETE y forza la recarga del estado para reflejar el borrado.
const eliminarProyecto = async (id) => {
    if (confirm('¿Confirmas la eliminación permanente de este registro?')) {
        try {
            cargando.value = true;
            await fetch(`/api/proyectos/${id}`, { method: 'DELETE' });
            cargarProyectos();
        } catch (err) {
            console.error("Fallo al ejecutar DELETE:", err);
        }
    }
};

// CONTROLADORES DE INTERFAZ

// Prepara el formulario para una inserción limpia.
const abrirNuevo = () => {
    proyectoActual.value = { ...proyectoInicial };
    archivoSeleccionado.value = null;
    modoEdicion.value = false;
    mostrarModal.value = true;
};

// Clona el objeto seleccionado de la tabla hacia el estado del formulario para evitar mutaciones accidentales antes de guardar.
const abrirEditar = (proyecto) => {
    proyectoActual.value = { ...proyecto };
    archivoSeleccionado.value = null;
    modoEdicion.value = true;
    mostrarModal.value = true;
};

// Ciclo de vida: Inicia la sincronización de datos apenas el componente es montado en el DOM.
onMounted(cargarProyectos);
</script>

<template>
    <div class="admin-page">
        <div class="cms-container">
            <header class="cms-header">
                <div>
                    <h1>Gestión de Contenido</h1>
                    <p>Administración centralizada de los proyectos del portafolio público.</p>
                </div>
                <Button label="Nuevo Proyecto" icon="pi pi-plus" @click="abrirNuevo" />
            </header>

            <Message v-if="error" severity="error" class="mb-4">{{ error }}</Message>

            <!-- Renderizado del DataGrid -->
            <div class="card shadow-sm">
                <DataTable :value="proyectos" :loading="cargando" stripedRows class="p-datatable-sm">
                    <Column field="id" header="ID" style="width: 50px"></Column>
                    
                    <!-- Columna personalizada para la validación visual de la imagen guardada -->
                    <Column header="Vista Previa" style="width: 100px">
                        <template #body="slotProps">
                            <img :src="slotProps.data.imagen_url || 'https://via.placeholder.com/50'" 
                                 class="table-img" 
                                 @error="(e) => e.target.src = 'https://via.placeholder.com/50'" />
                        </template>
                    </Column>
                    
                    <Column field="titulo" header="Título" sortable></Column>
                    <Column field="tecnologias" header="Tecnologías"></Column>
                    
                    <Column header="Acciones" style="width: 150px">
                        <template #body="slotProps">
                            <div class="actions">
                                <Button icon="pi pi-pencil" class="p-button-text" @click="abrirEditar(slotProps.data)" />
                                <Button icon="pi pi-trash" class="p-button-text p-button-danger" @click="eliminarProyecto(slotProps.data.id)" />
                            </div>
                        </template>
                    </Column>
                </DataTable>
            </div>
        </div>

        <!-- Formulario Modal para operaciones de escritura -->
        <Dialog v-model:visible="mostrarModal" :header="modoEdicion ? 'Actualización de Registro' : 'Nuevo Registro'" 
                :modal="true" class="p-fluid custom-dialog">
            
            <div class="form-grid">
                <div class="field">
                    <label>Título del Proyecto</label>
                    <InputText v-model="proyectoActual.titulo" required autofocus />
                </div>
                
                <div class="field">
                    <label>Stack Tecnológico (separado por comas)</label>
                    <InputText v-model="proyectoActual.tecnologias" placeholder="Ej: Python, Vue, FastAPI" />
                </div>

                <div class="field">
                    <label>Descripción de la Solución</label>
                    <Textarea v-model="proyectoActual.descripcion" rows="3" required />
                </div>

                <!-- Bloque de interfaz personalizada para la carga de archivos locales -->
                <div class="field">
                    <label>Recurso Gráfico (Imagen)</label>
                    
                    <!-- Input nativo de HTML oculto mediante CSS. Se activa programáticamente desde el botón de PrimeVue -->
                    <input 
                        type="file" 
                        ref="archivoImagen" 
                        @change="manejarSeleccionImagen" 
                        accept="image/*" 
                        style="display: none;" 
                    />
                    
                    <div class="img-upload-container">
                        <div class="preview-box">
                            <img v-if="proyectoActual.imagen_url" :src="proyectoActual.imagen_url" class="preview-img" />
                            <i v-else class="pi pi-image"></i>
                        </div>
                        
                        <div class="botones-upload">
                            <!-- Este botón dispara el evento click() sobre la referencia del input oculto -->
                            <Button 
                                type="button" 
                                label="Examinar sistema local" 
                                icon="pi pi-upload" 
                                severity="secondary" 
                                outlined 
                                @click="$refs.archivoImagen.click()" 
                            />
                            <small v-if="archivoSeleccionado" class="text-exito">
                                Archivo en cola para subida: {{ archivoSeleccionado.name }}
                            </small>
                        </div>
                    </div>
                </div>

                <div class="grid">
                    <div class="col">
                        <label>URL Entorno de Pruebas (Demo)</label>
                        <InputText v-model="proyectoActual.demo_url" />
                    </div>
                    <div class="col">
                        <label>URL Control de Versiones (Repo)</label>
                        <InputText v-model="proyectoActual.repositorio_url" />
                    </div>
                </div>
            </div>

            <template #footer>
                <Button label="Cancelar Operación" icon="pi pi-times" class="p-button-text" @click="mostrarModal = false"/>
                <!-- Bloquea el botón durante la subida para prevenir envíos múltiples de la misma solicitud POST -->
                <Button label="Procesar y Guardar" icon="pi pi-check" @click="guardarProyecto" :loading="cargando" />
            </template>
        </Dialog>
    </div>
</template>

<style scoped>
.admin-page {
    background: #f4f7f6;
    min-height: 100vh;
    padding: 2rem;
    font-family: 'Inter', sans-serif;
}

.cms-container {
    max-width: 1100px;
    margin: 0 auto;
}

.cms-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 1rem;
}

.cms-header h1 {
    color: #0f172a;
    margin: 0 0 0.5rem 0;
}

.cms-header p {
    color: #64748b;
    margin: 0;
}

.table-img {
    width: 60px;
    height: 40px;
    object-fit: cover;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
}

.actions {
    display: flex;
    gap: 0.5rem;
}

/* Estilos estructurales del formulario */
.form-grid .field {
    margin-bottom: 1.2rem;
}

.field label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #334155;
    font-size: 0.9rem;
}

/* Interfaz de carga de imagen */
.img-upload-container {
    display: flex;
    gap: 1rem;
    align-items: center;
    background-color: #f8fafc;
    padding: 1rem;
    border-radius: 8px;
    border: 1px dashed #cbd5e1;
}

.preview-box {
    width: 100px;
    height: 70px;
    background: #e2e8f0;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.preview-box i {
    font-size: 1.5rem;
    color: #94a3b8;
}

.preview-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.botones-upload {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.text-exito {
    color: #059669;
    font-size: 0.8rem;
    font-weight: 600;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.custom-dialog {
    width: 600px;
}

@media (max-width: 600px) {
    .custom-dialog { width: 95vw; }
    .grid { grid-template-columns: 1fr; }
    .img-upload-container { flex-direction: column; align-items: flex-start; }
}
</style>