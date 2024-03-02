<?php
$servername = "192.168.10.123";
$username = "root";
$password = "password";
$dbname = "escuela";

// Crear conexión
$conn =mysqli_connect($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
$matricula= $_POST['matricula'];
$curp= $_POST['curp'];
session_start();
$consulta="SELECT*FROM usuarios where matricula='$matricula' and curp='$curp'";
$resultado=mysqli_query($conn,$consulta);

$filas=mysqli_num_rows($resultado);

if($filas){
    header("Location: agregar_grupo.html");
}
else {
    ?>
    <?php
    include("index.html");
    ?>
    <h1 >ERROR EN LA AUTENTIFICACION</h1>
    <?php
}
mysqli_free_result($resultado);
mysqli_close($conn);
?>