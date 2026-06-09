<script setup>
import Button from 'primevue/button';

const scrollTo = (idDestino) => {
    const seccion = document.getElementById(idDestino);
    if (seccion) {
        seccion.scrollIntoView({ behavior: 'smooth'});
    }
};
</script>

<template>
    <section class="adn-nexova" id="nosotros">
        <div class="contenedor">
            
            <div class="grid-principal">
                
                <div class="contenido-texto">
                    <span class="etiqueta-nexova">Nuestro ADN</span>
                    <h2>Desbloqueamos el verdadero<br> potencial de tu empresa.</h2>
                    
                    <p style="text-align: start;" class="parrafo-principal">
                        La tecnología no debería ser un dolor de cabeza, debería ser lo que te hace crecer. En <strong>Nexova</strong> convertimos lo técnico en resultados concretos: más clientes, procesos más rápidos y un negocio que funciona aunque no estés mirando.
                    </p>
                    <p style="text-align: start;" class="parrafo-principal">
                        No importa si estás empezando o si ya tienes un negocio consolidado. Te acompañamos en cada paso.
                    </p>

                    <!-- <ul class="lista-beneficios">
                        <li><i class="pi pi-check-circle"></i> Construido para crecer: lo que hacemos hoy no te queda pequeño mañana</li>
                        <li><i class="pi pi-check-circle"></i> Tu información, siempre protegida: porque los datos de tu empresa no son un riesgo que debas correr.</li>
                        <li><i class="pi pi-check-circle"></i> Siempre al tanto: sabes en qué vamos, cuándo entregamos y cómo va tu proyecto sin tener que preguntar.</li>
                    </ul> -->

                    <Button label="Hablemos de tu proyecto" 
                            icon="pi pi-comments"
                            size="large" 
                            class="boton-contacto"
                            @click="scrollTo('contacto')" />
                </div>

                <div class="grid-metricas">
                    
                    <div class="metrica-card oscura">
                        <i class="pi pi-sync"></i>
                        <h3>Entregas que puedes ver</h3>
                        <p>Te mostramos avances reales en cada etapa. Nada de sorpresas al final.</p>
                    </div>

                    <div class="metrica-card clara">
                        <i class="pi pi-shield"></i> 
                        <h3>Tu data bajo llave</h3>
                        <p>Aplicamos estándares corporativos para proteger la información de tu empresa.</p>
                    </div>

                    <div class="metrica-card destacada">
                        <div class="destacada-contenido">
                            <span class="numero-grande">360°</span>
                            <div class="destacada-texto">
                                <h3>Una sola empresa, todo resuelto</h3>
                                <p>Web, software, soporte técnico y mantenimiento. No necesitas buscar a nadie más.</p>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

        </div>
    </section>
</template>

<style scoped>
/* 1. CONTENEDOR Y FONDOS */
.adn-nexova {
    background-color: #ffffff; /* Blanco puro para descansar la vista */
    padding: 7rem 2rem;
    font-family: 'Inter', sans-serif;
}

.contenedor {
    max-width: 1200px;
    margin: 0 auto;
}

/* 2. LAYOUT PRINCIPAL: Dividimos la pantalla en 2 mitades */
.grid-principal {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}

/* 3. TIPOGRAFÍA Y TEXTOS (Columna Izquierda) */
.etiqueta-nexova {
    color: #0F8B58; /* Verde Nexova */
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    display: block;
    margin-bottom: 1.5rem;
}

.contenido-texto h2 {
    font-size: 2.5rem;
    color: #0f172a;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1.5rem;
}

.parrafo-principal {
    font-size: 1.2rem;
    color: #334155;
    line-height: 1.6;
    margin-bottom: 1rem;
    font-weight: 500;
}

.parrafo-secundario {
    font-size: 1.1rem;
    color: #64748b;
    line-height: 1.7;
    margin-bottom: 2rem;
}

/* 4. LISTA DE BENEFICIOS */
.lista-beneficios {
    list-style: none;
    padding: 0;
    margin-bottom: 2.5rem;
}

.lista-beneficios li {
    display: flex;
    align-items: start;
    gap: 0.75rem;
    font-size: 1.05rem;
    color: #475569;
    margin-bottom: 0.8rem;
}

.lista-beneficios i {
    color: #0F8B58; /* Chulos (checks) en Verde Nexova */
    font-size: 1.2rem;
}

.boton-contacto {
    margin-top: 1rem;
}

/* 5. CUADRÍCULA DERECHA (Métricas y ADN) */
.grid-metricas {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
}

.metrica-card {
    padding: 2rem;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: transform 0.3s ease;
}

.metrica-card:hover {
    transform: translateY(-5px);
}

.metrica-card i {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.metrica-card h3 {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
    font-weight: 700;
}

.metrica-card p {
    font-size: 0.95rem;
    line-height: 1.5;
    margin: 0;
}

/* Estilos específicos de cada tarjeta para crear un "Patrón de Tablero" */
.oscura {
    background: linear-gradient(
        to bottom right,
        #0f172a 0%,
        #0c1a3a 40%,
        #0e2a45 70%,
        #0f172a 100%
    ); /* Azul corporativo muy oscuro */
    color: white;
    padding: 2.5rem 2rem;
}

.oscura i { color: #BCE4D3; /* Verde Menta para contrastar */ }
.oscura p { color: #eaf6f0; }

.clara {
    background: linear-gradient(
        to bottom right,
        #0f172a 0%,
        #0c1a3a 40%,
        #0e2a45 70%,
        #0f172a 100%
    ); /* Azul corporativo muy oscuro */
    color: white;
    padding: 2.5rem 2rem;
}

.clara i { color: #0F8B58; }
.clara p { color: #ffffff; }

/* La tarjeta destacada ocupa todo el ancho inferior (span 2) */
.destacada {
    grid-column: span 2;
    background: linear-gradient(
        to bottom right,
        #0f172a 0%,
        #0c1a3a 40%,
        #0e2a45 70%,
        #0f172a 100%
    ); /* Azul corporativo muy oscuro */
    color: white;
    padding: 2.5rem 2rem;
}

.destacada-contenido {
    display: flex;
    align-items: center;
    gap: 2rem;
}

.numero-grande {
    font-size: 3.5rem;
    font-weight: 900;
    color: #34d399; /* Verde vibrante */
    line-height: 1;
}

.destacada-texto p { color: #ffffff; }

/* 6. RESPONSIVO (Móviles y Tablets) */
@media (max-width: 992px) {
    .grid-principal {
        grid-template-columns: 1fr; /* Pasa a 1 sola columna */
        gap: 3rem;
    }
    .destacada-contenido {
        flex-direction: column;
        text-align: center;
        gap: 1rem;
    }
}

@media (max-width: 576px) {
    .grid-metricas {
        grid-template-columns: 1fr; /* Las tarjetitas también pasan a 1 columna */
    }
    .destacada {
        grid-column: span 1;
    }
}
</style>