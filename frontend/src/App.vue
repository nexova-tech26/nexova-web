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

// Lógica para el clic en el Logo
const handleLogoClick = () => {
    if (route.path === '/') {
        // Si ya está en el inicio, simplemente lo sube suavemente
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        // Si está en otra página, lo envía al inicio y luego lo sube
        router.push('/').then(() => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
};

// Lógica de navegación robusta para los enlaces del menú
const scrollToSection = (id) => {
    if (route.path !== '/') {
        router.push('/').then(() => {
            setTimeout(() => document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' }), 100);
        });
    } else {
        document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
    }
};

const items = ref([
    { label: 'Inicio', icon: 'pi pi-home', command: () => scrollToSection('home-main') },
    { label: 'Nosotros', icon: 'pi pi-users', command: () => scrollToSection('nosotros') },
    { label: 'Servicios', icon: 'pi pi-briefcase', command: () => scrollToSection('servicios') },
    { label: 'Planes', icon: 'pi pi-box', command: () => scrollToSection('planes') },
    { label: 'Contacto', icon: 'pi pi-envelope', command: () => scrollToSection('contacto') },
    // { label: 'Portafolio', icon: 'pi pi-envelope', command: () => scrollToSection('portafolio') },
]);
</script>

<template>
    <header :class="['header-dinamico', { 'header-scrolled': menuScrolled }]">
        <Menubar :model="items" class="menu-corporativo">
            <template #start>
                <!-- Aquí aplicamos la nueva función al hacer clic -->
                <div class="logo-container" @click="handleLogoClick">
                    <img src="./assets/logo-nexova.png" alt="Nexova Tech" class="logo-img" />
                    <span class="marca-texto">Nexova Tech</span>
                </div>
            </template>
        </Menubar>
    </header>
    
    <main class="contenedor-principal">
        <router-view></router-view>
    </main>
</template>

<style>
/* === RESET Y COMPORTAMIENTO GLOBAL CRÍTICO === */
*, *::before, *::after {
    box-sizing: border-box; 
}

html {
    scroll-behavior: smooth; 
}

body {
    background-color: #f8fafc;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    padding: 0;
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
    width: 100%;
}

.menu-corporativo .p-menubar-root-list,
.menu-corporativo .p-menubar-button {
    margin-left: auto !important;
}

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
    gap: 0.8rem;
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
    letter-spacing: -0.5px;
}

.logo-container:hover .logo-img {
    transform: scale(1.05);
}

/* === RESPONSIVIDAD DEL HEADER === */
@media (max-width: 768px) {
    .header-dinamico {
        padding: 0.8rem 1rem;
    }
    .header-scrolled {
        padding: 0.6rem 1rem;
    }
    .logo-img {
        height: 32px;
    }
    .marca-texto {
        font-size: 1.1rem;
    }
}

/* CSS RESET ADICIONAL */
#app, 
main, 
.contenedor-principal {
    max-width: 100% !important;
    width: 100% !important;
    padding: 0;
    margin: 0;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
}
</style>