<script setup>
import { ref, onMounted } from 'vue';
import Carousel from 'primevue/carousel';
import Tag from 'primevue/tag';

const proyectos = ref([]);
const cargando = ref(true);

const responsiveOptions = ref([
    { breakpoint: '1199px', numVisible: 3, numScroll: 1 },
    { breakpoint: '991px', numVisible: 2, numScroll: 1 },
    { breakpoint: '767px', numVisible: 1, numScroll: 1 }
]);

const cargarProyectos = async () => {
    try {
        // Agregué un slash inicial para evitar errores de ruta relativa en Vue Router
        const respuesta = await fetch('/api/proyectos/');
        if (respuesta.ok) {
            proyectos.value = await respuesta.json();
        }
    } catch (error) {
        console.error("Error cargando proyectos:", error);
    } finally {
        cargando.value = false;
    }
};

onMounted(() => {
    cargarProyectos();
});
</script>

<template>
    <section class="portafolio-premium" id="portafolio">
        <div class="glow-fondo"></div>
        
        <div class="contenedor">
            
            <div class="encabezado-seccion" data-aos="fade-up">
                <span class="etiqueta-nexova">Nuestros Clientes</span>
                <h2>Transformamos ideas en resultados reales.</h2>
                <p>Cada proyecto es una historia de crecimiento. Descubre cómo hemos ayudado a empresas a dar el salto digital que necesitaban.</p>
            </div>

            <div v-if="cargando" class="estado-carga">
                <i class="pi pi-spin pi-spinner" style="font-size: 2rem; margin-bottom: 1rem;"></i>
                <p>Cargando casos de éxito...</p>
            </div>

            <div v-else class="carrusel-contenedor" data-aos="fade-up" data-aos-delay="100">
                <Carousel 
                    :value="proyectos" 
                    :numVisible="3" 
                    :numScroll="1" 
                    :responsiveOptions="responsiveOptions" 
                    circular 
                    :autoplayInterval="5000" 
                    class="carrusel-nexova"
                >
                    <template #item="slotProps">
                        
                        <div class="tarjeta-portafolio">
                            
                            <div class="imagen-contenedor">
                                <img v-if="slotProps.data.imagen_url" :src="slotProps.data.imagen_url" :alt="slotProps.data.titulo" />
                                <div v-else class="placeholder-icon">
                                    <i class="pi pi-briefcase"></i>
                                </div>
                            </div>
                            
                            <div class="contenido-texto">
                                
                                <div class="tags-tech">
                                    <Tag v-for="tech in slotProps.data.tecnologias.split(',')" :key="tech" :value="tech.trim()" class="tag-nexova" />
                                </div>
                                
                                <h3>{{ slotProps.data.titulo }}</h3>
                                <p>{{ slotProps.data.descripcion }}</p>
                                
                                <div class="accion-inferior">
                                    <a v-if="slotProps.data.demo_url" :href="slotProps.data.demo_url" target="_blank" class="btn-visitar">
                                        <span>Ver proyecto</span>
                                        <i class="pi pi-arrow-up-right"></i>
                                    </a>
                                </div>
                            </div>
                            
                        </div>

                    </template>
                </Carousel>
            </div>
            
        </div>
    </section>
</template>

<style scoped>
/* === ESTRUCTURA Y FONDOS === */
.portafolio-premium {
    background-color: #09090b; /* Negro puro corporativo */
    padding: 8rem 1.5rem;
    font-family: 'Inter', sans-serif;
    position: relative;
    overflow: hidden;
}

/* Destello sutil de fondo para dar profundidad */
.glow-fondo {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80%;
    height: 500px;
    background: radial-gradient(ellipse at top, rgba(15, 139, 88, 0.08) 0%, rgba(9, 9, 11, 0) 70%);
    pointer-events: none;
}

.contenedor {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}

/* === ENCABEZADO === */
.encabezado-seccion {
    text-align: center;
    max-width: 700px;
    margin: 0 auto 4rem auto;
}

.etiqueta-nexova {
    color: #34d399; 
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    display: inline-block;
    margin-bottom: 1rem;
    padding: 0.3rem 1rem;
    background-color: rgba(52, 211, 153, 0.1);
    border-radius: 20px;
}

.encabezado-seccion h2 {
    font-size: clamp(2rem, 4vw, 2.8rem);
    color: #ffffff;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1.2rem;
    letter-spacing: -0.5px;
}

.encabezado-seccion p {
    font-size: 1.15rem;
    color: #a1a1aa;
    line-height: 1.6;
}

/* === TARJETAS DEL PORTAFOLIO === */
.tarjeta-portafolio {
    background-color: #18181b; /* Zinc oscuro */
    border: 1px solid #27272a;
    border-radius: 24px;
    display: flex;
    flex-direction: column;
    height: 100%;
    margin: 1rem;
    padding: 2rem;
    transition: all 0.4s ease;
}

.tarjeta-portafolio:hover {
    transform: translateY(-8px);
    border-color: #0F8B58;
    box-shadow: 0 15px 35px rgba(15, 139, 88, 0.15);
}

.estado-carga {
    text-align: center;
    color: #34d399;
    padding: 5rem 0;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.estado-carga p {
    color: #a1a1aa;
    font-size: 1.1rem;
    margin: 0;
}

/* === IMAGEN INTEGRADA === */
.imagen-contenedor {
    height: 200px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.8rem;
    background-color: #09090b; /* Contraste para que la imagen resalte */
    border: 1px solid #27272a;
    border-radius: 16px;
    overflow: hidden;
    padding: 1rem;
}

.imagen-contenedor img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    transition: transform 0.5s ease;
}

.tarjeta-portafolio:hover .imagen-contenedor img {
    transform: scale(1.05);
}

.placeholder-icon {
    font-size: 3.5rem;
    color: #3f3f46;
}

/* === CONTENIDO DE TEXTO === */
.contenido-texto {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}

.tags-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 1.2rem;
}

:deep(.tag-nexova) {
    background-color: rgba(15, 139, 88, 0.15) !important;
    color: #34d399 !important;
    border: 1px solid rgba(52, 211, 153, 0.2) !important;
    font-size: 0.75rem !important;
    padding: 0.3rem 0.8rem !important;
    border-radius: 20px !important;
    font-weight: 600 !important;
}

.contenido-texto h3 {
    font-size: 1.4rem;
    color: #ffffff;
    font-weight: 800;
    margin: 0 0 1rem 0;
    line-height: 1.3;
}

.contenido-texto p {
    color: #a1a1aa;
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 0 0 2rem 0;
    flex-grow: 1;
}

/* === BOTÓN === */
.accion-inferior {
    margin-top: auto;
}

.btn-visitar {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background-color: transparent;
    color: #ffffff;
    padding: 0.8rem 1.5rem;
    border-radius: 10px;
    font-weight: 600;
    font-size: 0.95rem;
    text-decoration: none;
    transition: all 0.3s ease;
    border: 1px solid #52525b;
}

.btn-visitar i {
    transition: transform 0.3s ease;
    color: #34d399;
}

.btn-visitar:hover {
    background-color: #27272a;
    border-color: #a1a1aa;
}

.btn-visitar:hover i {
    transform: translate(3px, -3px);
}

/* === ESTILOS DEL CARRUSEL PRIMEVUE === */
:deep(.p-carousel-prev), :deep(.p-carousel-next) {
    background-color: #18181b !important;
    color: #ffffff !important;
    border: 1px solid #3f3f46 !important;
    border-radius: 50% !important;
    width: 3rem !important;
    height: 3rem !important;
    transition: all 0.3s ease !important;
    margin: 0 0.5rem !important;
}

:deep(.p-carousel-prev:hover), :deep(.p-carousel-next:hover) {
    background-color: #0F8B58 !important;
    border-color: #0F8B58 !important;
    transform: scale(1.05) !important;
}

:deep(.p-carousel-indicator button) {
    border-radius: 50px !important;
    height: 6px !important;
    width: 15px !important;
    background-color: #3f3f46 !important;
    transition: all 0.3s ease !important;
}

:deep(.p-carousel-indicator.p-highlight button) {
    background-color: #34d399 !important;
    width: 30px !important;
}

@media (max-width: 768px) {
    .portafolio-premium {
        padding: 5rem 1.5rem;
    }
    .encabezado-seccion h2 { font-size: 2.2rem; }
    .tarjeta-portafolio { padding: 1.5rem; margin: 0.5rem; }
}
</style>