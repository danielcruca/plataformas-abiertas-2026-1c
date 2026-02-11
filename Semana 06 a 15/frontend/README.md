
# 📘 Introducción a AJAX con JavaScript (Fetch API)

## Repaso Inicial de HTML y JavaScript

- [HTML](./README-HTML.md)
- [Ejemplo inicial de HTML](./ejemplos/inicial.html)

---

## ¿Qué es AJAX?

**AJAX** significa **Asynchronous JavaScript and XML**, aunque hoy en día ya no se limita a XML. Es una técnica que permite a las páginas web **comunicarse con servidores en segundo plano**, sin tener que recargar la página completa.

Gracias a AJAX, podemos:

- Cargar datos dinámicamente (como productos, comentarios, publicaciones).
- Enviar formularios sin recargar la página.
- Crear interfaces más rápidas e interactivas.

---

## Ejemplos

### Páginas web SIN AJAX:
- [ytmnd.com](https://ytmnd.com/)
- Lonney Toons: [https://lonneytoons.com/](https://www.spacejam.com/1996/jam.htm)

### Páginas web CON AJAX:
- [Amazon.com](https://www.amazon.com/)
- [Ebay](https://www.ebay.com/)

---

## 🛠️ ¿Cómo funciona?

AJAX permite realizar **peticiones HTTP (GET, POST, etc.)** desde el navegador al servidor. Con la llegada de la **Fetch API**, es más fácil y moderno trabajar con AJAX que con el viejo `XMLHttpRequest`.

### Ejemplo básico con `fetch`:

```javascript
fetch("https://api.ejemplo.com/datos")
  .then(response => response.json())
  .then(data => {
    console.log("Datos recibidos:", data);
  })
  .catch(error => {
    console.error("Error en la petición:", error);
  });
```

---

## 🔒 Autenticación

Algunas APIs requieren un **token de acceso** (Bearer Token). En ese caso, hay que agregarlo en los headers de la petición:

```javascript
fetch("https://api.ejemplo.com/privado", {
  method: "GET",
  headers: {
    "Authorization": "Bearer TU_TOKEN",
    "Content-Type": "application/json"
  }
})
```

---

## 🧪 ¿Cómo integrar esto en una página HTML?

Aquí un ejemplo completo de una página web que usa **AJAX con Fetch** para cargar libros desde un API REST (local o remoto). Incluye el manejo opcional de un token de acceso en los comentarios del código.

---

## 📄 Ejemplo completo

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Libros</title>
  <style>
    table {
      width: 90%;
      margin: 2rem auto;
      border-collapse: collapse;
      background: white;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    th, td {
      border: 1px solid #ccc;
      padding: 0.75rem;
      text-align: left;
    }
    th {
      background-color: #004466;
      color: white;
    }
  </style>
</head>
<body>
  <h1 style="text-align:center;">Listar todos los Libros</h1>
  <table id="tabla-libros">
    <thead>
      <tr>
        <th>Título</th>
        <th>Autor</th>
        <th>Nacionalidad</th>
        <th>Precio</th>
        <th>Stock</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>

  <script>
    const url = `http://127.0.0.1:5000/libreria/api/v1/libros`;

    /*
    // Descomentar y poner su token si el endpoint requiere autenticación:
    const token = "TU_TOKEN_AQUI";

    fetch(url, {
      method: "GET",
      headers: {
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json"
      }
    })
    */

    // Petición sin token (pública)
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        const tbody = document.querySelector("#tabla-libros tbody");
        tbody.innerHTML = ""; // Limpia la tabla

        data.forEach(libro => {
          const tr = document.createElement("tr");
          tr.innerHTML = `
            <td>${libro.titulo}</td>
            <td>${libro.autor.nombre} ${libro.autor.apellido}</td>
            <td>${libro.autor.nacionalidad}</td>
            <td>$${libro.precio}</td>
            <td>${libro.cantidad_stock}</td>
          `;
          tbody.appendChild(tr);
        });
      })
      .catch(err => {
        console.error("Error cargando libros:", err);
      });
  </script>
</body>
</html>
```

---

## Ejemplos completos

### Consumir una API REST PÚBLICA

- [Llamar API pública de DBZ](./ejemplos/ejemplo-ajax-sencillo-api-dbz/index.html)
- [Llamar API creada en el curso de librería](./ejemplos/ajax-sencillo-con-api-libros/listado.html)
- [Ejemplo completo front end llamada a API](./ejemplos/frontend-completo/index.html)
