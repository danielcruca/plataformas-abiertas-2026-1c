
# Introducción práctica a HTML y JavaScript para el proyecto

Este documento resume **solo los elementos de HTML y JavaScript que se utilizan directamente** en el proyecto `frontend-completo`. 

---

## 🧱 HTML: Elementos fundamentales usados

### 1. Formularios (`<form>`)
Se utilizan para enviar datos (como el login de usuario).

```html
<form id="loginForm">
  <label for="usuario">Usuario:</label>
  <input type="text" id="usuario" />
  <label for="clave">Contraseña:</label>
  <input type="password" id="clave" />
  <button type="submit">Ingresar</button>
</form>
```

---

### 2. Entradas de datos (`<input>`, `<select>`, `<label>`)
Para capturar texto, seleccionar opciones, etc.

```html
<input type="text" id="buscar" placeholder="Buscar libro..." />
<select id="categoria">
  <option value="todos">Todos</option>
  <option value="ficcion">Ficción</option>
</select>
```

---

### 3. Tablas (`<table>`, `<thead>`, `<tbody>`)
Se utilizan para mostrar listas (libros, reportes, ventas).

```html
<table>
  <thead>
    <tr>
      <th>Título</th>
      <th>Autor</th>
      <th>Precio</th>
    </tr>
  </thead>
  <tbody id="tablaLibros">
    <!-- Filas generadas por JavaScript -->
  </tbody>
</table>
```

---

### 4. Navegación (`<a href>`), estructura (`<div>`, `<nav>`)
Organizan la interfaz y permiten navegar entre vistas.

```html
<nav>
  <a href="libros.html">Libros</a>
  <a href="ventas.html">Ventas</a>
</nav>
```

---

## 🧠 JavaScript: Funciones clave

### 1. Selección de elementos
```js
const boton = document.getElementById("btnGuardar");
const formulario = document.querySelector("#loginForm");
```

---

### 2. Manejo de eventos
```js
formulario.addEventListener("submit", function(e) {
  e.preventDefault();
  loginUsuario();
});
```

---

### 3. Fetch API (llamadas HTTP)
```js
fetch("http://localhost:5000/api/v1/libros")
  .then(res => res.json())
  .then(data => console.log(data));
```

---

### 4. localStorage
Se usa para guardar y leer el token de sesión.

```js
localStorage.setItem("token", respuesta.token);
const token = localStorage.getItem("token");
```

---

### 5. Modificar contenido dinámico
```js
document.getElementById("mensaje").textContent = "Bienvenido";
document.getElementById("tablaLibros").innerHTML += filaHTML;
```

---

### 6. Funciones
```js
function loginUsuario() {
  // Lógica de autenticación
}
```