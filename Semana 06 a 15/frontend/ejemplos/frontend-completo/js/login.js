// Lógica del login

document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();
    login();
});

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('http://127.0.0.1:5000/libreria/api/v1/usuarios/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username, password: password })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.usuario) {
                document.getElementById('mensaje').innerText = data.mensaje;
                // Aquí podrías redirigir o guardar en localStorage, etc.
                localStorage.setItem('usuario', JSON.stringify(data.usuario));
            // Luego redirigimos a la página de libros
                window.location.href = 'pages/welcome.html';
            
            } else {
                document.getElementById('mensaje').innerHTML = '<p>Login fallido.</p>';
            }
        })
        .catch(error => {
            document.getElementById('mensaje').innerHTML = '<p>Error de red o servidor.</p>';
            console.error('Error:', error);
        });
}
