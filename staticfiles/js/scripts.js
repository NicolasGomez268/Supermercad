// Aquí puedes agregar lógica JavaScript si es necesario 

function filtrarProductos(categoria) {
    const url = new URL(window.location.href);
    url.searchParams.set('filtro', categoria);
    window.location.href = url.toString();
} 