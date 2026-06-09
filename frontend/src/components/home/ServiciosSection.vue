<script setup>
import Button from 'primevue/button';
// No necesitamos importar componentes pesados de PrimeVue aquí, 
// haremos el diseño limpio con CSS puro y PrimeIcons para máxima velocidad.

const scrollTo = (idDestino) => {
    const seccion = document.getElementById(idDestino);
    if (seccion) {
        seccion.scrollIntoView({ behavior: 'smooth'});
    }
};
</script>

<template>
    <section class="servicios-premium" id="servicios">
        <div class="contenedor">
            <div class="encabezado-seccion">
                <span class="etiqueta-nexova">Nuestros Servicios</span>
                <h2>Tu visión es grande, tu tecnología también debe serlo.</h2>
                <p>Somos tu <strong>Nexo</strong> tecnológico hacia la transformación digital.</p>
            </div>

            <div class="grid-bento">
                
                <div data-aos="fade-up" class="tarjeta-servicio">
                    <!-- <div class="icono-contenedor">
                        <i class="pi pi-desktop"></i>
                    </div> -->
                    <h3>Desarrollo a la Medida</h3>
                    <p>Deja atrás las soluciones limitadas. Diseñamos software personalizado que se adapta a tu flujo de trabajo real, eliminando errores manuales y potenciando la productividad de tu equipo.</p>
                    <!-- <a href="#" class="enlace-servicio">Saber más <i class="pi pi-arrow-right"></i></a> -->
                </div>

                <div data-aos="fade-up" class="tarjeta-servicio">
                    <!-- <div class="icono-contenedor">
                        <i class="pi pi-globe"></i>
                    </div> -->
                    <h3>Sitios Web Modernos</h3>
                    <p>Tu marca merece una vitrina que impacte. Desarrollamos sitios web con tecnología de carga ultrarrápida y SEO avanzado, garantizando que tu primera impresión sea siempre la más profesional.</p>
                    <!-- <a href="#" class="enlace-servicio">Saber más <i class="pi pi-arrow-right"></i></a> -->
                </div>

                <div data-aos="fade-up" class="tarjeta-servicio">
                    <!-- <div class="icono-contenedor">
                        <i class="pi pi-server"></i>
                    </div> -->
                    <h3>Mantenimiento IT</h3>
                    <p>Nos encargamos de que tu tecnología simplemente funcione. Administración y soporte preventivo a equipos de computo, diseñado para que tu negocio sea imparable, seguro y siempre eficiente.</p>
                    <!-- <a href="#" class="enlace-servicio">Saber más <i class="pi pi-arrow-right"></i></a> -->
                </div>
                <div class="botones-container" data-aos="fade-up" data-aos-delay="300">
                    <Button
                    label="Más información" 
                    size="large" 
                    @click="scrollTo('contacto')" 
                />   
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
/* 1. CONTENEDOR PRINCIPAL: Fondo gris ultra claro para separar del Hero blanco */
.servicios-premium {
    background-color: #f8fafc;
    padding: 6rem 2rem;
    font-family: 'Inter', sans-serif;
}

.contenedor {
    max-width: 1200px;
    margin: 0 auto;
}

.botones-container {
    display: flex;
    gap: 1.5rem;
    margin-top: 1rem;
}

/* 2. ENCABEZADO: Centrado, limpio, con tu identidad */
.encabezado-seccion {
    text-align: center;
    max-width: 700px;
    margin: 0 auto 4rem auto;
}

.etiqueta-nexova {
    color: #0F8B58; /* Verde Nexova */
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    display: block;
    margin-bottom: 1rem;
}

.encabezado-seccion h2 {
    font-size: 2.8rem;
    color: #0f172a;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1.5rem;
}

.encabezado-seccion p {
    font-size: 1.15rem;
    color: #64748b;
    line-height: 1.6;
}

/* 3. CUADRÍCULA (Grid): Alineación perfecta automática */
.grid-bento {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
}

/* 4. TARJETAS DE SERVICIO: El estilo Agencia Premium */
.tarjeta-servicio {
    background: linear-gradient(
        to bottom right,
        #0f172a 0%,
        #0c1a3a 40%,
        #0e2a45 70%,
        #0f172a 100%
    );
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 2.5rem 2rem;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: justify;
}

/* Interacción moderna: Sombra suave y borde color menta al pasar el mouse */
.tarjeta-servicio:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02);
    border-color: #BCE4D3; /* Verde Menta */
}

/* 5. ICONOS: Fondo menta claro, icono verde Nexova */
.icono-contenedor {
    background-color: #eaf6f0;
    width: 60px;
    height: 60px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
}

.icono-contenedor i {
    font-size: 1.8rem;
    color: #0F8B58; /* Verde Nexova */
}

/* 6. TIPOGRAFÍA INTERNA */
.tarjeta-servicio h3 {
    font-size: 1.4rem;
    color: #ffffff;
    margin-bottom: 1rem;
    font-weight: 700;
}

.tarjeta-servicio p {
    color: #ffffff;
    line-height: 1.6;
    margin-bottom: 2rem;
    font-size: 1rem;
    flex-grow: 1; /* Empuja el enlace hacia el fondo */
}

/* 7. ENLACE DE ACCIÓN */
.enlace-servicio {
    color: #34d399;
    text-decoration: none;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.95rem;
    transition: gap 0.2s ease;
}

/* El icono de la flecha se mueve un poco a la derecha al pasar el mouse */
.tarjeta-servicio:hover .enlace-servicio {
    gap: 0.8rem; 
}

/* 8. RESPONSIVO (Móviles) */
@media (max-width: 768px) {
    .encabezado-seccion h2 {
        font-size: 2.2rem;
    }
    .tarjeta-servicio {
        padding: 2rem 1.5rem;
    }
}
</style>