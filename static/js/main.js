document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('renderForm');
    const blueprintInput = document.getElementById('blueprint');
    const previewImage = document.getElementById('previewImage');
    const fileName = document.getElementById('fileName');
    const generateBtn = document.getElementById('generateBtn');
    const btnText = document.querySelector('.btn-text');
    const btnLoading = document.querySelector('.btn-loading');
    const resultSection = document.getElementById('resultSection');
    const errorSection = document.getElementById('errorSection');
    const resultImage = document.getElementById('resultImage');
    const downloadLink = document.getElementById('downloadLink');
    const errorText = document.getElementById('errorText');

    // Handle file selection
    blueprintInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            fileName.textContent = file.name;
            
            // Show preview
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result;
                previewImage.style.display = 'block';
                fileName.style.display = 'none';
            };
            reader.readAsDataURL(file);
        }
    });

    // Handle form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Hide previous results/errors
        resultSection.style.display = 'none';
        errorSection.style.display = 'none';
        
        // Show loading state
        generateBtn.disabled = true;
        btnText.style.display = 'none';
        btnLoading.style.display = 'inline-flex';
        
        // Prepare form data
        const formData = new FormData(form);
        
        try {
            const response = await fetch('/generate', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (response.ok && data.success) {
                // Show result
                resultImage.src = data.image_url;
                downloadLink.href = data.image_url;
                resultSection.style.display = 'block';
                
                // Scroll to result
                resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else {
                // Show error
                showError(data.error || 'Error desconocido al generar el render');
            }
        } catch (error) {
            console.error('Error:', error);
            showError('Error de conexión. Por favor, inténtelo de nuevo.');
        } finally {
            // Reset button state
            generateBtn.disabled = false;
            btnText.style.display = 'inline';
            btnLoading.style.display = 'none';
        }
    });
});

function showError(message) {
    const errorSection = document.getElementById('errorSection');
    const errorText = document.getElementById('errorText');
    
    errorText.textContent = message;
    errorSection.style.display = 'block';
    errorSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function resetForm() {
    const form = document.getElementById('renderForm');
    const resultSection = document.getElementById('resultSection');
    const errorSection = document.getElementById('errorSection');
    const previewImage = document.getElementById('previewImage');
    const fileName = document.getElementById('fileName');
    
    form.reset();
    resultSection.style.display = 'none';
    errorSection.style.display = 'none';
    previewImage.style.display = 'none';
    fileName.style.display = 'block';
    fileName.textContent = 'Selecciona un archivo o arrastra aquí';
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
}
