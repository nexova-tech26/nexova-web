import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';
import { definePreset } from '@primevue/themes';
import 'primeicons/primeicons.css';
import './style.css';

// NUEVO: Importamos las animaciones ligeras
import AOS from 'aos';
import 'aos/dist/aos.css';

const NexovaPreset = definePreset(Aura, {
    semantic: {
        primary: {
            50: '#ecfdf5', 100: '#d1fae5', 200: '#a7f3d0', 300: '#6ee7b7', 400: '#34d399',
            500: '#0F8B58', 600: '#059669', 700: '#047857', 800: '#065f46', 900: '#064e3b', 950: '#022c22'
        }
    }
});

const app = createApp(App);

app.use(PrimeVue, {
    theme: { preset: NexovaPreset, options: { darkModeSelector: 'none' } }
});

app.use(router);

// NUEVO: Inicializamos AOS antes de montar la app
app.mixin({
    mounted() {
        AOS.init({
            duration: 800, // Duración de la animación en ms (muy suave)
            once: true,    // Solo se anima una vez al bajar, no marea al usuario
            offset: 50     // Activa la animación 50px antes de ver el elemento
        });
    }
});

app.mount('#app');