// Variables
let libroEditandoId = null;

// Obtener datos del formulario
function obtenerDatosFormulario() {
    return {
        titulo: document.getElementById("titulo").value,
        autor: {
            nombre: document.getElementById("autorNombre").value,
            apellido: document.getElementById("autorApellido").value,
            nacionalidad: document.getElementById("autorNacionalidad").value,
        },
        precio: parseFloat(document.getElementById("precio").value),
        cantidad_stock: parseInt(document.getElementById("stock").value),
    };
}

// Limpiar formulario y estado
function limpiarFormulario() {
    document.getElementById("form-libro").reset();
    libroEditandoId = null;
    document.querySelector('#form-libro button[type="submit"]').textContent = "Agregar libro";
    document.getElementById("cancelar-edicion").style.display = "none";
}

// Guardar libro (crear o actualizar)
function guardarLibro(data, id = null) {
    const url = id
        ? "http://127.0.0.1:5000/libreria/api/v1/libros/" + id
        : "http://127.0.0.1:5000/libreria/api/v1/libros";

    const method = id ? "PUT" : "POST";

    return fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    }).then((res) => res.json());
}

// Cargar libros
function cargarLibros() {
    fetch("http://127.0.0.1:5000/libreria/api/v1/libros")
        .then((res) => res.json())
        .then((libros) => {
            const tbody = document.querySelector("#tabla-libros tbody");
            tbody.innerHTML = "";
            libros.forEach((libro) => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${libro.titulo}</td>
                    <td>${libro.autor.nombre} ${libro.autor.apellido} (${libro.autor.nacionalidad})</td>
                    <td>$${libro.precio}</td>
                    <td>${libro.cantidad_stock}</td>
                    <td>
                        <button onclick="editarLibro('${libro._id}')">Editar</button>
                        <button onclick="eliminarLibro('${libro._id}')">Eliminar</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        });
}

// Editar libro
function editarLibro(id) {
    fetch("http://127.0.0.1:5000/libreria/api/v1/libros/" + id)
        .then((res) => res.json())
        .then((libro) => {
            document.getElementById("titulo").value = libro.titulo;
            document.getElementById("autorNombre").value = libro.autor.nombre;
            document.getElementById("autorApellido").value = libro.autor.apellido;
            document.getElementById("autorNacionalidad").value = libro.autor.nacionalidad;
            document.getElementById("precio").value = libro.precio;
            document.getElementById("stock").value = libro.cantidad_stock;

            libroEditandoId = libro._id;
            document.querySelector('#form-libro button[type="submit"]').textContent = "Actualizar libro";
            document.getElementById("cancelar-edicion").style.display = "inline-block";
        });
}

// Eliminar libro
function eliminarLibro(id) {
    if (!confirm("¿Seguro que deseas eliminar este libro?")) return;

    fetch("http://127.0.0.1:5000/libreria/api/v1/libros/" + id, {
        method: "DELETE",
    })
        .then((res) => res.json())
        .then((json) => {
            alert(json.mensaje);
            cargarLibros();
        });
}

// Cancelar edición
document.getElementById("cancelar-edicion").addEventListener("click", limpiarFormulario);

// Evento submit del formulario
document.getElementById("form-libro").addEventListener("submit", (e) => {
    e.preventDefault();
    const data = obtenerDatosFormulario();
    guardarLibro(data, libroEditandoId).then((json) => {
        alert(json.mensaje);
        limpiarFormulario();
        cargarLibros();
    });
});

// Inicial
cargarLibros();
