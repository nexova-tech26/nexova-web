import { createRouter, createWebHistory } from 'vue-router';
// Importamos las dos pantallas que acabamos de crear
import HomeView from './views/HomeView.vue';
import AdminView from './views/AdminView.vue';

const routes = [
    {
        path: '/',            // Cuando el usuario visite la raíz de la página...
        name: 'home',
        component: HomeView   // ...mostramos la vista pública.
    },
    {
        path: '/admin',       // Cuando visite /admin...
        name: 'admin',
        component: AdminView  // ...mostramos tu panel CMS.
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;