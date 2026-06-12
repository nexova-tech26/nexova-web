<script setup>
// Función para navegación suave desde el pie de página hacia cualquier sección
const navegarA = (idDestino) => {
    if (idDestino === 'top') {
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
    }
    
    const seccion = document.getElementById(idDestino);
    if (seccion) {
        seccion.scrollIntoView({ behavior: 'smooth' });
    }
};
</script>

<template>
    <footer class="footer-premium">
        <div class="linea-gradiente"></div>

        <div class="contenedor-footer">
            
            <div class="grid-footer">
                
                <div class="col-marca">
                    <div class="logo-nexova" @click="navegarA('top')">
                        <span class="letra-n">N</span>
                        <span class="texto-logo">Nexova Tech</span>
                    </div>
                    <p class="descripcion-marca">
                        Tecnología estratégica. Diseñamos soluciones digitales que impulsan y escalan tu negocio.
                    </p>
                    <div class="redes-sociales">
                        <a href="https://web.facebook.com/profile.php?id=61589231953639" target="_blank" aria-label="Facebook" class="icono-red"><i class="pi pi-facebook"></i></a>
                        <a href="https://www.instagram.com/nexova_tech/" target="_blank" aria-label="Instagram" class="icono-red"><i class="pi pi-instagram"></i></a>
                        <a href="https://wa.me/573209238674" target="_blank" aria-label="WhatsApp" class="icono-red"><i class="pi pi-whatsapp"></i></a>
                    </div>
                </div>

                <div class="col-links">
                    <h4 class="titulo-columna">Explorar</h4>
                    <nav class="nav-footer">
                        <a href="#inicio" @click.prevent="navegarA('top')" class="link-footer">
                            <i class="pi pi-angle-right"></i> Inicio
                        </a>
                        <a href="#nosotros" @click.prevent="navegarA('nosotros')" class="link-footer">
                            <i class="pi pi-angle-right"></i> Nuestro ADN
                        </a>
                        <a href="#servicios" @click.prevent="navegarA('servicios')" class="link-footer">
                            <i class="pi pi-angle-right"></i> Soluciones IT
                        </a>
                        <a href="#planes" @click.prevent="navegarA('planes')" class="link-footer">
                            <i class="pi pi-angle-right"></i> Planes de Inversión
                        </a>
                    </nav>
                </div>

                <div class="col-contacto">
                    <h4 class="titulo-columna">Contacto</h4>
                    <ul class="lista-contacto">
                        <li>
                            <i class="pi pi-envelope icono-verde"></i>
                            <a href="mailto:contacto.nexovatech@gmail.com">contacto.nexovatech@gmail.com</a>
                        </li>
                        <li>
                            <i class="pi pi-whatsapp icono-verde"></i>
                            <a href="https://wa.me/573209238674" target="_blank">+57 320 923 8674</a>
                        </li>
                        <li>
                            <i class="pi pi-map-marker icono-verde"></i>
                            <span>Villavicencio, Meta<br><small style="color: #64748b;">Colombia</small></span>
                        </li>
                    </ul>
                    
                    <button class="btn-footer-cta" @click="navegarA('contacto')">
                        Agendar Consultoría
                    </button>
                </div>

            </div>

            <div class="footer-inferior">
                <div class="copyright">
                    &copy; 2026 Nexova Tech. Todos los derechos reservados.
                </div>
                </div>

        </div>
    </footer>
</template>

<style scoped>
/* === ESTRUCTURA GLOBAL === */
.footer-premium {
    background-color: #09090b; /* Negro profundo corporativo, adiós azul */
    color: #e2e8f0;
    font-family: 'Inter', sans-serif;
    position: relative;
    padding-top: 2rem;
}

/* Línea de gradiente superior */
.linea-gradiente {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, #09090b 0%, #0F8B58 50%, #09090b 100%);
}

.contenedor-footer {
    max-width: 1200px;
    margin: 0 auto;
    padding: 4rem 1.5rem 1.5rem 1.5rem;
}

/* === CUADRÍCULA PRINCIPAL === */
.grid-footer {
    display: grid;
    grid-template-columns: 2fr 1fr 1.5fr;
    gap: 4rem;
    margin-bottom: 4rem;
}

.titulo-columna {
    color: #ffffff;
    font-size: 1.1rem;
    font-weight: 700;
    margin: 0 0 1.5rem 0;
    letter-spacing: 0.5px;
}

/* === COLUMNA 1: MARCA === */
.logo-nexova {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    cursor: pointer;
    margin-bottom: 1.5rem;
}

.letra-n {
    background-color: #0F8B58;
    color: white;
    font-weight: 900;
    font-size: 1.5rem;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(15, 139, 88, 0.3);
}

.texto-logo {
    font-size: 1.5rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.5px;
}

.descripcion-marca {
    color: #a1a1aa;
    line-height: 1.7;
    font-size: 0.95rem;
    margin-bottom: 2rem;
    max-width: 350px;
}

.redes-sociales {
    display: flex;
    gap: 1rem;
}

.icono-red {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background-color: #18181b;
    border: 1px solid #27272a;
    color: #a1a1aa;
    border-radius: 50%;
    text-decoration: none;
    transition: all 0.3s ease;
}

.icono-red:hover {
    background-color: #0F8B58;
    border-color: #0F8B58;
    color: #ffffff;
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(15, 139, 88, 0.3);
}

/* === COLUMNA 2: NAVEGACIÓN === */
.nav-footer {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.link-footer {
    color: #a1a1aa;
    text-decoration: none;
    font-size: 0.95rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
}

.link-footer i {
    font-size: 0.7rem;
    color: #0F8B58;
    transition: transform 0.3s ease;
}

.link-footer:hover {
    color: #34d399;
}

.link-footer:hover i {
    transform: translateX(5px);
}

/* === COLUMNA 3: CONTACTO === */
.lista-contacto {
    list-style: none;
    padding: 0;
    margin: 0 0 2rem 0;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
}

.lista-contacto li {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    color: #a1a1aa;
    font-size: 0.95rem;
    line-height: 1.5;
}

.lista-contacto a {
    color: #a1a1aa;
    text-decoration: none;
    transition: color 0.3s ease;
}

.lista-contacto a:hover {
    color: #ffffff;
}

.icono-verde {
    color: #34d399;
    font-size: 1.1rem;
    margin-top: 0.1rem;
}

.btn-footer-cta {
    background-color: transparent;
    color: #ffffff;
    border: 1px solid #52525b;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
}

.btn-footer-cta:hover {
    background-color: #27272a;
    border-color: #a1a1aa;
}

/* === SECCIÓN INFERIOR (COPYRIGHT) === */
.footer-inferior {
    border-top: 1px solid #27272a;
    padding-top: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.copyright {
    color: #71717a;
    font-size: 0.85rem;
}

.links-legales {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.links-legales a {
    color: #71717a;
    text-decoration: none;
    font-size: 0.85rem;
    transition: color 0.3s ease;
}

.links-legales a:hover {
    color: #e2e8f0;
}

.separador {
    color: #3f3f46;
}

/* === RESPONSIVO === */
@media (max-width: 991px) {
    .grid-footer {
        grid-template-columns: 1fr 1fr;
        gap: 3rem;
    }
    .col-marca {
        grid-column: span 2;
    }
}

@media (max-width: 600px) {
    .grid-footer {
        grid-template-columns: 1fr;
        gap: 2.5rem;
    }
    .col-marca {
        grid-column: span 1;
    }
    .footer-inferior {
        flex-direction: column;
        text-align: center;
        justify-content: center;
    }
}
</style>