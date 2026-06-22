<script setup>
// 1. IMPORTACIÓN DE COMPONENTES
// Aquí traemos nuestros bloques de Lego. Aunque aún estén vacíos, 
// Vue ya sabe que los vamos a usar en esta pantalla.
import HeroSection from '../components/home/HeroSection.vue';
import QuienesSomos from '../components/home/QuienesSomos.vue';
import ServiciosSection from '../components/home/ServiciosSection.vue';
import ClientesSection from '../components/home/ClientesSection.vue';
// import PortafolioSection from '../components/home/PortafolioSection.vue';
import ContactoSection from '../components/home/ContactoSection.vue';
import PlanesSection from '../components/home/PlanesSection.vue';
import FooterSection from '../components/home/FooterSection.vue';

</script>

<template>
    <main id="home-main" class="contenedor-principal">
        <HeroSection />
        <QuienesSomos />
        <ServiciosSection />
        <ClientesSection />
        <PlanesSection />
        <PortafolioSection />
        <ContactoSection />
        <FooterSection />
    </main>
</template>

<style scoped>
/* 'scoped' significa que este estilo SOLO afecta a este archivo */
.contenedor-principal {
    /* Ocultamos cualquier desbordamiento horizontal para evitar barras de scroll raras */
    overflow-x: hidden; 
    /* Un color de fondo global limpio, un blanco apenas grisáceo para no cansar la vista */
    background:linear-gradient(
        to bottom right,
        #0f172a 0%,
        #0c1a3a 40%,
        #0e2a45 70%,
        #0f172a 100%
    );
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}
</style>