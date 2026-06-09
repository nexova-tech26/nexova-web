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
                <h2>Deja de ser invisible y empieza a ser elegido.</h2>
                <p>Desarrollamos tu sitio web. Contamos con diferentes alternativas para tu negocio.</p>
            </div>

            <div class="grid-planes">
                
                <div class="plan-card" data-aos="fade-up" data-aos-delay="100">
                    <div class="plan-header">
                        <h3 id="plan-name"><strong>Nex - Start</strong></h3>
                        <p class="plan-desc">Tu negocio merece estar en internet desde hoy. Sin complicaciones, sin esperas, con resultados reales desde la primera semana.</p>
                        <p>Desde</p>
                        <div class="precio-caja">
                            <span class="moneda">COP</span>
                            <span class="precio">$500.000</span>
                        </div>
                        <span style="color:darkgreen ; font-size: small;">Descuento de lanzamiento disponible*</span>
                    </div>
            
                    <div class="plan-info">
                        <div class="info-item">
                            <i class="pi pi-bolt"></i>
                            <span>Entrega: 1-2 semanas</span>
                        </div>
                        <div class="info-item">
                            <i class="pi pi-home"></i>
                            <span>Para emprendedores y Pymes</span>
                        </div>
                    </div>

                    <ul class="lista-features">
                        <li><i class="pi pi-check"></i>Hasta 5 páginas</li>
                        <li><i class="pi pi-check"></i>Se ve perfecto en celular y computador</li>
                        <li><i class="pi pi-check"></i>Optimizado para aparecer en Google</li>
                        <li><i class="pi pi-check"></i>Carga rápida, sin esperas que aburren</li>
                        <li><i class="pi pi-check"></i>1 mes de soporte directo post-entrega</li>
                        <li><i class="pi pi-check"></i>Integración con WhatsApp</li>
                        <li><i class="pi pi-check"></i>Garantía en línea por 1 año</li>
                    </ul>

                    <Button label="Empezar proyecto" 
                        outlined 
                        class="btn-plan w-full"
                        @click="irAWhatsApp ('Nex - Start')"
                        />
                </div>

                <div class="plan-card destacado" data-aos="fade-up" data-aos-delay="200">
                    <div class="badge-popular">RECOMENDADO</div>
                    
                    <div class="plan-header">
                        <h3 id="plan-name"><strong>Nex - Pro</strong></h3>
                        <p class="plan-desc">Para negocios que quieren una presencia digital que diferencie, que trabaje para ellos.</p>
                        <span>Desde</span>

                        <div class="precio-caja">
                            <span class="moneda">COP</span>
                            <span class="precio text-verde">$1'300.000</span>
                        </div>
                        <span style="color:darkgreen ; font-size: small;">Consulta por nuestras facilidades de pago*</span>
                    </div>

                    <div class="plan-info">
                        <div class="info-item">
                            <i class="pi pi-clock"></i>
                            <span>Entrega: 3-6 semanas</span>
                        </div>
                        <div class="info-item">
                            <i class="pi pi-building"></i>
                            <span>Para Startups y empresas en crecimiento</span>
                        </div>
                    </div>

                    <ul class="lista-features">
                        <li><i class="pi pi-check text-verde"></i> Hasta 15 páginas, lo que tu marca necesite</li>
                        <li><i class="pi pi-check text-verde"></i> Diseño personalizado que nadie más tiene</li>
                        <li><i class="pi pi-check text-verde"></i> Animaciones e interacciones</li>
                        <li><i class="pi pi-check text-verde"></i> SEO avanzado, más visibilidad en Google</li>
                        <li><i class="pi pi-check text-verde"></i> Panel para editar tu contenido tú mismo</li>
                        <li><i class="pi pi-check text-verde"></i> 3 meses de soporte post-entrega</li>
                        <li><i class="pi pi-check text-verde"></i> Garantía en línea por 1 año</li>
                        <li><i class="pi pi-check text-verde"></i> Integración con WhatsApp y redes sociales</li>
                    </ul>

                    <Button label="Elegir Nex - Pro" 
                        class="btn-plan w-full"
                        @click="irAWhatsApp ('Nex - Pro')"
                         />
                </div>

                <div class="plan-card" data-aos="fade-up" data-aos-delay="300">
                    <div class="plan-header">
                        <h3 id="plan-name"><strong>Nex - Business</strong></h3>
                        <p class="plan-desc">Cuando tu negocio necesita más que una web, necesita tecnología que se adapte a tu flujo de trabajo.</p>
                        <div class="precio-caja">
                            <span class="precio">Inversión a tu medida</span>
                        </div>
                    </div>

                    <div class="plan-info">
                        <div class="info-item">
                            <i class="pi pi-clock"></i>
                            <span>Entrega: Desde 4 semanas</span>
                        </div>
                        <div class="info-item">
                            <i class="pi pi-objects-column"></i>
                            <span>Ingeniería exclusiva para tu negocio</span>
                        </div>
                    </div>

                    <ul class="lista-features">
                        <li><i class="pi pi-check"></i> Soluciones sin límites de alcance ni función</li>
                        <li><i class="pi pi-check"></i> Automatización de procesos que hoy haces a mano</li>
                        <li><i class="pi pi-check"></i> Portales y accesos exclusivos por usuario</li>
                        <li><i class="pi pi-check"></i> Arquitectura escalable desde el inicio</li>
                        <li><i class="pi pi-check"></i> Acompañamiento continuo post-lanzamiento.</li>
                        <li><i class="pi pi-check"></i> Sesión de estrategia gratuita antes de cotizar</li>
                        <li><i class="pi pi-check"></i> Propiedad total del código. Es tuyo para siempre</li>
                    </ul>

                    <Button label="Agendar llamada" 
                        outlined 
                        class="btn-plan w-full" 
                        style="margin-top: auto;"
                        @click="scrollTo('contacto')"
                         />
                </div>

            </div>
        </div>
    </section>
</template>

<style scoped>
/* ==========================================================================
   VARIABLES DE TEMA (Preparación para Modo Claro / Oscuro)
   ========================================================================== */
.planes-wrapper {
    /* Variables por defecto (Modo Claro) */
    --bg-section: linear-gradient(
        to bottom right,
        #0f172a 0%,
        #0c1a3a 40%,
        #0e2a45 70%,
        #0f172a 100%
    );
    --card-bg: #ffffff;
    --card-border: #e2e8f0;
    --card-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);
    
    --text-main: #ffffff;
    --text-main-card: #0f172a;

    --text-muted: #64748b;
    --text-light: #94a3b8;
    
    --divider-color: #f1f5f9;
    
    /* Variables de Tarjeta Destacada */
    --highlight-bg: #f8fafc; /* Un gris/menta hiper sutil */
    --highlight-border: #BCE4D3; /* Tu Verde Menta */
    --highlight-badge: #0F8B58; /* Tu Verde Nexova */
    
    background-color: var(--bg-section);
    padding: 6rem 1.5rem;
    font-family: 'Inter', sans-serif;
}

/* NOTA: Cuando activemos el modo oscuro globalmente, 
   solo añadiremos una clase que reemplace estas variables por colores oscuros,
   y las tarjetas cambiarán solas sin tocar el resto del CSS.
*/

.contenedor {
    max-width: 1200px;
    margin: 0 auto;
}

/* === ENCABEZADO === */
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
    display: block;
    margin-bottom: 1rem;
}

.encabezado-seccion h2 {
    font-size: 2.5rem;
    color: var(--text-main);
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1rem;
}

.encabezado-seccion p {
    font-size: 1.1rem;
    color: var(--text-muted);
}

/* === CUADRÍCULA DE PLANES === */
.grid-planes {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    align-items: stretch; /* Asegura que todas las tarjetas midan lo mismo */
}

/* === TARJETA BASE === */
.plan-card {
    background-color: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 24px;
    padding: 2.0rem 1.5rem;
    display: flex;
    flex-direction: column;
    position: relative;
    box-shadow: var(--card-shadow);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.plan-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.1);
}

/* === TARJETA DESTACADA (POPULAR) === */
.destacado {
    position: relative;
    overflow: visible !important; /* Mantiene la etiqueta visible */
    z-index: 10;
    
    /* Estilos base de platino */
    background: linear-gradient(165deg, #ffffff 0%, #f1f5f9 40%, #ecfdf5 100%);
    border-radius: 24px;
    border: 4px solid transparent;
    background-clip: padding-box, border-box;
    background-origin: padding-box, border-box;
    background-image: 
        linear-gradient(to bottom, #ffffff, #f1f5f9), 
        linear-gradient(135deg, #10b981, #ffffff, #059669);
    
    box-shadow: 0 25px 50px -12px rgba(16, 185, 129, 0.25);
    transition: all 0.4s ease;
}

/* EL TRUCO: El brillo ahora es interno y no se sale */
.destacado::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 20px; /* Un poco menos que el padre por el grosor del borde */
     
    /* Gradiente de brillo con tamaño extra para animar el fondo, no el elemento */
    background: linear-gradient(
        120deg, 
        transparent 30%, 
        rgba(255, 255, 255, 0.6) 50%, 
        transparent 70%
    );
    background-size: 300% 100%; /* Hacemos el gradiente más ancho que la tarjeta */
    background-position: 150% 0;
    
    animation: shine-ultra 4s infinite;
    z-index: 1;
    pointer-events: none;
    clip-path: inset(0 round 20px); /* Doble seguridad para el recorte */
}

@keyframes shine-ultra {
    0% { background-position: 150% 0; }
    30% { background-position: -150% 0; }
    100% { background-position: -150% 0; }
}

.destacado:hover {
    transform: scale(1.05) translateY(-10px);
}

.badge-popular {
    position: absolute;
    top: -14px;
    left: 50%;
    transform: translateX(-50%);
    background-color: var(--highlight-badge);
    color: white;
    padding: 0.4rem 1.2rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 1px;
}

/* === CABECERA DEL PLAN === */
.plan-header {
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--divider-color);
}

.plan-header h3 {
    font-size: 1.5rem;
    color: var(--text-main-card);
    margin: 0 0 0.5rem 0;
    font-weight: 700;
}

.plan-desc {
    color: var(--text-muted);
    font-size: 0.95rem;
    margin: 0 0 1.5rem 0;
    min-height: 45px; /* Alinea los precios si las descripciones tienen distinto largo */
}

.precio-caja {
    display: flex;
    align-items: justify;
    gap: 2rem;
}

.moneda {
    font-size: 1rem;
    color: var(--text-light);
    font-weight: 600;
}

.precio {
    font-size: 1.9rem;
    font-weight: 800;
    color: var(--text-main-card);
}
.text-verde {
    color: #0F8B58 !important;
}

.desde {
    font-size: 0.9rem;
    color: var(--text-light);
}

/* === INFO DE ENTREGA Y PÚBLICO === */
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

.info-item i {
    color: var(--text-light);
    font-size: 1.1rem;
    margin-top: 0.2rem;
}

.info-item span {
    color: var(--text-muted);
    font-size: 0.9rem;
    line-height: 1.5;
}

/* === LISTA DE CARACTERÍSTICAS === */
.lista-features {
    list-style: none;
    padding: 0;
    margin: 0 0 2.5rem 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    flex-grow: 1; /* Empuja el botón hacia el fondo */
}

.lista-features li {
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
    color: var(--text-main-card);
    font-size: 0.95rem;
    line-height: 1.4;
}

.lista-features i {
    color: #34d399; /* Chulito (Check) genérico */
    font-size: 1rem;
    margin-top: 0.2rem;
}

/* === BOTONES === */
.w-full {
    width: 100%;
}

.btn-plan {
    padding: 1rem;
    font-weight: 700;
    border-radius: 12px;
}

/* Responsivo para Tablets/Móviles */
@media (max-width: 991px) {
    .destacado {
        transform: scale(1); /* Quitamos el scale en pantallas pequeñas para que no se desborde */
    }
    .destacado:hover {
        transform: translateY(-5px);
    }
    .encabezado-seccion h2 { font-size: 2.2rem; }
}
</style>