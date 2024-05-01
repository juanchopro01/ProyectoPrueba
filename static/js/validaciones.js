
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("form").addEventListener("submit", function(event) {
        var username = document.querySelector("#id_username").value.trim();
        var email = document.querySelector("#id_email").value.trim();
        var password1 = document.querySelector("#id_password1").value.trim();
        var password2 = document.querySelector("#id_password2").value.trim();
        var errors = [];

        // validacion del nombre ususario
        if (username.length < 5 || username.length > 20) {
            errors.push("el usuario debe tener entre minimo 5 caracteres y maximo.");
        }

        // validacion para verificar que se ingrese un formato correcto de correo electronico
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            errors.push("ingresa un correo electrónico que tenga formato vlido.");
        }

        // validacion para una contraseña segura con obligatoriamente una mayuscula, una minuscula, un umero y un caracter especial
        var passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$/;
        if (!passwordRegex.test(password1)) {
            errors.push("la contraseña debe contener minimo una letra mayiscula, una minuscula, un numero y un caracter especial.");
        }

        // validacion para que no se pueda ingresar una contraseña igual al nombre de usuario
        if (password1.toLowerCase().includes(username.toLowerCase())) {
            errors.push("La contraseña no puede ser igual al nombre de usuario.");
        }

        // validacion para la confirmacion de contraseña
        if (password1 !== password2) {
            errors.push("Las contraseñas no coinciden.");
        }

        // utilizar las alertas sweet alert
        if (errors.length > 0) {
            event.preventDefault();
            var errorMessage = errors.join("<br>");
            Swal.fire({
                icon: 'error',
                title: 'Oops..',
                html: errorMessage,
            });
        }
    });
});
