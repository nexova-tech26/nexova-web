<script setup>
import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Dropdown from 'primevue/dropdown';
import Button from 'primevue/button';

const formulario = ref({
    nombre: '',
    email: '',
    servicio: null,
    mensaje: ''
});

const enviando = ref(false);

const servicios = ref([
    { nombre: 'Desarrollo de sitios web o tiendas online', code: 'web' },
    { nombre: 'Desarrollo de software a medida', code: 'web_custom' },
    { nombre: 'Mantenimiento preventivo de equipos de computo', code: 'mantenimiento' },
    { nombre: 'Consultoría e Infraestructura', code: 'consulting' },
    { nombre: 'Otro', code: 'otro' }
]);

const enviarMensaje = async () => {
    enviando.value = true;
    
    try {
        const servicioSeleccionado = formulario.value.servicio ? formulario.value.servicio.nombre : 'No especificado';

        const datosEnvio = {
            nombre: formulario.value.nombre,
            email: formulario.value.email,
            servicio: servicioSeleccionado,
            mensaje: formulario.value.mensaje
        };

        const respuesta = await fetch('/api/contacto/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(datosEnvio)
        });

        if (respuesta.ok) {
            alert("¡Mensaje enviado con éxito! Te contactaremos pronto.");
            formulario.value = { nombre: '', email: '', servicio: null, mensaje: '' };
        } else {
            alert("Hubo un problema procesando tu solicitud. Por favor intenta de nuevo.");
        }
    } catch (error) {
        console.error("Error de comunicación con FastAPI:", error);
        alert("No se pudo conectar con el servidor. Verifica tu conexión.");
    } finally {
        enviando.value = false;
    }
};

const irAWhatsApp = () => {
    window.open('https://wa.me/573209238674?text=Hola%20equipo%20Nexova,%20me%20gustaría%20hablar%20sobre%20un%20proyecto.', '_blank');
};
</script>

<template>
    <section class="contacto-premium" id="contacto">
        <div class="contenedor-contacto">
            
            <div class="panel-info" data-aos="fade-right">
                <div class="glow-verde"></div> <div class="info-contenido">
                    <span class="etiqueta-brillante">Hablemos de negocios</span>
                    
                    <h2>Transforma tu operación con tecnología a medida.</h2>
                    
                    <p class="texto-persuasivo">
                        Ya sea que necesites automatizar procesos, modernizar tu presencia web o asegurar tu infraestructura. Cuéntanos tu desafío y diseñaremos el plan exacto para resolverlo.
                    </p>

                    <div class="items-contacto">
                        <div class="item">
                            <div class="icono-caja">
                                <i class="pi pi-envelope"></i>
                            </div>
                            <div>
                                <h4>Email directo</h4>
                                <p>contacto.nexovatech@gmail.com</p>
                            </div>
                        </div>

                        <div class="item">
                            <div class="icono-caja">
                                <i class="pi pi-whatsapp"></i>
                            </div>
                            <div>
                                <h4>Línea de atención</h4>
                                <p>+57 320 9238674</p>
                            </div>
                        </div>
                        
                        <div class="item">
                            <div class="icono-caja">
                                <i class="pi pi-map-marker"></i>
                            </div>
                            <div>
                                <h4>Ubicación</h4>
                                <p>Villavicencio, Meta — Cobertura Nacional</p>
                            </div>
                        </div>
                    </div>

                    <div class="sello-confianza">
                        <i class="pi pi-bolt"></i>
                        <span>¡Te respondemos hoy mismo!</span>
                    </div>
                </div>
            </div>

            <div class="panel-formulario" data-aos="fade-left" data-aos-delay="100">
                <form @submit.prevent="enviarMensaje" class="formulario-limpio">
                    
                    <div class="campo">
                        <label>Nombre o Empresa</label>
                        <InputText v-model="formulario.nombre" placeholder="Ingresa tu nombre o el de la empresa" class="input-moderno" required />
                    </div>

                    <div class="campo">
                        <label>Correo Electrónico corporativo</label>
                        <InputText v-model="formulario.email" type="email" placeholder="tucorreo@empresa.com" class="input-moderno" required />
                    </div>

                    <div class="campo contenedor-restriccion">
                        <label>¿En qué área podemos apoyarte?</label>
                        <Dropdown v-model="formulario.servicio" :options="servicios" optionLabel="nombre" placeholder="Selecciona un servicio" class="input-moderno select-responsivo" />
                    </div>

                    <div class="campo">
                        <label>Detalles del proyecto</label>
                        <Textarea v-model="formulario.mensaje" rows="4" placeholder="Cuéntanos un poco sobre lo que tienes en mente..." class="input-moderno" required />
                    </div>

                    <Button type="submit" 
                        label="Solicitar consultoría gratuita" 
                        icon="pi pi-send" 
                        iconPos="right" :loading="enviando" 
                        class="btn-enviar btn-primary-nexova w-full" 
                        size="large" />
                </form>

                <div class="separador-whatsapp">
                    <span>O si prefieres atención inmediata</span>
                </div>

                <Button type="button" label="Iniciar chat por WhatsApp" icon="pi pi-whatsapp" class="btn-whatsapp w-full" @click="irAWhatsApp" />
            </div>

        </div>
    </section>
</template>

<style scoped>
/* Reseteo universal dentro del componente */
.contacto-premium * {
    box-sizing: border-box;
}

.contacto-premium {
    background-color: #f8fafc;
    padding: 8rem 1.5rem;
    font-family: 'Inter', sans-serif;
    display: flex;
    justify-content: center;
    width: 100%;
    overflow-x: hidden;
}

.contenedor-contacto {
    max-width: 1200px;
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.08);
    min-width: 0; 
}

/* === PANEL IZQUIERDO (INFO) === */
.panel-info {
    background-color: #18181b; /* Gris muy oscuro, alineado con la sección Planes */
    color: white;
    padding: 4.5rem 3.5rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-width: 0;
    position: relative;
    overflow: hidden;
}

/* Resplandor verde corporativo de fondo */
.glow-verde {
    position: absolute;
    top: -20%;
    left: -20%;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(15, 139, 88, 0.15) 0%, rgba(24, 24, 27, 0) 70%);
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
}

.info-contenido {
    position: relative;
    z-index: 1;
}

.etiqueta-brillante {
    display: inline-block;
    color: #34d399;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

.panel-info h2 {
    font-size: clamp(2rem, 3.5vw, 2.6rem);
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 1.5rem;
    color: #ffffff;
    letter-spacing: -0.5px;
}

.texto-persuasivo {
    color: #a1a1aa;
    font-size: 1.05rem;
    line-height: 1.7;
    margin-bottom: 3rem;
}

.items-contacto {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    margin-bottom: 3.5rem;
}

.item {
    display: flex;
    align-items: center;
    gap: 1.2rem;
}

.icono-caja {
    width: 50px;
    height: 50px;
    background-color: rgba(15, 139, 88, 0.15);
    border: 1px solid rgba(15, 139, 88, 0.3);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #34d399;
    font-size: 1.3rem;
    transition: all 0.3s ease;
}

.item:hover .icono-caja {
    background-color: #0F8B58;
    color: #ffffff;
    transform: scale(1.05);
}

.item h4 {
    margin: 0 0 0.3rem 0;
    font-size: 1rem;
    color: #f4f4f5;
    font-weight: 600;
}

.item p {
    margin: 0;
    color: #a1a1aa;
    font-size: 0.95rem;
}

.sello-confianza {
    background-color: rgba(255, 255, 255, 0.03);
    padding: 1.2rem 1.5rem;
    border-radius: 12px;
    border-left: 4px solid #0F8B58;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.sello-confianza i {
    color: #34d399;
    font-size: 1.2rem;
}

.sello-confianza span {
    color: #d4d4d8;
    font-size: 0.95rem;
    line-height: 1.5;
    font-weight: 500;
}

/* === PANEL DERECHO (FORMULARIO) === */
.panel-formulario {
    background-color: #ffffff;
    padding: 4.5rem 3.5rem;
    min-width: 0; 
    width: 100%;
}

.formulario-limpio {
    display: flex;
    flex-direction: column;
    gap: 1.8rem;
    width: 100%;
    min-width: 0; 
}

.campo {
    width: 100%;
    min-width: 0; 
    display: flex;
    flex-direction: column;
}

.contenedor-restriccion {
    max-width: 100%;
    overflow: hidden; 
}

.campo label {
    display: block;
    font-size: 0.95rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 0.5rem;
}

:deep(.input-moderno) {
    width: 100%;
    border-radius: 10px;
    border: 1px solid #cbd5e1;
    padding: 0.9rem 1rem;
    transition: all 0.3s;
    font-family: inherit;
    font-size: 1rem;
    background-color: #f8fafc;
}

:deep(.input-moderno:focus), :deep(.input-moderno.p-focus) {
    border-color: #0F8B58;
    background-color: #ffffff;
    box-shadow: 0 0 0 4px rgba(15, 139, 88, 0.1);
    outline: none;
}

/* === DROPDOWN === */
:deep(.select-responsivo) {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    display: flex !important;
    align-items: center;
}

:deep(.select-responsivo .p-dropdown-label),
:deep(.select-responsivo .p-select-label) {
    flex: 1 1 auto;
    width: 10%; 
    overflow: hidden !important;
    white-space: nowrap !important;
    text-overflow: ellipsis !important;
    display: block !important;
    padding-right: 1.5rem !important;
}

/* === BOTONES === */
.w-full {
    width: 100%;
}

.btn-enviar {
    padding: 1.2rem;
    font-weight: 700;
    font-size: 1.05rem;
    border-radius: 10px;
    margin-top: 0.5rem;
    white-space: normal;
    line-height: 1.3;
}

:deep(.btn-primary-nexova) {
    background-color: #0F8B58;
    border-color: #0F8B58;
    transition: all 0.3s ease;
}

:deep(.btn-primary-nexova:hover) {
    background-color: #0b6b43;
    border-color: #0b6b43;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px -6px rgba(15, 139, 88, 0.6);
}

.separador-whatsapp {
    text-align: center;
    position: relative;
    margin: 2.5rem 0;
}

.separador-whatsapp::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    height: 1px;
    background-color: #e2e8f0;
    z-index: 1;
}

.separador-whatsapp span {
    background-color: #ffffff;
    padding: 0 1rem;
    color: #64748b;
    font-size: 0.9rem;
    font-weight: 500;
    position: relative;
    z-index: 2;
}

.btn-whatsapp {
    background-color: #25D366;
    border: none;
    color: white;
    padding: 1.1rem;
    font-weight: 700;
    font-size: 1.05rem;
    border-radius: 10px;
    white-space: normal;
    transition: all 0.3s ease;
}

.btn-whatsapp:hover {
    background-color: #20bd5a;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px -6px rgba(37, 211, 102, 0.4);
}

/* === RESPONSIVO === */
@media (max-width: 991px) {
    .contenedor-contacto {
        grid-template-columns: 1fr;
    }
    .panel-info, .panel-formulario {
        padding: 3rem 2.5rem;
    }
}

@media (max-width: 768px) {
    .contacto-premium {
        padding: 4rem 1rem;
    }
    
    .panel-info, .panel-formulario {
        padding: 2.5rem 1.5rem;
    }
    
    .panel-info h2 {
        font-size: 1.8rem; 
        margin-bottom: 1rem;
    }
    
    .items-contacto {
        gap: 1.5rem;
    }

    .formulario-limpio {
        gap: 1.2rem; 
    }
    
    :deep(.input-moderno) {
        padding: 0.8rem 1rem;
    }
}
</style>