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
            
            <!-- <div class="badge-elegante" data-aos="fade-down">
                <i class="pi pi-check-circle"></i> Arquitectura IT & Desarrollo
            </div> -->
            <br>
            
            <h1 data-aos="fade-up" data-aos-delay="100">
                Tu negocio abierto 24/7, <br> <span class="text-gradient">trabajando mientras descansas</span>
            </h1>
            
            <p data-aos="fade-up" data-aos-delay="200">
Creamos tu presencia digital desde cero: web profesional, tienda en línea o software a la medida. Sin tecnicismos, sin vueltas y con resultados que sí se ven.</p>
            
            <div class="botones-container" data-aos-delay="300">
                <Button 
                    label="Agenda tu consultoría gratuita" 
                    icon="pi pi-calendar" 
                    size="large" 
                    @click="scrollTo('contacto')" 
                />
                <Button 
                    label="Ver Servicios" 
                    icon="pi pi-arrow-down" 
                    iconPos="right" 
                    severity="primary" 
                    text 
                    size="large"
                    color="White"
                    @click="scrollTo('servicios')" 

                />
            </div>

        </div>
    </section>
</template>

<style scoped>
.hero-clean {
    min-height: 85vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: transparent;
    text-align: center;
    padding: 2rem;
}

.hero-content {
    max-width: 900px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
    /* Pequeña animación de entrada */
    animation: fadeUp 0.8s ease-out; 
}

/* El Badge superior, ahora más sutil y corporativo */
.badge-elegante {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background-color: #eaf6f0; /* Un tono ultraclaro derivado de tu menta */
    color: #0F8B58; /* Tu Verde Nexova */
    padding: 0.5rem 1.2rem;
    border-radius: 30px;
    font-size: 0.9rem;
    font-weight: 700;
    border: 1px solid #BCE4D3; /* Borde color menta */
}

/* Tipografía de Alto Impacto */
h1 {
    font-size: 4.5rem;
    line-height: 1.1;
    margin: 0;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: -1.5px; /* Letras ligeramente más juntas dan un look de agencia top */
}

/* Efecto de texto con degradado moderno */
.text-gradient {
    background: linear-gradient(to right, #0F8B58, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

p {
    font-size: 1.25rem;
    color: #34d399;
    line-height: 1.7;
    max-width: 700px;
    margin: 0;
}

.botones-container {
    display: flex;
    gap: 1.5rem;
    margin-top: 1rem;
}

/* Animación sutil de aparición desde abajo */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Ajustes para móviles */
@media (max-width: 768px) {
    h1 { font-size: 2.8rem; }
    .botones-container { flex-direction: column; width: 100%; }
    .botones-container button { width: 100%; }
}
</style>