const $formularioAliado = document.getElementById('formularioAliado');
const $txtNombre = document.getElementById('txtNombre');
const $txtCorreo = document.getElementById('txtCorreo'); 
const $tipoServicios = document.getElementById('tipoServicios');
const $Contraseña = document.getElementById('Contraseña');   
const $Telefono = document.getElementById('Telefono');   

(function(){
    $formularioAliado.addEventListener('submit', function(e){
        let nombre = String($txtNombre.value).trim();
        let correo = String($txtCorreo.value).trim();
        let tipoServicios = String($tipoServicios.value).trim();
        let Contraseña = String($Contraseña.value).trim();
        let Telefono = String($Telefono.value).trim();
        if (nombre.length === 0) {
            alert('Debes ingresar un nombre');
            e.preventDefault();
        }
        if (correo.length === 0) {
            alert('Debes ingresar un correo');
            e.preventDefault();
        }
        if (tipoServicios.length === 0) {
            alert('Debes ingresar un tipo de servicio');
            e.preventDefault();
        }
        if (Contraseña.length === 0) {
            alert('Debes ingresar una contraseña');
            e.preventDefault();
        }
        if (Telefono.length === 0) {
            alert('Debes ingresar un telefono');
            e.preventDefault();
        }
    });
})();