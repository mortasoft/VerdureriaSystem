def sum(x, y):
    return x + y


credencialesDeIngreso = [{'usuario': "admin", "contraseña": "admin"}]


def ingresoAlSistema():
    global credencialesDeIngreso
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    validarUsuario = [credencialesDeIngreso for credencialesDeIngreso in credencialesDeIngreso if
                      credencialesDeIngreso['usuario'] == usuario]
    validarContraseña = [credencialesDeIngreso for credencialesDeIngreso in credencialesDeIngreso if
                         credencialesDeIngreso['contraseña'] == contraseña]
    if len(validarUsuario) == 0 or len(validarContraseña) == 0:
        print("Su usuario o contraseña es incorrecto, por favor intente de nuevo")
        return "invalido"
    else:
        print("bueno")
        return "loggeado"
        # LUEGO DEBEMOS LLAMAR AL METODO DE OPCIONES...


def seleccionarOpciones():
    opcion = int(input("Seleccione la opción deseada: "))

