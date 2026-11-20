# 🚀 NeuroLectura Arcade 11
### Suite de 30 Microjuegos Multisensoriales y Telemetría Cognitiva para Entrenamiento Lector

Diseñado especialmente para niños de **11 años** con dificultades severas en decodificación de letras, dislexia del desarrollo o dificultades en procesamiento fonológico y visual.

[![Jugar Online](https://img.shields.io/badge/🎮%20Jugar%20Online-GitHub%20Pages-success?style=for-the-badge&logo=github)](https://carloscarbajallinan.github.io/neurolectura-arcade/)
[![Código Abierto](https://img.shields.io/badge/Licencia-MIT-blue?style=for-the-badge)](https://github.com/carloscarbajallinan/neurolectura-arcade)

---

## 🌐 Juega Directamente en el Navegador (Sin Instalar Nada)

👉 **[Haz clic aquí para Jugar NeuroLectura Arcade en Vivo](https://carloscarbajallinan.github.io/neurolectura-arcade/)**

Puedes abrir este enlace en cualquier computadora, laptop, tablet o teléfono móvil.
- Compatible con Chrome, Edge, Safari, Firefox y Brave.
- Usa la síntesis de voz en español nativa del navegador (`Web Speech API`) y efectos sonoros (`Web Audio API`).
- Guarda el progreso, estrellas y precisión en la memoria del navegador (`localStorage`).
- Permite descargar el registro de rendimiento en **Excel (CSV)** e imprimir el reporte clínico.

---

## 📌 ¿Cómo iniciar el juego?

Tienes dos opciones muy sencillas:

### Opción A: Modo Escritorio (Recomendado para guardar registros automáticos)
1. Haz doble clic en el archivo **`Iniciar_LecturaArcade.bat`** (o en **`Iniciar_LecturaArcade_Silencioso.vbs`**).
2. Se abrirá una ventana de escritorio dedicada (estilo aplicación nativa de Windows).
3. Cada partida que termine tu primo se guardará automáticamente en tiempo real en la carpeta `registros/registro_rendimiento.csv` (listo para abrir en Excel).

### Opción B: Modo Archivo Único HTML (Portátil / Sin instalación)
1. Haz doble clic directo sobre **`index.html`** con cualquier navegador (Chrome, Edge, Firefox, Brave, Safari).
2. Funciona 100% desconectado a internet (offline).
3. Las estadísticas y estrellas se guardan en el navegador y puedes descargar el registro en Excel/CSV pulsando **"📊 Analizar Rendimiento" -> "📥 Descargar CSV"**.

---

## 🎚️ Niveles de Dificultad y Tutoriales Interactivos Animados

### 1. Tres Niveles de Desafío (🟢 Fácil | 🟡 Medio | 🔴 Desafío)
- **Fácil**: Rimas directas, apoyos de color para $b$ (azul) y $d$ (naranja), mayor tiempo de lectura y menos distractores.
- **Medio**: Longitud equilibrada con palabras cotidianas y discriminación visual estándar.
- **Desafío**: Trampas fonológicas complejas como **pseudo-rimas** (ej. *MESA* vs *META* o *BOTE* vs *BOTA* que parecen sonar igual pero **NO riman**), letras simétricas en color blanco sin ayudas cromáticas y mayor agilidad.

### 2. Botón de Tutorial & Teoría Dinámica (`💡 Tutorial & Teoría`)
- En cualquier juego, tu primo puede presionar el botón de Tutorial para abrir una explicación animada:
  - **Animación de los pulgares (👍 cama)** para entender la orientación de $b$ y $d$.
  - **Ondas sonoras animadas** para entender la música de las rimas.
  - **Vagón de tren** para visualizar el rastreo de izquierda a derecha.
- Incluye el botón **"🔊 Escuchar Explicación"** para que el sintetizador de voz le explique la teoría sin obligarlo a leer textos densos.

### 3. Diseño Limpio y Anti-Saturación
- Interfaz despejada, con fondos oscuros relajantes, botones amplios y tipografía accesible adaptada para dislexia y TDAH.

---

## 🎲 Generador Dinámico Anti-Repetición

Todos los juegos han sido actualizados con algoritmos de **generación procedural y bancos masivos de contenido** (`CONTENT_POOLS` con más de 400 palabras, fonemas y retos):
- **Crucigramas / Sopa de Letras (Juego #29)**: Cada vez que se juega, se selecciona una palabra distinta y se construye una cuadrícula 4x4 única en orientación horizontal o vertical con distractores aleatorios.
- **Laberintos (Juego #11)**: El camino se traza automáticamente con diferentes letras diana ($S, M, B, P, L, T, D$).
- **Memoramas (Juego #12)**: Elige 4 pares al azar de entre todo el abecedario (A a la Z).
- **Desafío b/d/p/q y Desafío Maestro (Juegos #7, #8, #30)**: Rejillas y preguntas que rotan dinámicamente en cada partida.

---

## 🧠 Los 5 Pilares de Habilidades y los 30 Juegos

| Pilar | Habilidad Neurocognitiva | Juegos Incluidos |
|---|---|---|
| **🎧 Pilar 1** | **Conciencia Fonológica y Fonémica**<br>*(Entrenar el oído antes que el ojo)* | **#1** Cazador de Sonidos Iniciales<br>**#2** El Eco de las Rimas<br>**#3** Contador de Golpes de Sílaba<br>**#4** ¿Quién se Escapó? (Omisión)<br>**#5** Fusión de Sonidos Mágicos<br>**#6** El Sonido Espía |
| **👁️ Pilar 2** | **Discriminación Visual & Espacial**<br>*(Superar la rotación y confusión de b, d, p, q)* | **#7** El Desafío Espejo (b vs d)<br>**#8** El Cuarteto Rebelde (b, d, p, q)<br>**#9** El Impostor Rotado (M/W, n/u)<br>**#10** Siluetas y Sombras de Letras<br>**#11** Laberinto de la Letra Fiel<br>**#12** Memorama de Letras Gemelas (A-a) |
| **⚡ Pilar 3** | **Correspondencia Grafema-Fonema**<br>*(El puente neural: conectar símbolo con sonido)* | **#13** La Tecla Parlante<br>**#14** Diana de Fonemas<br>**#15** Cofre del Tesoro Vocálico<br>**#16** La Ruleta de Consonantes<br>**#17** El Alfabeto Musical<br>**#18** Lluvia de Letras del Cielo |
| **🧱 Pilar 4** | **Memoria de Trabajo & Sílabas**<br>*(Ensamblar y retener sonidos en secuencia)* | **#19** El Tren de las Sílabas (C+V)<br>**#20** Simón Fonológico (Memoria)<br>**#21** Fábrica de Palabras C-V-C<br>**#22** Torre de Sílabas Desordenadas<br>**#23** El Puente Cortado (Letra faltante)<br>**#24** Flash de Memoria Rápida (Fijación 2s) |
| **🎯 Pilar 5** | **Rastreo Visual & Fluidez Lectora**<br>*(Agilidad ocular de izquierda a derecha y RAN)* | **#25** La Linterna en la Noche (Focalización)<br>**#26** Pista de Carreras Lectora<br>**#27** El Radar de la Letra Clave<br>**#28** Lectura con Metrónomo Rítmico<br>**#29** Sopa de Letras Guiada (3x3)<br>**#30** El Desafío Maestro de las 10 Gemas |

---

## 📊 Sistema de Telemetría y Análisis de Rendimiento

El sistema incluye un módulo de analítica accesible desde el botón superior **"📊 Analizar Rendimiento"**:
- **Precisión global y por pilar**: Permite identificar exactamente dónde está la barrera (¿falla más en orientación de letras o en discriminar sonidos?).
- **Detección automática de confusiones específicas**: Si el niño suele confundir $b$ con $d$ o $p$ con $q$, el reporte lo señalará explícitamente como recomendación.
- **Exportación en CSV**: Genera una hoja de cálculo con fecha, aciertos, tiempo por juego e intentos, ideal para llevarla al neurólogo, psicólogo o terapeuta de aprendizaje.

---

## 💡 Consejos de Acompañamiento para tu Primo (11 años)

1. **Sesiones cortas (15 a 20 minutos al día):** Es preferible jugar 3 o 4 microjuegos diarios que agotarlo en una sesión larga.
2. **Usa la voz y los audífonos:** Anímalo a pulsar el botón "🔊 Repetir Voz" cuantas veces quiera. El circuito auditivo refuerza el visual.
3. **Mnemotecnia visual de los pulgares:** En los juegos de $b$ y $d$, recuérdale cerrar los puños con los pulgares hacia arriba: la mano izquierda forma una **b** (👍) y la mano derecha forma una **d** (👍). Juntas forman una "cama" (**b**-e-**d**).
4. **Cero frustración:** El juego no tiene castigos ni ruidos molestos. Cada error es solo una oportunidad para volver a escuchar con calma.
