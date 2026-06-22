<script setup>
import Button from 'primevue/button';

const scrollTo = (idDestino) => {
    const seccion = document.getElementById(idDestino);
    if (seccion) {
        seccion.scrollIntoView({ behavior: 'smooth'});
    }
};
</script>

<template>
    <section class="hero-clean">
        <div class="hero-content">
            
            <!-- Badge Top -->
            <div class="badge-elegante" data-aos="fade-down">
                <span class="pulse-dot"></span>
                Expertos en Transformación Digital
            </div>
            
            <h1 data-aos="fade-up" data-aos-delay="100">
                Tu negocio abierto 24/7, <span class="text-gradient">trabajando mientras descansas</span>
            </h1>
            
            <p data-aos="fade-up" data-aos-delay="200">
                Creamos tu presencia digital desde cero: web profesional, tienda en línea o software a la medida. Sin tecnicismos, sin vueltas y con resultados que sí se ven.
            </p>
            
            <div class="botones-container" data-aos-delay="300" data-aos="fade-up">
                <Button 
                    label="Agenda tu consultoría gratuita" 
                    icon="pi pi-calendar" 
                    size="large" 
                    class="btn-primary-nexova"
                    @click="scrollTo('contacto')" 
                />
                <Button 
                    label="Ver Servicios" 
                    icon="pi pi-arrow-down" 
                    iconPos="right" 
                    severity="secondary" 
                    outlined
                    size="large"
                    class="btn-outline-nexova"
                    @click="scrollTo('servicios')" 
                />
            </div>

        </div>
    </section>
</template>

<style scoped>
.hero-clean {
    min-height: 100vh;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    text-align: center;
    padding: 8rem 1.5rem 3rem 1.5rem; 
    
    /* === ELIMINAMOS EL TRANSPARENTE Y MATAMOS EL AZUL === */
    background-color: #09090b; /* Negro corporativo puro */
    
    /* Le agregamos un resplandor esmeralda que cae desde arriba */
    background-image: radial-gradient(circle at top center, rgba(15, 139, 88, 0.2) 0%, rgba(9, 9, 11, 1) 60%);
    
    position: relative;
    overflow: hidden;
}

/* cuadricula*/
.hero-clean::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: 0;
    pointer-events: none;
}

.hero-content {
    max-width: 900px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem; 
    position: relative;
    z-index: 1; /* Asegura que el texto esté por encima de la cuadrícula */
}

/* -badge */
.badge-elegante {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background-color: rgba(15, 139, 88, 0.1); /* Fondo translúcido */
    color: #34d399; /* Verde claro vibrante */
    padding: 0.5rem 1.2rem;
    border-radius: 10px;
    font-size: 0.9rem;
    font-weight: 600;
    border: 1px solid rgba(15, 139, 88, 0.3);
    backdrop-filter: blur(10px);
}

.pulse-dot {
    width: 8px;
    height: 8px;
    background-color: #34d399;
    border-radius: 50%;
    box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7);
    animation: pulse 2s infinite;
}

/* tipografia */
h1 {
    font-size: clamp(2.5rem, 5vw, 4.5rem); /* Escalado fluido perfecto */
    line-height: 1.1;
    margin: 0;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -1px;
}

.text-gradient {
    background: linear-gradient(135deg, #34d399 0%, #0F8B58 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
}

p {
    font-size: 1.15rem;
    color: #a1a1aa; /* Gris platinado para mejor lectura */
    line-height: 1.6;
    max-width: 650px;
    margin: 0;
    font-weight: 400;
}

/* --- BOTONES --- */
.botones-container {
    display: flex;
    gap: 1.5rem;
    margin-top: 1rem;
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

:deep(.btn-outline-nexova) {
    color: #ffffff;
    border-color: rgba(255,255,255,0.3);
    transition: all 0.3s ease;
}

:deep(.btn-outline-nexova:hover) {
    background-color: rgba(255,255,255,0.1);
    border-color: #ffffff;
}

/* --- ANIMACIONES --- */
@keyframes pulse {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(52, 211, 153, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0); }
}

/* --- RESPONSIVIDAD --- */
@media (max-width: 768px) {
    .botones-container { flex-direction: column; width: 100%; gap: 1rem; }
    .botones-container :deep(.p-button) { width: 100%; justify-content: center; }
    p { font-size: 1.05rem; }
    .hero-clean { padding: 5rem 2.5rem; }
}
</style>