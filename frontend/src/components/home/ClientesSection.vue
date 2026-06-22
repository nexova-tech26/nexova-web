<script setup>
import { ref } from 'vue';

/* 
  REGLA DE CARPETAS EN VITE: 
  Guarda tus imágenes dentro de la carpeta: public/img/clientes/
  Si guardas un archivo llamado "pepsi.png" ahí, la ruta aquí debe ser exactamente: '/img/clientes/pepsi.png'
*/
const clientes = ref([
    { id: 1, nombre: 'Gestrasing SAS', imgUrl: './src/assets/logo-gestrasing.png' },
    { id: 2, nombre: 'Sabor Latino', imgUrl: './src/assets/saborlatino.png' },
    { id: 3, nombre: 'Restaurante el Triangulo', imgUrl: './src/assets/triangulo.png' },
    { id: 4, nombre: 'DeltaZero', imgUrl: './src/assets/deltazero-logo.png' }
]);
</script>

<template>
    <section class="ticker-seccion" id="clientes">
        <div class="contenedor-encabezado">
            <span class="etiqueta-nexova">Nuestros Clientes</span>
            <!-- <h2>Ingeniería probada en el mundo real</h2> -->
        </div>

        <div class="ticker-wrapper">
            
            <div class="fade-vignette left"></div>
            <div class="fade-vignette right"></div>

            <div class="ticker-track">
                
                <!-- GRUPO A -->
                <div class="ticker-group">
                    <div v-for="cliente in clientes" :key="'A-' + cliente.id" class="cliente-item">
                        <div class="logo-box">
                            <img :src="cliente.imgUrl" :alt="`Logo de ${cliente.nombre}`" class="logo-img" />
                        </div>
                        <span class="cliente-nombre">{{ cliente.nombre }}</span>
                    </div>
                </div>

                <!-- GRUPO B (Clon matemático para el scroll infinito) -->
                <div class="ticker-group" aria-hidden="true">
                    <div v-for="cliente in clientes" :key="'B-' + cliente.id" class="cliente-item">
                        <div class="logo-box">
                            <img :src="cliente.imgUrl" :alt="`Logo de ${cliente.nombre}`" class="logo-img" />
                        </div>
                        <span class="cliente-nombre">{{ cliente.nombre }}</span>
                    </div>
                </div>

            </div>

        </div>
    </section>
</template>

<style scoped>
/* ==========================================================================
   MOBILE FIRST ESTRICTO
   ========================================================================== */
.ticker-seccion {
    background-color: #09090b; /* Negro puro */
    padding: 5rem 0; 
    font-family: 'Inter', sans-serif;
    overflow: hidden;
    position: relative;
}

.contenedor-encabezado {
    text-align: center;
    padding: 0 1.5rem;
    margin-bottom: 3.5rem;
}

.etiqueta-nexova {
    color: #34d399;
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

.contenedor-encabezado h2 {
    font-size: clamp(1.8rem, 5vw, 2.4rem);
    color: #ffffff;
    font-weight: 800;
    margin: 0;
    letter-spacing: -0.5px;
}

.ticker-wrapper {
    position: relative;
    width: 100%;
    max-width: 100vw;
    overflow: hidden;
}

.fade-vignette {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 80px;
    z-index: 2;
    pointer-events: none;
}

.fade-vignette.left {
    left: 0;
    background: linear-gradient(to right, #09090b 0%, rgba(9,9,11,0) 100%);
}

.fade-vignette.right {
    right: 0;
    background: linear-gradient(to left, #09090b 0%, rgba(9,9,11,0) 100%);
}

.ticker-track {
    display: flex;
    width: max-content;
    animation: scroll-infinito 15s linear infinite;
}

.ticker-track:hover {
    animation-play-state: paused;
}

.ticker-group {
    display: flex;
    align-items: center;
    justify-content: space-around;
    gap: 4rem; 
    padding-right: 4rem; 
}

/* --- EL NODO DEL CLIENTE --- */
.cliente-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    opacity: 0.45;
    filter: grayscale(100%); /* Vuelve cualquier logo a color a un tono plateado elegante */
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

/* LA CAJA PROTECTORA DEL LOGO */
.logo-box {
    height: 34px; /* Altura restrictiva para móvil */
    display: flex;
    align-items: center;
    justify-content: center;
}

.logo-img {
    max-height: 100%;
    width: auto;
    object-fit: contain; /* Impide la deformación */
    display: block;
    transition: transform 0.3s ease;
}

.cliente-nombre {
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    letter-spacing: -0.5px;
    white-space: nowrap; 
}

/* Interacción Hover */
.cliente-item:hover {
    opacity: 1;
    filter: grayscale(0%); /* El logo recupera sus colores originales al tocarlo */
    transform: scale(1.06);
}

.cliente-item:hover .logo-img {
    transform: scale(1.1);
}

.cliente-item:hover .cliente-nombre {
    color: #ffffff;
}

@keyframes scroll-infinito {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}

/* Adaptación a PC */
@media (min-width: 768px) {
    .ticker-seccion {
        padding: 7rem 0;
    }
    .fade-vignette {
        width: 150px;
    }
    .logo-box {
        height: 42px; /* En escritorio los logos crecen proporcionalmente */
    }
    .cliente-nombre {
        font-size: 1.25rem;
    }
}
</style>