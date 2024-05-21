const $formularioAnimales = document.getElementById('FomrularioAnimales');
const $txtNombre = document.getElementById('txtNombre');
const $txtRaza = document.getElementById('txtRaza'); 
const $txtEstadoSalud = document.getElementById('txtEstadoSalud'); 
const $txtUbicacion = document.getElementById('txtUbicacion');   

(function(){
    $formularioAnimales.addEventListener('submit', function(e){
        let nombre = String($txtNombre.value).trim();
        let raza = String($txtRaza.value).trim();
        let estadoSalud = String($txtEstadoSalud.value).trim();
        let ubicacion = String($txtUbicacion.value).trim();
        if (nombre.length === 0) {
            alert('El nombre no puede estar vacio');
            e.preventDefault();
            return;
        }
        if (raza.length === 0) {
            alert('La raza no puede estar vacia');
            e.preventDefault();
            return;
        }
        if (estadoSalud.length === 0) {
            alert('El estado de salud no puede estar vacio');
            e.preventDefault();
            return;
        }
        if (ubicacion.length === 0) {
            alert('La ubicacion no puede estar vacia');
            e.preventDefault();
            return;
        }
        
    });
})();