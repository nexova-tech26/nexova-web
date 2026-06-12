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
                
                <div class="contenido-texto" data-aos="fade-right">
                    <span class="etiqueta-nexova">Nuestro ADN</span>
                    <h2>Desbloqueamos el verdadero<br> potencial de tu empresa.</h2>
                    
                    <p class="parrafo-principal">
                       En <strong>Nexova Tech</strong> convertimos lo técnico en resultados concretos: procesos más rápidos y un negocio que funciona aunque no estés mirando.
                    </p>

                    <ul class="lista-beneficios">
                        <li>
                            <div class="icono-check"><i class="pi pi-check"></i></div>
                            <span><strong>Escalabilidad:</strong> Lo que hacemos hoy no te queda pequeño mañana.</span>
                        </li>
                        <li>
                            <div class="icono-check"><i class="pi pi-check"></i></div>
                            <span><strong>Acompañamiento:</strong> Te guiamos en cada paso.</span>
                        </li>
                    </ul>

                    <Button label="Hablemos de tu proyecto" 
                            icon="pi pi-comments"
                            size="large" 
                            class="boton-contacto btn-primary-nexova"
                            @click="scrollTo('contacto')" />
                </div>

                <div class="grid-metricas" data-aos="fade-left">
                    
                    <div class="metrica-card oscura">
                        <i class="pi pi-sync"></i>
                        <h3>Transparencia total</h3>
                        <p>Te mostramos avances reales en cada etapa. Cero sorpresas al final del proyecto.</p>
                    </div>

                    <div class="metrica-card acento-verde">
                        <i class="pi pi-shield"></i> 
                        <h3>Tu data bajo llave</h3>
                        <p>Estándares estrictos para proteger la información vital de tu operación.</p>
                    </div>

                    <div class="metrica-card destacada">
                        <div class="destacada-contenido">
                            <span class="numero-grande">360°</span>
                            <div class="destacada-texto">
                                <h3>Todo resuelto en un solo lugar</h3>
                                <p>Web, software a medida, soporte y mantenimiento continuo. Nos encargamos de la infraestructura para que tú te enfoques en el negocio.</p>
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
    background-color: #ffffff; 
    padding: 8rem 2rem;
    font-family: 'Inter', sans-serif;
    overflow: hidden;
}

.contenedor {
    max-width: 1200px;
    margin: 0 auto;
}

/* 2. LAYOUT PRINCIPAL */
.grid-principal {
    display: grid;
    grid-template-columns: 1fr 1.1fr; /* Le damos un poco más de espacio a las tarjetas */
    gap: 5rem;
    align-items: center;
}

/* 3. TIPOGRAFÍA Y TEXTOS */
.etiqueta-nexova {
    color: #0F8B58; 
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    display: inline-block;
    margin-bottom: 1rem;
    padding: 0.3rem 0.8rem;
    background-color: rgba(15, 139, 88, 0.1);
    border-radius: 20px;
}

.contenido-texto h2 {
    font-size: clamp(2rem, 4vw, 2.8rem);
    color: #0f172a;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 1.5rem;
    letter-spacing: -0.5px;
}

.parrafo-principal {
    font-size: 1.15rem;
    color: #475569;
    line-height: 1.7;
    margin-bottom: 2rem;
}

/* 4. LISTA DE BENEFICIOS (Rediseñada) */
.lista-beneficios {
    list-style: none;
    padding: 0;
    margin-bottom: 2.5rem;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
}

.lista-beneficios li {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    font-size: 1.05rem;
    color: #334155;
    line-height: 1.5;
}

.icono-check {
    background-color: #0F8B58;
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    font-size: 0.8rem;
    margin-top: 0.1rem;
    box-shadow: 0 4px 10px rgba(15, 139, 88, 0.3);
}

/* Ajuste del botón */
:deep(.btn-primary-nexova) {
    background-color: #0F8B58;
    border-color: #0F8B58;
    transition: all 0.3s ease;
    border-radius: 8px;
}

:deep(.btn-primary-nexova:hover) {
    background-color: #0b6b43;
    border-color: #0b6b43;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px -6px rgba(15, 139, 88, 0.6);
}

/* 5. CUADRÍCULA DERECHA (Bento Box Style) */
.grid-metricas {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.2rem;
}

.metrica-card {
    padding: 2.2rem 1.8rem;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.metrica-card:hover {
    transform: translateY(-5px);
}

.metrica-card i {
    font-size: 2.2rem;
    margin-bottom: 1.2rem;
}

.metrica-card h3 {
    font-size: 1.25rem;
    margin-bottom: 0.8rem;
    font-weight: 700;
    line-height: 1.3;
}

.metrica-card p {
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 0;
    opacity: 0.9;
}

/* Tarjeta Oscura Neutra */
.oscura {
    background-color: #18181b; /* Gris casi negro, muy elegante */
    border: 1px solid #27272a;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}

.oscura i { color: #34d399; } /* Icono verde claro */
.oscura p { color: #a1a1aa; }

/* Tarjeta Acento (Totalmente Verde Corporativo) */
.acento-verde {
    background: linear-gradient(135deg, #0F8B58 0%, #0b6b43 100%);
    color: white;
    box-shadow: 0 10px 30px rgba(15, 139, 88, 0.2);
}

.acento-verde i { color: #ffffff; }
.acento-verde p { color: #eaf6f0; }

/* Tarjeta Destacada Inferior */
.destacada {
    grid-column: span 2;
    background-color: #fafafa;
    border: 1px solid #e4e4e7;
    color: #0f172a;
}

.destacada:hover {
    box-shadow: 0 10px 40px rgba(0,0,0,0.04);
}

.destacada-contenido {
    display: flex;
    align-items: center;
    gap: 2rem;
}

.numero-grande {
    font-size: 4rem;
    font-weight: 900;
    color: #0F8B58; 
    line-height: 1;
    letter-spacing: -2px;
}

.destacada-texto p { color: #475569; }

/* 6. RESPONSIVO */
@media (max-width: 992px) {
    .grid-principal {
        grid-template-columns: 1fr; 
        gap: 4rem;
    }
    .contenido-texto {
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .lista-beneficios li {
        text-align: left;
    }
}

@media (max-width: 576px) {
    .adn-nexova {
        padding: 5rem 1.5rem;
    }
    .grid-metricas {
        grid-template-columns: 1fr; 
    }
    .destacada {
        grid-column: span 1;
    }
    .destacada-contenido {
        flex-direction: column;
        text-align: center;
        gap: 1.5rem;
    }
}
</style>