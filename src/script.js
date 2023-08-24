function triggerFileInput() {
    const imageInput = document.getElementById('imageInput');
    imageInput.click();
}

document.getElementById('imageInput').addEventListener('change', function() {
    if (this.files && this.files[0]) {
        uploadImage();
    }
});

function uploadImage() {
    const project_name = document.getElementById('projectName').value;
    const imageFile = document.getElementById('imageInput').files[0];

    const formData = new FormData();
    formData.append('project_name', project_name);
    formData.append('image', imageFile);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Uploaded:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
