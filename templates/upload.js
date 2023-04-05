document.getElementById('upload').addEventListener('submit', function (e) {
    e.preventDefault();

    const userFile = document.getElementById('file').files[0];
    const userComments = document.getElementById('comments').value;

    const formData = new FormData();
    formData.append('user-file', userFile, 'user-file.json');
    formData.append('user-comments', userComments);


    fetch(': http://127.0.0.1:8000/uploadfile/', {
        method: "POST",
        body: formData,
    })

        .then(res => res.json())
        .then(data => console.log(data))
        .catch(err => console.log(err));
})
function fun() {
    alert("File uploaded successfully")
}