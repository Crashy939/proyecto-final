<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <?php
        // Obtener los datos del formulario
        $alumno_id = $_POST['alumno_id'];
        $fecha = $_POST['fecha'];
        
        // Conexión a la base de datos (asumiendo que ya tienes una conexión establecida)
        $conexion = mysqli_connect("localhost", "usuario", "contraseña", "basededatos");

        // Consulta SQL
        $consulta = "SELECT * FROM tabla WHERE alumno_id = '$alumno_id' AND fecha = '$fecha'";
        
        // Ejecutar consulta
        $resultado = mysqli_query($conexion, $consulta);

        // Mostrar resultados en una tabla
        echo "<table>";
        echo "<tr><th>ID Alumno</th><th>Fecha</th><th>Otro Campo</th></tr>";
        while($fila = mysqli_fetch_assoc($resultado)) {
            echo "<tr><td>".$fila['alumno_id']."</td><td>".$fila['fecha']."</td><td>".$fila['otro_campo']."</td></tr>";
        }
        echo "</table>";

        // Cerrar conexión
        mysqli_close($conexion);
    ?>
</body>
</html>
