<script setup>
import Button from 'primevue/button';

const scrollTo = (idDestino) => {
    const seccion = document.getElementById(idDestino);
    if (seccion) {
        seccion.scrollIntoView({ behavior: 'smooth'});
    }
};

const irAWhatsApp = (nombrePlan) => {
    const mensajeBase = `Hola equipo Nexova, estoy interesado en el plan ${nombrePlan} y me gustaría recibir más información.`;
    const mensajeCodificado = encodeURIComponent(mensajeBase);
    window.open(`https://wa.me/573209238674?text=${mensajeCodificado}`, '_blank');
};
</script>

<template>
    <section class="planes-wrapper" id="planes">
        <div class="contenedor">
            
            <div class="encabezado-seccion" data-aos="fade-up">
                <span class="etiqueta-nexova">Inversión Transparente</span>
                <h2>Deja de ser invisible.<br>Empieza a ser elegido.</h2>
                <p>Elige el plan que se adapte a tu etapa de crecimiento.</p>
            </div>

            <div class="grid-planes">
                
                <!-- PLAN 1: NEX - START (Tarjeta Oscura) -->
                <div class="plan-card oscura" data-aos="fade-up" data-aos-delay="100">
                    <div class="plan-header">
                        <h3 class="plan-name">Nex - Start</h3>
                        <p class="plan-desc">Tu negocio merece estar en internet desde hoy. Sin complicaciones y con resultados reales.</p>
                        
                        <span class="desde-texto">Inversión desde</span>
                        <div class="precio-caja">
                            <span class="moneda">COP</span>
                            <span class="precio">$500.000</span>
                        </div>
                        <span class="nota-descuento">Descuento de lanzamiento disponible*</span>
                    </div>
            
                    <div class="plan-info">
                        <div class="info-item">
                            <i class="pi pi-bolt"></i>
                            <span>Entrega express: 1-2 semanas</span>
                        </div>
                        <div class="info-item">
                            <i class="pi pi-home"></i>
                            <span>Para emprendedores y Pymes</span>
                        </div>
                    </div>

                    <ul class="lista-features">
                        <li><i class="pi pi-check"></i> Hasta 5 páginas</li>
                        <li><i class="pi pi-check"></i> Se ve perfecto en Smartphone y Pc</li>
                        <li><i class="pi pi-check"></i> Optimización básica para Google (SEO)</li>
                        <li><i class="pi pi-check"></i> Conexión directa con WhatsApp</li>
                        <li><i class="pi pi-check"></i> 1 mes de soporte directo</li>
                        <li><i class="pi pi-check"></i> Garantía técnica de 1 año</li>
                    </ul>

                    <Button label="Elegir Nex - Start" 
                        class="btn-plan btn-outline-dark w-full mt-auto"
                        @click="irAWhatsApp('Nex - Start')"
                    />
                </div>

                <!-- PLAN 2: NEX - PRO (Tarjeta Blanca Destacada) -->
                <div class="plan-card destacado" data-aos="fade-up" data-aos-delay="200">
                    <div class="badge-popular">MÁS ELEGIDO</div>
                    
                    <div class="plan-header">
                        <h3 class="plan-name text-verde-oscuro">Nex - Pro</h3>
                        <p class="plan-desc texto-oscuro">Para negocios que quieren una presencia digital que los diferencie de su competencia local.</p>
                        
                        <span class="desde-texto texto-gris">Inversión desde</span>
                        <div class="precio-caja">
                            <span class="moneda texto-gris">COP</span>
                            <span class="precio text-verde">$1'300.000</span>
                        </div>
                        <span class="nota-descuento text-verde-oscuro">Consulta nuestras facilidades de pago*</span>
                    </div>

                    <div class="plan-info">
                        <div class="info-item">
                            <i class="pi pi-clock text-verde"></i>
                            <span class="texto-oscuro">Entrega: 3-6 semanas</span>
                        </div>
                        <div class="info-item">
                            <i class="pi pi-building text-verde"></i>
                            <span class="texto-oscuro">Para Startups y empresas establecidas</span>
                        </div>
                    </div>

                    <ul class="lista-features">
                        <li><i class="pi pi-check-circle text-verde"></i> <span class="texto-oscuro"><strong>Hasta 15 páginas</strong> estratégicas</span></li>
                        <li><i class="pi pi-check-circle text-verde"></i> <span class="texto-oscuro">Diseño UX/UI totalmente personalizado</span></li>
                        <li><i class="pi pi-check-circle text-verde"></i> <span class="texto-oscuro">Animaciones e interacciones premium</span></li>
                        <li><i class="pi pi-check-circle text-verde"></i> <span class="texto-oscuro">SEO Avanzado y Google Analytics</span></li>
                        <li><i class="pi pi-check-circle text-verde"></i> <span class="texto-oscuro">Panel autoadministrable (Edita tú mismo el contenido)</span></li>
                        <li><i class="pi pi-check-circle text-verde"></i> <span class="texto-oscuro"><strong>3 meses</strong> de soporte post-entrega</span></li>
                    </ul>

                    <Button label="Elegir Nex - Pro" 
                        class="btn-plan btn-primary-nexova w-full mt-auto"
                        @click="irAWhatsApp('Nex - Pro')"
                    />
                </div>

                <!-- PLAN 3: NEX - BUSINESS (Tarjeta Oscura) -->
                <div class="plan-card oscura" data-aos="fade-up" data-aos-delay="300">
                    <div class="plan-header">
                        <h3 class="plan-name">Nex - Business</h3>
                        <p class="plan-desc">Cuando tu negocio necesita tecnología a medida y automatización de procesos internos.</p>
                        
                        <span class="desde-texto">Inversión</span>
                        <div class="precio-caja" style="margin-top: 0.5rem;">
                            <span class="precio" style="font-size: 1.6rem;">A tu medida</span>
                        </div>
                        <span class="nota-descuento transparent-text">Consulta nuestras facilidades de pago*</span>
                    </div>

                    <div class="plan-info">
                        <div class="info-item">
                            <i class="pi pi-calendar-plus"></i>
                            <span>Entrega: Según alcance</span>
                        </div>
                        <div class="info-item">
                            <i class="pi pi-code"></i>
                            <span>Ingeniería exclusiva corporativa</span>
                        </div>
                    </div>

                    <ul class="lista-features">
                        <li><i class="pi pi-check"></i> Soluciones 100% personalizadas</li>
                        <li><i class="pi pi-check"></i> Automatización de procesos manuales</li>
                        <li><i class="pi pi-check"></i> Bases de datos y portales de usuarios</li>
                        <li><i class="pi pi-check"></i> Arquitectura en la nube escalable</li>
                        <li><i class="pi pi-check"></i> Propiedad intelectual total del código</li>
                        <li><i class="pi pi-check"></i> Acompañamiento continuo a largo plazo</li>
                    </ul>

                    <Button label="Agendar consultoría" 
                        class="btn-plan btn-outline-dark w-full mt-auto" 
                        @click="scrollTo('contacto')"
                    />
                </div>

            </div>
        </div>
    </section>
</template>

<style scoped>
/* 1. SECCIÓN PRINCIPAL: Premium Dark */
.planes-wrapper {
    background-color: #09090b; /* Un negro/zinc muy sofisticado, adiós azul */
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
    color: #34d399; /* Verde más vibrante para fondos oscuros */
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
    color: #a1a1aa; /* Gris claro */
    line-height: 1.6;
}

/* 3. GRID DE PLANES */
.grid-planes {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    align-items: stretch; 
}

/* 4. TARJETAS BASE */
.plan-card {
    border-radius: 24px;
    padding: 2.5rem 2rem;
    display: flex;
    flex-direction: column;
    position: relative;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.plan-card:hover {
    transform: translateY(-8px);
}

/* TARJETAS OSCURAS (Start y Business) */
.oscura {
    background-color: #18181b;
    border: 1px solid #27272a;
    color: #ffffff;
}

.oscura:hover {
    border-color: #3f3f46;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

.oscura .plan-name { color: #ffffff; }
.oscura .plan-desc { color: #a1a1aa; }
.oscura .desde-texto, .oscura .moneda { color: #71717a; }
.oscura .precio { color: #ffffff; }
.oscura .nota-descuento { color: #34d399; font-size: 0.85rem; }
.oscura .info-item i { color: #34d399; }
.oscura .info-item span { color: #d4d4d8; }
.oscura .lista-features i { color: #0F8B58; }
.oscura .lista-features li { color: #d4d4d8; }

/* TARJETA DESTACADA (Pro - Blanca) */
.destacado {
    background-color: #ffffff;
    border: 2px solid #0F8B58;
    box-shadow: 0 0 40px rgba(15, 139, 88, 0.15); /* Resplandor verde corporativo */
    transform: scale(1.03); /* Ligeramente más grande que las otras */
    z-index: 2;
}

.destacado:hover {
    transform: scale(1.05) translateY(-8px);
    box-shadow: 0 20px 50px rgba(15, 139, 88, 0.25);
}

.badge-popular {
    position: absolute;
    top: -16px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, #0F8B58 0%, #0b6b43 100%);
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 30px;
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 1px;
    box-shadow: 0 4px 10px rgba(15, 139, 88, 0.3);
}

/* Colores utilitarios para la tarjeta clara */
.texto-oscuro { color: #1e293b !important; }
.texto-gris { color: #64748b !important; }
.text-verde { color: #0F8B58 !important; }
.text-verde-oscuro { color: #0b6b43 !important; }
.transparent-text { color: transparent; user-select: none; } /* Oculta el texto pero mantiene el espacio */

/* 5. ESTRUCTURA INTERNA */
.plan-header {
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid rgba(161, 161, 170, 0.2);
}

.plan-name {
    font-size: 1.6rem;
    margin: 0 0 0.8rem 0;
    font-weight: 800;
}

.plan-desc {
    font-size: 0.95rem;
    line-height: 1.5;
    margin: 0 0 1.5rem 0;
    min-height: 42px; 
}

.desde-texto {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
    display: block;
    margin-bottom: 0.3rem;
}

.precio-caja {
    display: flex;
    align-items: baseline;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
}

.moneda { font-size: 1.2rem; font-weight: 700; }
.precio { font-size: 2.2rem; font-weight: 900; letter-spacing: -1px; }

/* 6. LISTAS E INFO */
.plan-info {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 2rem;
}

.info-item {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
}

.info-item i { font-size: 1.2rem; margin-top: 0.1rem; }
.info-item span { font-size: 0.95rem; font-weight: 500; }

.lista-features {
    list-style: none;
    padding: 0;
    margin: 0 0 2.5rem 0;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
}

.lista-features li {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    font-size: 0.95rem;
    line-height: 1.4;
}

.lista-features i { font-size: 1.1rem; margin-top: 0.1rem; }

/* 7. BOTONES */
.w-full { width: 100%; }
.mt-auto { margin-top: auto; } /* Empuja el botón siempre al fondo, alineándolos todos */

:deep(.btn-plan) {
    padding: 1.2rem;
    font-weight: 700;
    border-radius: 12px;
    font-size: 1rem;
    justify-content: center;
}

:deep(.btn-primary-nexova) {
    background-color: #0F8B58;
    border-color: #0F8B58;
    color: white;
    transition: all 0.3s ease;
}

:deep(.btn-primary-nexova:hover) {
    background-color: #0b6b43;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(15, 139, 88, 0.4);
}

:deep(.btn-outline-dark) {
    background-color: transparent;
    border: 1px solid #52525b;
    color: #ffffff;
    transition: all 0.3s ease;
}

:deep(.btn-outline-dark:hover) {
    background-color: #27272a;
    border-color: #a1a1aa;
}

/* 8. RESPONSIVO */
@media (max-width: 1024px) {
    .destacado {
        transform: scale(1); /* Quitamos el scale en tablets/móviles */
    }
    .destacado:hover {
        transform: translateY(-5px);
    }
}

@media (max-width: 768px) {
    .planes-wrapper {
        padding: 5rem 1.5rem;
    }
    .encabezado-seccion h2 {
        font-size: 2.2rem;
    }
}
</style>