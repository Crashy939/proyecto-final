document.addEventListener('DOMContentLoaded', function () {
    // Importante obtener estos datos de la base de datos
    const asistenciaAlumno = {
        '2023-03-05': 'asistio',
        '2023-03-29': 'ausente',
        // Solamente es un ejemplo de cómo se vería la asistencia
    };

    const contenedorApp = document.getElementById('app');

    // Función para generar el calendario
    function generarCalendario() {
        const contenedorCalendario = document.createElement('div');
        contenedorCalendario.classList.add('calendar');

        const fechaInicio = new Date('2023-03-01');
        const fechaFin = new Date('2023-03-31');

        while (fechaInicio <= fechaFin) {
            const stringFecha = fechaInicio.toISOString().split('T')[0];
            const contenedorDia = document.createElement('div');
            contenedorDia.classList.add('day');

            const numeroDia = fechaInicio.getDate();
            contenedorDia.innerText = numeroDia;

            // Verificar la asistencia y aplicar estilo
            if (asistenciaAlumno[stringFecha] === 'asistio') {
                contenedorDia.classList.add('attended');
            } else if (asistenciaAlumno[stringFecha] === 'ausente') {
                contenedorDia.classList.add('absent');
            }

            contenedorCalendario.appendChild(contenedorDia);
            fechaInicio.setDate(fechaInicio.getDate() + 1);
        }

        contenedorApp.appendChild(contenedorCalendario);
    }

    // Llamada a la función para generar el calendario
    generarCalendario();
});
