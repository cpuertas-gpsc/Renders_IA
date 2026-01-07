import os
import base64
from io import BytesIO
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from openai import OpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['GENERATED_FOLDER'] = 'static/generated'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['GENERATED_FOLDER'], exist_ok=True)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def process_image(image_path, max_size=(1024, 1024)):
    """Process and resize image for API consumption"""
    img = Image.open(image_path)
    
    # Convert to RGB if necessary
    if img.mode in ('RGBA', 'LA', 'P'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
        img = background
    
    # Resize if too large
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    # Save to bytes
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_render():
    """Generate render from blueprint and prompt"""
    try:
        # Validate request
        if 'blueprint' not in request.files:
            return jsonify({'error': 'No se ha proporcionado ningún archivo de plano'}), 400
        
        file = request.files['blueprint']
        prompt = request.form.get('prompt', '')
        
        if file.filename == '':
            return jsonify({'error': 'No se ha seleccionado ningún archivo'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Tipo de archivo no permitido. Use PNG, JPG, JPEG, GIF o BMP'}), 400
        
        if not prompt:
            return jsonify({'error': 'Por favor, proporcione una descripción para el render'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process image
        image_base64 = process_image(filepath)
        
        # Create enhanced prompt for construction rendering
        enhanced_prompt = f"""Basándose en el plano arquitectónico proporcionado, crea un render fotorealista 3D de construcción con las siguientes características: {prompt}. 
        El render debe mostrar una visualización profesional y realista del proyecto de construcción, con iluminación natural, 
        materiales realistas y un entorno arquitectónico apropiado."""
        
        # Generate image using DALL-E 3
        response = client.images.generate(
            model="dall-e-3",
            prompt=enhanced_prompt[:4000],  # DALL-E 3 has a 4000 character limit
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Get generated image URL
        image_url = response.data[0].url
        
        return jsonify({
            'success': True,
            'image_url': image_url,
            'prompt_used': enhanced_prompt,
            'message': 'Render generado exitosamente'
        })
        
    except Exception as e:
        app.logger.error(f"Error generating render: {str(e)}")
        return jsonify({
            'error': f'Error al generar el render: {str(e)}'
        }), 500


@app.route('/generated/<path:filename>')
def generated_file(filename):
    """Serve generated files"""
    return send_from_directory(app.config['GENERATED_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
