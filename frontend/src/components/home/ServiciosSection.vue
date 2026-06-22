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
    <section class="servicios-editorial" id="servicios">
        <div class="contenedor">
            
            <div class="encabezado-seccion" data-aos="fade-up">
                <span class="etiqueta-nexova">Nuestros Servicios</span>
                <h2>Tu visión es grande.<br>Tu tecnología debe estar a la altura.</h2>
                <p>Soluciones digitales escalables para empresas que buscan liderar su sector.</p>
            </div>

            <div class="grid-editorial">
                
                <article class="pilar-servicio" data-aos="fade-up" data-aos-delay="100">
                    <div class="pilar-visual">
                        <span class="indice-enorme">01</span>
                        <div class="arte-css-dev">
                            <span class="line-code w-70"></span>
                            <span class="line-code w-100"></span>
                            <span class="line-code w-40 active"></span>
                        </div>
                    </div>
                    <div class="pilar-contenido">
                        <h3>Desarrollo a la Medida</h3>
                        <p>Deja atrás las soluciones limitadas. Diseñamos software que se adapta a tu flujo de trabajo real, automatizando procesos y potenciando la productividad de tu equipo.</p>
                    </div>
                </article>

                <article class="pilar-servicio offset-pilar" data-aos="fade-up" data-aos-delay="200">
                    <div class="pilar-visual">
                        <span class="indice-enorme">02</span>
                        <div class="arte-css-web">
                            <div class="orbital-ring"></div>
                            <div class="core-dot"></div>
                        </div>
                    </div>
                    <div class="pilar-contenido">
                        <h3>Sitios Web Modernos</h3>
                        <p>Tu marca merece una vitrina que impacte. Desarrollamos tu página web con carga ultrarrápida y SEO avanzado. Gana clientes desde la primera impresión.</p>
                    </div>
                </article>

                <article class="pilar-servicio" data-aos="fade-up" data-aos-delay="300">
                    <div class="pilar-visual">
                        <span class="indice-enorme">03</span>
                        <div class="arte-css-it">
                            <span class="node n1"></span>
                            <span class="node n2"></span>
                            <span class="node n3"></span>
                            <div class="pulse-line"></div>
                        </div>
                    </div>
                    <div class="pilar-contenido">
                        <h3>Soporte Técnico</h3>
                        <p>Nos encargamos de que tu operación nunca se detenga. Realizamos mantenimiento preventivo a equipos de cómputo e infraestructura TI</p>
                    </div>
                </article>

            </div>

            <div class="accion-central" data-aos="fade-up" data-aos-delay="400">
                <Button
                    label="Hablemos de tu próximo desafío" 
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
/* ==========================================================================
   ENFOQUE ESTRICTO MOBILE FIRST (Estilos por defecto para pantallas pequeñas)
   ========================================================================== */
.servicios-editorial {
    background-color: #ffffff; /* Blanco puro para un look de revista de diseño */
    padding: 5rem 1.5rem;
    font-family: 'Inter', sans-serif;
    color: #0f172a;
}

.contenedor {
    max-width: 1200px;
    margin: 0 auto;
}

/* --- ENCABEZADO --- */
.encabezado-seccion {
    text-align: left; /* Alineación izquierda en móvil proyecta más modernidad */
    margin-bottom: 4rem;
}

.etiqueta-nexova {
    color: #0F8B58;
    font-weight: 700;
    font-size: 1.2rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    display: inline-block;
    margin-bottom: 1rem;
    padding: 0.3rem 0.8rem;
    background-color: rgba(15, 139, 88, 0.1);
    border-radius: 10px;
}

.encabezado-seccion h2 {
    font-size: clamp(2.2rem, 8vw, 3.2rem);
    font-weight: 900;
    line-height: 1.1;
    margin: 0 0 1rem 0;
    letter-spacing: -1px;
    color: #000000;

}

.encabezado-seccion p {
    font-size: 1.1rem;
    color: #000000;
    line-height: 1.6;
    margin: 0;
}

/* --- GRID EDITORIAL MÓVIL (Apilado vertical limpio) --- */
.grid-editorial {
    display: flex;
    flex-direction: column;
    gap: 3.5rem;
    margin-bottom: 4rem;
}

.pilar-servicio {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding-bottom: 3.5rem;
    border-bottom: 1px solid #e2e8f0; /* Divisor fino y elegante */
    transition: transform 0.3s ease;
}

.pilar-servicio:last-child {
    border-bottom: none;
    padding-bottom: 0;
}

.pilar-visual {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
}

.indice-enorme {
    font-size: 3.5rem;
    font-weight: 900;
    color: #0F8B58;
    line-height: 0.8;
    letter-spacing: -2px;
}

.pilar-contenido h3 {
    font-size: 1.6rem;
    font-weight: 800;
    margin: 0 0 1rem 0;
    letter-spacing: -0.5px;
}

.pilar-contenido p {
    color: #475569;
    line-height: 1.7;
    margin: 0;
    font-size: 1.05rem;
}

/* ==========================================================================
   ARTE ABSTRACTO EN CSS PURO (Animaciones de alto rendimiento)
   ========================================================================== */

/* 01. Arte Dev: Líneas de código compilando */
.arte-css-dev {
    width: 60px; height: 40px;
    display: flex; flex-direction: column;
    justify-content: space-around;
}
.line-code {
    height: 4px; background-color: #cbd5e1;
    border-radius: 4px; transition: width 0.3s ease;
}
.w-70 { width: 70%; } .w-100 { width: 100%; } .w-40 { width: 40%; }
.active { background-color: #0F8B58; animation: typing 2s infinite ease-in-out; }

@keyframes typing {
    0% { width: 20%; } 50% { width: 90%; } 100% { width: 20%; }
}

/* 02. Arte Web: Anillo orbital ultrarrápido */
.arte-css-web {
    width: 50px; height: 50px;
    position: relative; display: flex;
    align-items: center; justify-content: center;
}
.orbital-ring {
    position: absolute; width: 100%; height: 100%;
    border: 2px dashed #cbd5e1; border-radius: 50%;
    animation: spin-orbit 8s linear infinite;
}
.core-dot {
    width: 14px; height: 14px;
    background-color: #0F8B58; border-radius: 50%;
    box-shadow: 0 0 15px rgba(15, 139, 88, 0.6);
    animation: pulse-core 2s infinite ease-in-out;
}

@keyframes spin-orbit { 100% { transform: rotate(360deg); } }
@keyframes pulse-core { 50% { transform: scale(1.3); } }

/* 03. Arte IT: Nodos de red interconectados */
.arte-css-it {
    width: 55px; height: 45px; position: relative;
}
.node {
    position: absolute; width: 10px; height: 10px;
    background-color: #0F8B58; border-radius: 50%;
}
.n1 { top: 0; left: 0; animation: blink 1.5s infinite; }
.n2 { bottom: 0; left: 40%; animation: blink 1.5s infinite 0.4s; }
.n3 { top: 10px; right: 0; animation: blink 1.5s infinite 0.8s; }
.pulse-line {
    position: absolute; top: 15px; left: 5px;
    width: 45px; height: 2px; background-color: rgba(15, 139, 88, 0.3);
    transform: rotate(15deg);
}

@keyframes blink { 50% { opacity: 0.2; transform: scale(0.8); } }

/* --- ACCIÓN CENTRAL --- */
.accion-central {
    display: flex;
    justify-content: flex-start; /* Consistente con el encabezado izquierdo en móvil */
}

:deep(.btn-primary-nexova) {
    background-color: #0F8B58;
    border-color: #0F8B58;
    color: white;
    font-weight: 700;
    padding: 1.2rem 2.5rem;
    border-radius: 12px;
    transition: all 0.3s ease;
    width: 100%;
    justify-content: center;
}

:deep(.btn-primary-nexova:hover) {
    background-color: #0b6b43;
    transform: translateY(-3px);
    box-shadow: 0 10px 25px -5px rgba(15, 139, 88, 0.4);
}

/* ==========================================================================
   ESCALADO A ESCRITORIO (Desktop Override)
   ========================================================================== */
@media (min-width: 768px) {
    .servicios-editorial {
        padding: 9rem 2rem;
    }
    
    .encabezado-seccion {
        text-align: center;
        max-width: 750px;
        margin: 0 auto 6rem auto;
    }
    
    .grid-editorial {
        flex-direction: row;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 3.5rem;
        border: none;
    }
    
    .pilar-servicio {
        border-bottom: none;
        padding: 2.5rem;
        background-color: #f8fafc; /* Fondo sutil para enmarcar en PC */
        border-radius: 24px;
        border: 1px solid #f1f5f9;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        justify-content: flex-start;
    }
    
    /* El pilar central flota más arriba para romper la monotonía de la cuadrícula */
    .offset-pilar {
        transform: translateY(-25px);
        background-color: #ffffff;
        box-shadow: 0 20px 40px -15px rgba(0,0,0,0.07);
        border-color: #e2e8f0;
    }
    
    .pilar-servicio:hover {
        transform: translateY(-10px);
        background-color: #ffffff;
        box-shadow: 0 25px 50px -12px rgba(15, 139, 88, 0.15);
        border-color: rgba(15, 139, 88, 0.3);
    }
    
    .offset-pilar:hover {
        transform: translateY(-35px);
    }

    .accion-central {
        justify-content: center;
    }
    
    :deep(.btn-primary-nexova) {
        width: auto;
    }
}
</style>