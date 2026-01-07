# Renders_IA 🏗️

Aplicación web con inteligencia artificial para generar renders fotorealistas de construcción a partir de planos arquitectónicos.

## Características

- 📸 **Carga de Planos**: Sube imágenes de planos arquitectónicos en diversos formatos (PNG, JPG, JPEG, GIF, BMP)
- 🤖 **IA Avanzada**: Utiliza OpenAI DALL-E 3 para generar renders de alta calidad
- ✍️ **Personalización**: Describe cómo quieres que se vea tu render con prompts personalizados
- 🎨 **Resultados Profesionales**: Obtén renders fotorealistas con iluminación natural y materiales realistas
- 💾 **Descarga Fácil**: Descarga los renders generados directamente desde la aplicación

## Requisitos Previos

- Python 3.8 o superior
- Cuenta de OpenAI con acceso a la API de DALL-E 3
- Clave API de OpenAI

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Cristina-Puertas-Camarero/Renders_IA.git
   cd Renders_IA
   ```

2. **Crear un entorno virtual** (recomendado)
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   
   Copia el archivo `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
   
   Edita el archivo `.env` y añade tu clave API de OpenAI:
   ```
   OPENAI_API_KEY=tu_clave_api_de_openai
   FLASK_SECRET_KEY=tu_clave_secreta_personalizada
   FLASK_ENV=development
   ```

## Uso

1. **Iniciar la aplicación**
   ```bash
   python app.py
   ```

2. **Acceder a la aplicación**
   
   Abre tu navegador y ve a: `http://localhost:5000`

3. **Generar un render**
   - Haz clic en el área de carga o arrastra un archivo de plano
   - Describe cómo quieres que se vea el render (ej: "Exterior moderno con fachada de vidrio, iluminación al atardecer")
   - Haz clic en "Generar Render"
   - Espera unos segundos mientras la IA procesa tu solicitud
   - Descarga o genera otro render

## Estructura del Proyecto

```
Renders_IA/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias Python
├── .env.example          # Ejemplo de configuración
├── .gitignore           # Archivos ignorados por git
├── README.md            # Este archivo
├── templates/
│   └── index.html       # Interfaz web principal
├── static/
│   ├── css/
│   │   └── style.css    # Estilos de la aplicación
│   ├── js/
│   │   └── main.js      # Lógica del frontend
│   └── generated/       # Renders generados (creado automáticamente)
└── uploads/             # Planos subidos (creado automáticamente)
```

## Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **IA**: OpenAI DALL-E 3
- **Frontend**: HTML5, CSS3, JavaScript
- **Procesamiento de Imágenes**: Pillow (PIL)

## Ejemplos de Prompts

Para obtener mejores resultados, usa descripciones detalladas:

- "Exterior moderno con fachada de vidrio y acero, iluminación natural al atardecer, jardines verdes, estilo contemporáneo minimalista"
- "Interior de oficina open-space con diseño industrial, techos altos, iluminación LED, mobiliario moderno"
- "Casa unifamiliar mediterránea con paredes blancas, tejas de barro, jardín con piscina, ambiente cálido"
- "Edificio de apartamentos urbano con balcones amplios, diseño sostenible, paneles solares, entorno urbano"

## Notas de Seguridad

- Nunca compartas tu clave API de OpenAI
- Mantén el archivo `.env` privado y nunca lo subas al control de versiones
- Los archivos subidos se guardan temporalmente y deben ser eliminados periódicamente

## Limitaciones

- Tamaño máximo de archivo: 16 MB
- La calidad del render depende de la claridad del plano y la descripción proporcionada
- El tiempo de generación puede variar según la carga del servidor de OpenAI

## Solución de Problemas

### Error: "No se ha proporcionado ningún archivo de plano"
Asegúrate de seleccionar un archivo antes de hacer clic en "Generar Render"

### Error: "Invalid API Key"
Verifica que tu clave API de OpenAI esté correctamente configurada en el archivo `.env`

### Error: "Rate limit exceeded"
Has excedido el límite de solicitudes de la API. Espera unos minutos e intenta de nuevo.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Soporte

Si tienes preguntas o necesitas ayuda, por favor abre un issue en el repositorio de GitHub.