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
    <section class="servicios-premium" id="servicios">
        <div class="contenedor">
            
            <div class="encabezado-seccion" data-aos="fade-up">
                <span class="etiqueta-nexova">Nuestros Servicios</span>
                <h2>Tu visión es grande, tu tecnología también debe serlo.</h2>
                <p>Soluciones digitales escalables para empresas que buscan liderar su sector.</p>
            </div>

            <div class="grid-servicios">
                
                <div class="tarjeta-servicio" data-aos="fade-up" data-aos-delay="100">
                    <div class="icono-contenedor">
                        <i class="pi pi-code"></i>
                    </div>
                    <h3>Desarrollo a la Medida</h3>
                    <p>Deja atrás las soluciones limitadas. Diseñamos software que se adapta a tu flujo de trabajo real, automatizando procesos y potenciando la productividad de tu equipo.</p>
                </div>

                <div class="tarjeta-servicio" data-aos="fade-up" data-aos-delay="200">
                    <div class="icono-contenedor">
                        <i class="pi pi-globe"></i>
                    </div>
                    <h3>Sitios Web Modernos</h3>
                    <p>Tu marca merece una vitrina que impacte. Desarrollamos sitios web con carga ultrarrápida y SEO avanzado, gana clientes desde la primera impresión.</p>
                </div>

                <div class="tarjeta-servicio" data-aos="fade-up" data-aos-delay="300">
                    <div class="icono-contenedor">
                        <i class="pi pi-server"></i>
                    </div>
                    <h3>Infraestructura y Soporte IT</h3>
                    <p>Nos encargamos de que tu tecnología nunca se detenga. Administración de infraestructura TI y mantenimiento preventivo a equipos de computo para que tu negocio sea 100% seguro.</p>
                </div>

            </div>

            <div class="accion-central" data-aos="fade-up" data-aos-delay="400">
                <Button
                    label="Solicitar cotización personalizada" 
                    icon="pi pi-arrow-right"
                    iconPos="right"
                    size="large" 
                    class="btn-primary-nexova"
                    @click="scrollTo('contacto')" 
                />   
            </div>

        </div>
    </section>
</template>

<style scoped>
/* 1. CONTENEDOR PRINCIPAL: Fondo gris perla */
.servicios-premium {
    background-color: #f8fafc; 
    padding: 8rem 2rem;
    font-family: 'Inter', sans-serif;
}

.contenedor {
    max-width: 1200px;
    margin: 0 auto;
}

/* 2. ENCABEZADO */
.encabezado-seccion {
    text-align: center;
    max-width: 700px;
    margin: 0 auto 4rem auto;
}

.etiqueta-nexova {
    color: #0F8B58; 
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    display: inline-block;
    margin-bottom: 1rem;
    padding: 0.3rem 0.8rem;
    background-color: rgba(15, 139, 88, 0.1);
    border-radius: 20px;
}

.encabezado-seccion h2 {
    font-size: clamp(2rem, 4vw, 2.8rem);
    color: #0f172a;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1.2rem;
    letter-spacing: -0.5px;
}

.encabezado-seccion p {
    font-size: 1.15rem;
    color: #475569;
    line-height: 1.6;
}

/* 3. CUADRÍCULA (Grid) */
.grid-servicios {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Fuerza 3 columnas en PC */
    gap: 2.5rem;
    margin-bottom: 4rem;
}

/* 4. TARJETAS DE SERVICIO (Clean & Light) */
.tarjeta-servicio {
    background: #ffffff;
    border: 1px solid #f1f5f9;
    border-radius: 20px;
    padding: 3rem 2rem;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    display: flex;
    flex-direction: column;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    position: relative;
    overflow: hidden;
}

/* El efecto Hover levanta la tarjeta y añade una sombra de color */
.tarjeta-servicio:hover {
    transform: translateY(-10px);
    border-color: rgba(15, 139, 88, 0.2);
    box-shadow: 0 20px 25px -5px rgba(15, 139, 88, 0.1), 0 10px 10px -5px rgba(15, 139, 88, 0.04);
}

/* 5. ICONOS */
.icono-contenedor {
    background: linear-gradient(135deg, rgba(15, 139, 88, 0.1) 0%, rgba(52, 211, 153, 0.15) 100%);
    width: 70px;
    height: 70px;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 2rem;
    transition: all 0.3s ease;
}

.tarjeta-servicio:hover .icono-contenedor {
    background: #0F8B58;
    transform: scale(1.1) rotate(-5deg);
}

.icono-contenedor i {
    font-size: 2rem;
    color: #0F8B58; 
    transition: all 0.3s ease;
}

.tarjeta-servicio:hover .icono-contenedor i {
    color: #ffffff;
}

/* 6. TIPOGRAFÍA INTERNA */
.tarjeta-servicio h3 {
    font-size: 1.4rem;
    color: #0f172a;
    margin-bottom: 1rem;
    font-weight: 800;
}

.tarjeta-servicio p {
    color: #475569;
    line-height: 1.7;
    margin: 0;
    font-size: 1.05rem;
}

/* 7. ACCIÓN CENTRAL */
.accion-central {
    display: flex;
    justify-content: center;
    width: 100%;
}

:deep(.btn-primary-nexova) {
    background-color: #0F8B58;
    border-color: #0F8B58;
    transition: all 0.3s ease;
    padding: 1rem 2rem;
    border-radius: 8px;
    font-weight: 600;
}

:deep(.btn-primary-nexova:hover) {
    background-color: #0b6b43;
    border-color: #0b6b43;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px -6px rgba(15, 139, 88, 0.6);
}

/* 8. RESPONSIVO */
@media (max-width: 1024px) {
    .grid-servicios {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .servicios-premium {
        padding: 5rem 1.5rem;
    }
    .grid-servicios {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
    .tarjeta-servicio {
        padding: 2.5rem 1.5rem;
    }
    .encabezado-seccion {
        margin-bottom: 3rem;
    }
}
</style>