const objetivo = document.querySelector(".objetivo");
const parrafoObjetivo = document.querySelector(".objetivo-p");
const flechaAbajo = document.getElementById("flechaAbajo");
objetivo.addEventListener("click", ()=>{
    if(parrafoObjetivo.style.display === "none" || parrafoObjetivo.style.display === ""){
        parrafoObjetivo.style.display = "block";
        flechaAbajo.style.transform = "rotate(-90deg)";
    } else{
        parrafoObjetivo.style.display = "none";
        flechaAbajo.style.transform = "rotate(0deg)"
    }
});