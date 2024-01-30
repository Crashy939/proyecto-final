function mostrarRegistro() {
    const ocultarLogin = document.querySelector(".form");
    ocultarLogin.style.opacity = 0;

    setTimeout(function () {
        ocultarLogin.style.display = "none";
    }, 500); // Espera 500 milisegundos (igual a la duración de la transición)

    const mostrarReg = document.querySelector(".formRegistro");
    mostrarReg.style.display = "block";
    setTimeout(function () {
        mostrarReg.style.opacity = 1;
    }, 10); // Inicia la transición con una pequeña demora para asegurar el efecto
}

function mostrarLogin() {
    const ocultarRegistro = document.querySelector(".formRegistro");
    ocultarRegistro.style.opacity = 0;

    setTimeout(function () {
        ocultarRegistro.style.display = "none";
    }, 500); // Espera 500 milisegundos (igual a la duración de la transición)

    const mostrarLog = document.querySelector(".form");
    mostrarLog.style.display = "block";
    setTimeout(function () {
        mostrarLog.style.opacity = 1;
    }, 10); // Inicia la transición con una pequeña demora para asegurar el efecto
}
