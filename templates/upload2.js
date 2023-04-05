const responseTimeLimit = 5000; // 5 seconds

async function upload(e) {
    e.preventDefault();
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://localhost:8000/uploadfile/', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    console.log(data);
    const responseP = document.createElement('p');
    responseP.innerText = JSON.stringify(data);

    const responseDiv = document.getElementById('response');
    responseDiv.appendChild(responseP);

    setTimeout(() => {
        responseDiv.removeChild(responseP);
    }, responseTimeLimit);
}

const form = document.getElementById('formContent');
form.addEventListener('submit', upload);

async function allow() {
    alert("Please Wait...")
}