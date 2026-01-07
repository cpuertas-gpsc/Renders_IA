# Guía de Uso - Generador de Renders IA

## Inicio Rápido

### 1. Configuración Inicial

Antes de usar la aplicación, asegúrate de tener configurada tu clave API de OpenAI en el archivo `.env`:

```bash
# Copia el archivo de ejemplo
cp .env.example .env

# Edita el archivo .env y añade tu clave API
# OPENAI_API_KEY=sk-...tu-clave-aquí...
```

### 2. Iniciar la Aplicación

```bash
# Activa el entorno virtual (si usas uno)
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Inicia la aplicación
python app.py
```

Verás un mensaje como:
```
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

### 3. Acceder a la Interfaz Web

Abre tu navegador y navega a: `http://localhost:5000`

## Flujo de Trabajo

### Paso 1: Subir un Plano

1. Haz clic en el área de carga o arrastra un archivo
2. Formatos soportados: PNG, JPG, JPEG, GIF, BMP
3. Tamaño máximo: 16 MB
4. Verás una vista previa del plano subido

**Ejemplo de planos que puedes usar:**
- Planos arquitectónicos 2D
- Dibujos técnicos de construcción
- Bocetos de diseño
- Plantas arquitectónicas
- Elevaciones de fachadas

### Paso 2: Describir el Render Deseado

Escribe una descripción detallada de cómo quieres que se vea el render. Cuanto más detallada sea la descripción, mejor será el resultado.

**Ejemplos de descripciones efectivas:**

#### Para un edificio residencial:
```
Exterior moderno con fachada de vidrio y acero, iluminación natural al atardecer, 
jardines verdes bien cuidados, piscina, estilo contemporáneo minimalista, 
cielo azul con nubes suaves, entorno urbano de lujo
```

#### Para un espacio interior:
```
Interior de oficina open-space con diseño industrial, techos altos con vigas 
expuestas, iluminación LED cálida, mobiliario moderno y ergonómico, 
plantas decorativas, ambiente profesional y acogedor
```

#### Para un proyecto comercial:
```
Fachada comercial moderna con escaparates amplios, iluminación nocturna LED, 
entrada principal destacada, materiales de alta calidad como mármol y cristal, 
zona peatonal con personas caminando, ambiente urbano dinámico
```

### Paso 3: Generar el Render

1. Haz clic en el botón "Generar Render"
2. Espera mientras la IA procesa tu solicitud (normalmente 10-30 segundos)
3. El render aparecerá automáticamente cuando esté listo

### Paso 4: Descargar o Generar Otro

Una vez generado el render:
- **Descargar**: Haz clic en "📥 Descargar Render" para guardar la imagen
- **Generar Otro**: Haz clic en "🔄 Generar Otro" para crear un nuevo render

## Consejos para Mejores Resultados

### 1. Calidad del Plano
- Usa planos claros y legibles
- Asegúrate de que el plano tenga buena resolución
- Los planos con líneas definidas funcionan mejor

### 2. Descripción Detallada
- Incluye estilo arquitectónico (moderno, clásico, industrial, etc.)
- Especifica materiales (vidrio, acero, madera, hormigón, etc.)
- Menciona la iluminación deseada (natural, atardecer, nocturna, etc.)
- Describe el entorno (urbano, rural, jardines, etc.)
- Añade detalles atmosféricos (clima, hora del día, etc.)

### 3. Iteración
- Si el primer resultado no es perfecto, prueba con una descripción diferente
- Ajusta los detalles específicos que quieras mejorar
- Experimenta con diferentes estilos y enfoques

## Casos de Uso Comunes

### 1. Presentaciones a Clientes
Genera renders profesionales para mostrar cómo se verá el proyecto terminado.

### 2. Aprobaciones de Proyectos
Crea visualizaciones para obtener aprobaciones de stakeholders o autoridades.

### 3. Marketing Inmobiliario
Produce imágenes atractivas para materiales de marketing y ventas.

### 4. Exploración de Diseño
Experimenta con diferentes estilos y acabados antes de la construcción.

## Solución de Problemas Comunes

### Error: "No se ha proporcionado ningún archivo de plano"
**Solución**: Asegúrate de seleccionar un archivo antes de hacer clic en generar.

### Error: "Tipo de archivo no permitido"
**Solución**: Verifica que tu archivo sea PNG, JPG, JPEG, GIF o BMP.

### Error: "Invalid API Key"
**Solución**: 
1. Verifica que tu clave API esté correctamente configurada en `.env`
2. Asegúrate de que la clave sea válida y activa en tu cuenta de OpenAI
3. No incluyas espacios o comillas extra en el archivo `.env`

### Error: "Rate limit exceeded"
**Solución**: Has alcanzado el límite de la API. Espera unos minutos antes de intentar de nuevo.

### El render no se parece al plano
**Solución**: 
- DALL-E 3 genera interpretaciones creativas, no conversiones exactas
- Ajusta tu descripción para ser más específico sobre elementos clave
- El sistema usa el plano como inspiración, no como plantilla exacta

## Limitaciones Técnicas

1. **Tamaño de archivo**: Máximo 16 MB
2. **Tiempo de generación**: 10-30 segundos por render
3. **Resolución de salida**: 1024x1024 píxeles
4. **Interpretación creativa**: Los renders son interpretaciones artísticas, no conversiones exactas
5. **Límites de API**: Dependen de tu plan de OpenAI

## Preguntas Frecuentes

**P: ¿Puedo usar renders generados comercialmente?**
R: Sí, según los términos de uso de OpenAI, tienes los derechos sobre las imágenes generadas.

**P: ¿Cuánto cuesta cada render?**
R: Depende de tu plan de OpenAI. DALL-E 3 tiene un costo por imagen generada.

**P: ¿Puedo generar renders en diferentes resoluciones?**
R: Actualmente la aplicación genera renders de 1024x1024. Puedes modificar el código para usar otras resoluciones soportadas.

**P: ¿Los datos de mis planos son privados?**
R: Los planos se almacenan temporalmente en el servidor y se procesan a través de la API de OpenAI según sus políticas de privacidad.

## Soporte Adicional

Para más ayuda:
- Revisa el README.md del proyecto
- Abre un issue en GitHub
- Consulta la documentación de OpenAI DALL-E 3

---

**¡Disfruta creando renders increíbles con IA! 🏗️✨**
