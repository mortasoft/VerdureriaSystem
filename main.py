def sum(x, y):
    return x + y


credencialesDeIngreso = [{'usuario': "admin", "contraseña": "admin"}]
productos = ['Aguacate', 'Apio', 'Ayote', 'Bananos', 'Cerezas', 'Chile', 'Fresas', 'Kiwi', 'Lechuga', 'Limones', 'Maíz',
             'Manzanas', 'Naranjas', 'Papa', 'Papayas', 'Pepino', 'Plátano', 'Sandías', 'Tomates', 'Uvas', 'Zanahorias']
inventario = []


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
            opcionDeMantenimiento()
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


def opcionDeMantenimiento():
    global productos
    opcionProducto = int(
        input("Seleccione el producto que desea trabajar: \n1.Aguacate. 2.Apio. 3.Ayote. 4.Bananos. 5.Cerezas" +
              "\n6.Chile. 7.Fresas. 8.Kiwi. 9.Lechuga. 10.Limones.\n11.Maíz. 12.Manzanas. 13.Naranjas 14.Papa 15.Papayas" +
              "\n16Pepino. 17.Plátano. 18.Sandías 19.Tomates. 20.Uvas. 21.Zanahorias"))
    opcionProducto = productos[opcionProducto]
    opcionAccionPorRealizar = int(
        input("Para el producto que seleccionó ¿qué acción desea realizar?\n1. Ingreso de productos." +
              "\n2. Modificación de productos.\n3. Modificación de precios."))
    if opcionAccionPorRealizar == 1:
        ingresoDeProductos(opcionProducto)
        # print("prod " + str(opcionProducto) + " accion " + str(opcionAccionPorRealizar))
    elif opcionAccionPorRealizar == 2:
        modificacionDeProductos(opcionProducto)
        # print("prod " + str(opcionProducto) + " accion " + str(opcionAccionPorRealizar))
    elif opcionAccionPorRealizar == 3:
        modificacionDePrecios(opcionProducto)
        # print("prod " + str(opcionProducto) + " accion " + str(opcionAccionPorRealizar))


def ingresoDeProductos(productoSeleccionado):
    opcionKilos = int(input("Digite: \n-¿Cuantos kilos desea añadir al inventario?"))
    opcionPrecioDeCompraDelKilo = int(input("\n-El precio de compra del kilo."))
    opcionPrecioDeVentaDelKilo = int(input("\n-El precio de venta del kilo."))
    opcionFechaDeVencimientoDelPrecioDeVenta = input(
        "\n-Para finalizar, digite la fecha de vencimiento del precio de venta")

    productoNuevo = {'nombre': productoSeleccionado,
                     "kilos": opcionKilos,
                     "precio_de_compra": opcionPrecioDeCompraDelKilo,
                     "precio_de_venta": opcionPrecioDeVentaDelKilo,
                     'fecha_vencimiento': opcionFechaDeVencimientoDelPrecioDeVenta}
    print(productoNuevo)
    return productoNuevo


def modificacionDeProductos(producto):
    return None


def modificacionDePrecios(producto):
    return None

# seleccionarOpciones()
#opcionDeMantenimiento()
