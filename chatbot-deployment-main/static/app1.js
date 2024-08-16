function processImage() {
    const uploadForm = document.getElementById('upload-form');
    const outputContainer = document.getElementById('output-container');
    const processedImage = document.getElementById('processed-image');
    const downloadLink = document.getElementById('download-link');

    const formData = new FormData(uploadForm);

    fetch('/process', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        processedImage.src = data.processed_image;
        outputContainer.style.display = 'block';
        downloadLink.href = data.processed_image;
    })
    .catch(error => console.error('Error:', error));
}
