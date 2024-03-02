<?php
// Conexión a la base de datos (debes completar con tus propios datos de conexión)
$servername = "192.168.10.123";
$username = "root";
$password = "password";
$dbname = "escuela";

// Crear conexión
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    echo("Conexión fallida: " . $conn->connect_error);
}

// Recibir datos del formulario
$nombre = $_POST['nombre'];
$matricula = $_POST['matricula'];
$apellido_paterno = $_POST['apellido_paterno'];
$apellido_materno = $_POST['apellido_materno'];
$fecha_nacimiento = $_POST['fecha_nacimiento'];
$rfid = $_POST['rfid'];
$carrera = $_POST['carrera'];
$semestre = $_POST['semestre'];
$grupo = $_POST['grupo'];
$correo_electronico = $_POST['correo_electronico'];
$grupo_id = $_POST['grupo_id'];

// Preparar la consulta SQL para insertar los datos en la tabla de alumnos
$sql = "INSERT INTO alumnos (nombre, matricula, ap_paterno, ap_materno, fecha_nac, rfid, carrera, semestre, grupo, correo_elec, id_grupo) VALUES ('$nombre', '$matricula', '$apellido_paterno', '$apellido_materno', '$fecha_nacimiento', '$rfid', '$carrera', '$semestre', '$grupo', '$correo_electronico', '$grupo_id')";
$resultado = mysqli_query($conn,$sql);
// Ejecutar la consulta y verificar si fue exitosa
if ($resultado) {
    echo '<script language="javascript">alert("Registro hecho correctamente");</script>';
    header("Location: agregar_alumno.html");
    
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Cerrar conexión
$conn->close();
?>
