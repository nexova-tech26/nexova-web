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
        const respuesta = await fetch('http://127.0.0.1:8000/proyectos/');
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
    <section class="portafolio-vibrante" id="portafolio">
        <div class="contenedor">
            
            <div class="encabezado-seccion" data-aos="fade-up">
                <span class="etiqueta-animada">NUESTROS CLIENTES</span>
                <h2>Transformamos ideas en resultados reales.</h2>
                <p>Cada proyecto es una historia de crecimiento. Descubre como hemos ayudado a empresas como la tuya a dar el salto digital que necesitaban.</p>
            </div>

            <div v-if="cargando" class="estado-carga">
                <i class="pi pi-spin pi-cog pi-spin-anim"></i> Procesando datos...
            </div>

            <div v-else class="carrusel-contenedor" data-aos="fade-up" data-aos-delay="200">
                <Carousel 
                    :value="proyectos" 
                    :numVisible="3" 
                    :numScroll="1" 
                    :responsiveOptions="responsiveOptions" 
                    circular 
                    :autoplayInterval="4500" 
                    class="carrusel-nexova"
                >
                    <template #item="slotProps">
                        
                        <div class="tarjeta-burbuja">
                            
                            <div class="imagen-contenedor">
                                <img v-if="slotProps.data.imagen_url" :src="slotProps.data.imagen_url" :alt="slotProps.data.titulo" />
                                <div v-else class="placeholder-icon">
                                    <i class="pi pi-briefcase"></i>
                                </div>
                            </div>
                            
                            <div class="contenido-texto">
                                
                                <div class="tags-tech">
                                    <Tag v-for="tech in slotProps.data.tecnologias.split(',')" :key="tech" :value="tech.trim()" class="tag-cristal" />
                                </div>
                                
                                <h3>{{ slotProps.data.titulo }}</h3>
                                <p>{{ slotProps.data.descripcion }}</p>
                                
                                <div class="accion-inferior">
                                    <a v-if="slotProps.data.demo_url" :href="slotProps.data.demo_url" target="_blank" class="btn-micro-animado">
                                        <span>Visitar</span>
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
/* === NUEVO FONDO OSCURO CON DEGRADADO EVIDENTE === */
.portafolio-vibrante {
    /* Un destello intenso verde en la esquina superior derecha que se funde en tu azul oscuro corporativo */
    background: radial-gradient(circle at top right, rgba(15, 139, 88, 0.4) 0%, #0f172a 45%, #020617 100%);
    padding: 6rem 1.5rem;
    font-family: 'Inter', sans-serif;
    position: relative;
    overflow: hidden;
}

.contenedor {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}

/* === ENCABEZADO (Adaptado para fondo oscuro) === */
.encabezado-seccion {
    text-align: center;
    max-width: 700px;
    margin: 0 auto 4rem auto;
}

.etiqueta-animada {
    display: inline-block;
    /* La etiqueta brilla en tonos menta más claros para resaltar en la oscuridad */
    background: linear-gradient(90deg, #34d399, #a7f3d0, #34d399);
    background-size: 200% auto;
    color: transparent;
    -webkit-background-clip: text;
    background-clip: text;
    font-weight: 800;
    font-size: 1rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1rem;
    animation: brillarTexto 3s linear infinite;
}

@keyframes brillarTexto {
    to { background-position: 200% center; }
}

.encabezado-seccion h2 {
    font-size: 2.5rem;
    color: #ffffff; /* Letras blancas para contraste */
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1.5rem;
}

.encabezado-seccion p {
    font-size: 1.1rem;
    color: #94a3b8; /* Gris azulado claro */
}

/* === LA TARJETA BURBUJA (Estilo Dark Glassmorphism) === */
.tarjeta-burbuja {
    border-radius: 40px; 
    
    /* Degradado oscuro semi-transparente para la tarjeta */
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%);
    backdrop-filter: blur(10px); /* Efecto cristal */
    
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    
    display: flex;
    flex-direction: column;
    height: 100%;
    margin: 1rem;
    padding: 2rem;
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.tarjeta-burbuja:hover {
    transform: translateY(-15px) scale(1.02);
    box-shadow: 0 25px 40px -10px rgba(15, 139, 88, 0.3);
    border-color: rgba(52, 211, 153, 0.5); /* El borde brilla en menta */
}

.estado-carga {
    text-align: center;
    color: #34d399;
    font-weight: 600;
    padding: 3rem 0;
}

/* === IMAGEN INTEGRADA === */
.imagen-contenedor {
    height: 180px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
    background-color: rgba(255, 255, 255, 0.03); /* Un fondo híper sutil para que el logo resalte */
    border-radius: 20px;
}

.imagen-contenedor img {
    max-width: 90%;
    max-height: 100%;
    object-fit: contain;
    filter: drop-shadow(0 15px 15px rgba(0,0,0,0.3)); 
    transition: transform 0.5s ease;
}

.tarjeta-burbuja:hover .imagen-contenedor img {
    transform: scale(1.1) rotate(-2deg);
}

.placeholder-icon {
    font-size: 4rem;
    color: rgba(255, 255, 255, 0.1);
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
    gap: 0.5rem;
    margin-bottom: 1.2rem;
}

:deep(.tag-cristal) {
    background-color: rgba(15, 139, 88, 0.2) !important;
    color: #34d399 !important;
    border: 1px solid rgba(52, 211, 153, 0.3) !important;
    font-size: 0.75rem !important;
    padding: 0.3rem 0.8rem !important;
    border-radius: 20px !important;
    font-weight: 700 !important;
}

.contenido-texto h3 {
    font-size: 1.5rem;
    color: #ffffff;
    font-weight: 800;
    margin: 0 0 1rem 0;
    line-height: 1.2;
}

.contenido-texto p {
    color: #94a3b8;
    font-size: 1rem;
    line-height: 1.6;
    margin: 0 0 2rem 0;
    flex-grow: 1;
}

/* === BOTÓN CON MICRO-ANIMACIÓN === */
.accion-inferior {
    margin-top: auto;
}

.btn-micro-animado {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background-color: rgba(255, 255, 255, 0.1);
    color: #ffffff;
    padding: 0.8rem 1.5rem;
    border-radius: 30px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.btn-micro-animado i {
    transition: transform 0.3s ease;
    color: #34d399;
}

.btn-micro-animado:hover {
    background-color: #0F8B58;
    color: #ffffff;
    border-color: #0F8B58;
    box-shadow: 0 8px 15px rgba(15, 139, 88, 0.4);
}

.btn-micro-animado:hover i {
    color: #ffffff;
    transform: translate(3px, -3px) rotate(10deg);
}

/* === ESTILOS DEL CARRUSEL PRIMEVUE (Adaptados a fondo oscuro) === */
:deep(.p-carousel-prev), :deep(.p-carousel-next) {
    background-color: rgba(255, 255, 255, 0.05) !important;
    color: #34d399 !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 50% !important;
    width: 3.5rem !important;
    height: 3.5rem !important;
    transition: all 0.3s ease !important;
}

:deep(.p-carousel-prev:hover), :deep(.p-carousel-next:hover) {
    background-color: #0F8B58 !important;
    color: #ffffff !important;
    transform: scale(1.1) !important;
    border-color: #0F8B58 !important;
}

:deep(.p-carousel-indicator button) {
    border-radius: 50px !important;
    height: 6px !important;
    width: 15px !important;
    background-color: rgba(255, 255, 255, 0.2) !important;
}

:deep(.p-carousel-indicator.p-highlight button) {
    background-color: #34d399 !important;
    width: 30px !important;
}

@media (max-width: 768px) {
    .encabezado-seccion h2 { font-size: 2.2rem; }
    .tarjeta-burbuja { margin: 0.5rem; }
}
</style>