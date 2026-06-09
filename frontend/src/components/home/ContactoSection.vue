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
    { nombre: 'Consultoría', code: 'consulting' },
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
                <div class="info-contenido">
                    <span class="etiqueta-brillante">El primer paso cuesta cero</span>
                    
                    <h2>Tu competencia ya se digitalizó. ¿Qué estás esperando?</h2>
                    
                    <p class="texto-persuasivo">
                        Tu empresa ha evolucionado, ¿tu tecnología también? Es momento de que tu infraestructura digital refleje la calidad de lo que ofreces.
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
                                <i class="pi pi-map-marker"></i>
                            </div>
                            <div>
                                <h4>Ubicación</h4>
                                <p>Colombia</p>
                            </div>
                        </div>
                    </div>

                    <div class="sello-confianza">
                        <i class="pi pi-clock"></i>
                        <span>Te garantizamos una pronta respuesta</span>
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
                        <label>Correo Electrónico</label>
                        <InputText v-model="formulario.email" type="email" placeholder="juanperez@ejemplo.com" class="input-moderno" required />
                    </div>

                    <div class="campo contenedor-restriccion">
                        <label>¿En qué podemos ayudarte?</label>
                        <Dropdown v-model="formulario.servicio" :options="servicios" optionLabel="nombre" placeholder="Selecciona un área de enfoque" class="input-moderno select-responsivo" />
                    </div>

                    <div class="campo">
                        <label>¿Tienes alguna idea?</label>
                        <Textarea v-model="formulario.mensaje" rows="4" placeholder="Cuéntanos tu plan!" class="input-moderno" required />
                    </div>

                    <Button type="submit" 
                        label="Agenda consultoría gratuita. Te llamamos!" 
                        icon="pi pi-send" 
                        iconPos="right" :loading="enviando" 
                        class="btn-enviar w-full" 
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
/* Reseteo universal dentro del componente para evitar paddings rebeldes */
.contacto-premium * {
    box-sizing: border-box;
}

.contacto-premium {
    background-color: #f8fafc;
    padding: 6rem 1.5rem;
    font-family: 'Inter', sans-serif;
    display: flex;
    justify-content: center;
    width: 100%;
    overflow-x: hidden; /* Cortafuegos nivel 1 */
}

.contenedor-contacto {
    max-width: 1200px;
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.1);
    min-width: 0; /* Cortafuegos nivel 2 */
}

/* === PANEL IZQUIERDO (INFO) === */
.panel-info {
    background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%);
    color: white;
    padding: 4rem 3rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-width: 0;
}

.etiqueta-brillante {
    display: inline-block;
    color: #34d399;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

.panel-info h2 {
    font-size: 2.8rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    color: #ffffff;
}

.texto-persuasivo {
    color: #94a3b8;
    font-size: 1.1rem;
    line-height: 1.7;
    margin-bottom: 3rem;
}

.items-contacto {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    margin-bottom: 3rem;
}

.item {
    display: flex;
    align-items: center;
    gap: 1.2rem;
}

.icono-caja {
    width: 48px;
    height: 48px;
    background-color: rgba(15, 139, 88, 0.2);
    border: 1px solid rgba(15, 139, 88, 0.4);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #34d399;
    font-size: 1.3rem;
}

.item h4 {
    margin: 0 0 0.3rem 0;
    font-size: 1rem;
    color: #ffffff;
}

.item p {
    margin: 0;
    color: #94a3b8;
    font-size: 0.95rem;
}

.sello-confianza {
    background-color: rgba(255, 255, 255, 0.05);
    padding: 1.5rem;
    border-radius: 12px;
    border-left: 4px solid #0F8B58;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
}

.sello-confianza i {
    color: #34d399;
    font-size: 1.2rem;
    margin-top: 0.2rem;
}

.sello-confianza span {
    color: #e2e8f0;
    font-size: 0.95rem;
    line-height: 1.5;
}

/* === PANEL DERECHO (FORMULARIO) === */
.panel-formulario {
    background-color: #ffffff;
    padding: 4rem 3rem;
    min-width: 0; /* Cortafuegos nivel 3: Grid Item */
    width: 100%;
}

.formulario-limpio {
    display: flex;
    flex-direction: column;
    gap: 1.8rem;
    width: 100%;
    min-width: 0; /* Cortafuegos nivel 4: Flex Item */
}

.campo {
    width: 100%;
    min-width: 0; /* Cortafuegos nivel 5: Elemento de entrada */
    display: flex;
    flex-direction: column;
}

.contenedor-restriccion {
    max-width: 100%;
    overflow: hidden; /* Garantiza que PrimeVue no desborde la caja bajo ninguna circunstancia */
}

.campo label {
    display: block;
    font-size: 0.9rem;
    font-weight: 700;
    color: #334155;
    margin-bottom: 0.6rem;
}

:deep(.input-moderno) {
    width: 100%;
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    padding: 0.8rem 1rem;
    transition: all 0.3s;
    font-family: inherit;
    font-size: 1rem;
}

:deep(.input-moderno:focus), :deep(.input-moderno.p-focus) {
    border-color: #0F8B58;
    box-shadow: 0 0 0 3px rgba(15, 139, 88, 0.1);
}

/* === ARQUITECTURA DEL DROPDOWN === */
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
    width: 10%; /* Un valor pequeño para obligar a que flexbox controle el crecimiento */
    overflow: hidden !important;
    white-space: nowrap !important;
    text-overflow: ellipsis !important;
    display: block !important;
    padding-right: 1.5rem !important;
}

.w-full {
    width: 100%;
}

.btn-enviar {
    padding: 1.2rem;
    font-weight: 700;
    font-size: 1.1rem;
    border-radius: 8px;
    margin-top: 1rem;
    white-space: normal;
    line-height: 1.3;
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
    color: #94a3b8;
    font-size: 0.9rem;
    font-weight: 600;
    position: relative;
    z-index: 2;
}

.btn-whatsapp {
    background-color: #25D366;
    border: none;
    color: white;
    padding: 1rem;
    font-weight: 700;
    border-radius: 8px;
    white-space: normal;
}

.btn-whatsapp:hover {
    background-color: #20bd5a;
}

/* === RESPONSIVO MÓVIL === */
@media (max-width: 991px) {
    .contenedor-contacto {
        grid-template-columns: 1fr;
    }
    .panel-info, .panel-formulario {
        padding: 3rem 2rem;
    }
}

@media (max-width: 768px) {
    .contacto-premium {
        padding: 3rem 1rem;
    }
    
    .panel-info, .panel-formulario {
        padding: 2.5rem 1.5rem;
    }
    
    .panel-info h2 {
        font-size: 1.8rem; 
        line-height: 1.2;
        margin-bottom: 1rem;
        word-wrap: break-word;
    }
    
    .texto-persuasivo {
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    .items-contacto {
        gap: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .item h4 {
        font-size: 0.95rem;
    }
    
    .item p {
        font-size: 0.85rem;
    }

    .formulario-limpio {
        gap: 1.2rem; 
    }
    
    .campo label {
        font-size: 0.85rem;
        margin-bottom: 0.4rem;
    }
    
    :deep(.input-moderno) {
        padding: 0.7rem 1rem;
        font-size: 0.95rem;
    }
    
    .btn-enviar {
        font-size: 0.95rem;
        padding: 1rem;
    }
}
</style>