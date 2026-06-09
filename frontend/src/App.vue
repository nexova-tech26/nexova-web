<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import Menubar from 'primevue/menubar';

const router = useRouter();
const route = useRoute();

const menuScrolled = ref(false);

const checkScroll = () => {
    menuScrolled.value = window.scrollY > 50;
};

onMounted(() => {
    window.addEventListener('scroll', checkScroll);
});

onUnmounted(() => {
    window.removeEventListener('scroll', checkScroll);
});

const items = ref([
    { label: 'Inicio', icon: 'pi pi-home', command: () => document.getElementById('home-main')?.scrollIntoView({ behavior: 'smooth' }) },
    { label: 'Nosotros', icon: 'pi pi-users', command: () => document.getElementById('nosotros')?.scrollIntoView({ behavior: 'smooth' }) },
    { label: 'Servicios', icon: 'pi pi-briefcase', command: () => document.getElementById('servicios')?.scrollIntoView({ behavior: 'smooth' }) },
    { label: 'Planes', icon: 'pi pi-box', command: () => document.getElementById('planes')?.scrollIntoView({ behavior: 'smooth' }) },
    // { label: 'Portafolio', icon: 'pi pi-desktop', command: () => document.getElementById('portafolio')?.scrollIntoView({ behavior: 'smooth' }) },
    { label: 'Contacto', icon: 'pi pi-envelope', command: () => document.getElementById('contacto')?.scrollIntoView({ behavior: 'smooth' }) },
]);
</script>

<template>
    <div :class="['header-dinamico', { 'header-scrolled': menuScrolled }]">
        <Menubar :model="items" class="menu-corporativo">
            <template #start>
                <div class="logo-container" @click="router.push('/')">
                    <img src="./assets/logo-nexova.png" alt="Nexova Tech" class="logo-img" />
                    <span class="marca-texto">Nexova Tech</span>
                </div>
            </template>
        </Menubar>
    </div>
    
    <main>
        <router-view></router-view>
    </main>
</template>

<style>
/* === COMPORTAMIENTO GLOBAL === */
html {
    scroll-behavior: smooth; 
}

body {
    background-color: #f8fafc;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    color: #1e293b;
    overflow-x: hidden;
}

/* === EL MENÚ DINÁMICO === */
.header-dinamico {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 9999;
    padding: 1.2rem 2rem;
    transition: all 0.4s ease;
    background: rgba(248, 250, 252, 0.85);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.header-scrolled {
    padding: 0.8rem 2rem;
    background: rgba(255, 255, 255, 0.98);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

/* Limpieza del componente nativo de PrimeVue */
.menu-corporativo {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 !important;
    width: 100%; /* Asegura que el menubar tome todo el espacio del contenedor */
}

/* 
   LA SOLUCIÓN: Empujar el menú hacia la derecha.
   Esto afecta tanto a la lista de enlaces en PC como al botón de hamburguesa en móvil.
*/
.menu-corporativo .p-menubar-root-list,
.menu-corporativo .p-menubar-button {
    margin-left: auto !important;
}

/* Hover de los links del menú */
.p-menubar .p-menuitem-link {
    transition: color 0.3s ease !important;
}
.p-menubar .p-menuitem-link:hover {
    color: #0F8B58 !important; 
    background: transparent !important;
}

/* === ESTILOS DEL LOGO === */
.logo-container {
    display: flex;
    align-items: center;
    gap: 0.8rem; /* Separación uniforme entre imagen y texto */
    cursor: pointer;
}

.logo-img {
    height: 40px;
    object-fit: contain;
    transition: transform 0.3s ease;
}

.marca-texto {
    font-weight: 800;
    font-size: 1.3rem;
    color: #0f172a;
    letter-spacing: -0.5px; /* Le da un toque corporativo más condensado */
}

.logo-container:hover .logo-img {
    transform: scale(1.05);
}

/* === SEPARACIÓN DEL CONTENIDO === */
.espacio-superior {
    padding-top: 7rem;
    max-width: 1200px; 
    margin: 0 auto; 
    border: none !important;
    box-shadow: none !important;
    background-color: transparent !important; 
}

/* CSS RESET */
#app, 
body, 
html, 
main, 
.contenedor-principal {
    border-left: none !important;
    border-right: none !important;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
}

#app {
    max-width: 100% !important;
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
}
</style>