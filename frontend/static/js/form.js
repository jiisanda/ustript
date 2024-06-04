let area = document.getElementById('uploadfile');
area.addEventListener('dragover', (event) => {
    event.preventDefault();
});

area.addEventListener('drop', (event) => {
    event.preventDefault();
    document.getElementById('file').files = event.dataTransfer.files;
});

document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let fileInput = document.getElementById('file');
    let file = fileInput.files[0];
    let formData = new FormData();
    formData.append('file', file);

    fetch('/test/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        let parsedData = JSON.parse(data);
        let responseDiv = document.getElementById('response');
        responseDiv.textContent = JSON.stringify(parsedData, null, 2);
    })
    .catch(error => console.error('Error:', error));
});