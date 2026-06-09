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
        <!-- Borde superior decorativo -->
        <div class="linea-gradiente"></div>

        <div class="contenedor-footer">
            
            <!-- SECCIÓN PRINCIPAL: Cuadrícula de 3 columnas -->
            <div class="grid-footer">
                
                <!-- Columna 1: Marca y Propuesta de Valor -->
                <div class="col-marca">
                    <div class="logo-nexova" @click="navegarA('top')">
                        <span class="letra-n">N</span>
                        <span class="texto-logo">Nexova Tech</span>
                    </div>
                    <p class="descripcion-marca">
                        Tecnología que impulsa tu negocio.
                    </p>
                    <div class="redes-sociales">
                        <a href="https://web.facebook.com/profile.php?id=61589231953639" aria-label="LinkedIn" class="icono-red"><i class="pi pi-facebook"></i></a>
                        <a href="https://www.instagram.com/nexova_tech/" aria-label="GitHub" class="icono-red"><i class="pi pi-instagram"></i></a>
                        <a href="https://wa.me/573209238674" target="_blank" aria-label="Twitter" class="icono-red"><i class="pi pi-whatsapp"></i></a>
                    </div>
                </div>

                <!-- Columna 2: Navegación Rápida -->
                <div class="col-links">
                    <h4 class="titulo-columna">Explorar</h4>
                    <nav class="nav-footer">
                        <a href="#inicio" @click.prevent="navegarA('top')" class="link-footer">
                            <i class="pi pi-angle-right"></i> Inicio
                        </a>
                        <a href="#servicios" @click.prevent="navegarA('servicios')" class="link-footer">
                            <i class="pi pi-angle-right"></i> Soluciones IT
                        </a>
                        <a href="#planes" @click.prevent="navegarA('planes')" class="link-footer">
                            <i class="pi pi-angle-right"></i> Planes de Inversión
                        </a>
                    </nav>
                </div>

                <!-- Columna 3: Contacto Directo -->
                <div class="col-contacto">
                    <h4 class="titulo-columna">Contacto</h4>
                    <ul class="lista-contacto">
                        <li>
                            <i class="pi pi-envelope icono-verde"></i>
                            <a href="mailto:contacto.nexovatech@gmail.com">contacto.nexova@gmail.com</a>
                        </li>
                        <li>
                            <i class="pi pi-whatsapp icono-verde"></i>
                            <a href="https://wa.me/573209238674" target="_blank">+57 3209238674</a>
                        </li>
                        <li>
                            <i class="pi pi-map-marker icono-verde"></i>
                            <span>Colombia</span>
                        </li>
                    </ul>
                    
                    <!-- Botón de acción final -->
                    <button class="btn-footer-cta" @click="navegarA('contacto')">
                        Agendar Consultoría
                    </button>
                </div>

            </div>

            <!-- SECCIÓN INFERIOR: Copyright y Legales -->
            <div class="footer-inferior">
                <div class="copyright">
                    &copy; 2026 Nexova Tech. Todos los derechos reservados.
                </div>
                <!-- <div class="links-legales">
                    <a href="#">Términos de Servicio</a>
                    <span class="separador">•</span>
                    <a href="#">Políticas de Privacidad</a>
                </div> -->
            </div>

        </div>
    </footer>
</template>

<style scoped>
/* === ESTRUCTURA GLOBAL === */
.footer-premium {
    background-color: #020617; /* Tono ultra oscuro para máxima elegancia */
    color: #e2e8f0;
    font-family: 'Inter', sans-serif;
    position: relative;
    padding-top: 2rem;
}

/* Línea de gradiente superior para separar sutilmente de la sección anterior */
.linea-gradiente {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, #020617 0%, #0F8B58 50%, #020617 100%);
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
}

.texto-logo {
    font-size: 1.5rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.5px;
}

.descripcion-marca {
    color: #94a3b8;
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
    width: 38px;
    height: 38px;
    background-color: rgba(255, 255, 255, 0.05);
    color: #94a3b8;
    border-radius: 50%;
    text-decoration: none;
    transition: all 0.3s ease;
}

.icono-red:hover {
    background-color: #0F8B58;
    color: #ffffff;
    transform: translateY(-3px);
}

/* === COLUMNA 2: NAVEGACIÓN === */
.nav-footer {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.link-footer {
    color: #94a3b8;
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
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.5;
}

.lista-contacto a {
    color: #94a3b8;
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
    color: #34d399;
    border: 1px solid #34d399;
    padding: 0.8rem 1.5rem;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
}

.btn-footer-cta:hover {
    background-color: #34d399;
    color: #020617;
}

/* === SECCIÓN INFERIOR (COPYRIGHT) === */
.footer-inferior {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.copyright {
    color: #64748b;
    font-size: 0.85rem;
}

.links-legales {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.links-legales a {
    color: #64748b;
    text-decoration: none;
    font-size: 0.85rem;
    transition: color 0.3s ease;
}

.links-legales a:hover {
    color: #e2e8f0;
}

.separador {
    color: #334155;
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