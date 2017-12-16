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
    opcion = 0
    while opcion != 6:
        opcion = int(input("Seleccione la opción deseada: \n1. Mantenimiento.\n2. Cotización.3. Venta de productos." +
                           "\n4. Informe de ventas diarias.\n5. Informe de ganancias diarias.\n6. Salir"))
        if opcion == 1:
            print("mantenimiento")
            return "mantenimiento"
        elif opcion == 2:
            print("cotizacion")
            return "cotizacion"
        elif opcion == 3:
            return "venta de productos"
        elif opcion == 4:
            return "informe de ventas diarias"
        elif opcion == 5:
            return "informe de ganancias diarias"
        elif opcion == 6:
            return "salir"


seleccionarOpciones()
