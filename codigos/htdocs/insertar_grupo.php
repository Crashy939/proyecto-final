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
    die("Conexión fallida: " . $conn->connect_error);
}

// Recibir datos del formulario
$id_grupo = $_POST['id_grupo'];
$carrera = $_POST['carrera'];
$semestre = $_POST['semestre'];
$turno = $_POST['turno'];

// Preparar la consulta SQL para insertar los datos en la tabla de grupos
$sql = "INSERT INTO grupos (id_grupo, carrera, semestre, turno) VALUES ('$id_grupo', '$carrera', '$semestre', '$turno')";

// Ejecutar la consulta y verificar si fue exitosa
if ($conn->query($sql) === TRUE) {
    echo '<script>alert("Registro hecho correctamente");</script>';
    header("Location: agregar_grupo.html");
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Cerrar conexión
$conn->close();
?>
