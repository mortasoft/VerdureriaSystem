def sum(x, y):
    return x + y


credencialesDeIngreso = [{'usuario': "admin", "contraseña": "admin"}]
productos = ['Aguacate', 'Apio', 'Ayote', 'Bananos', 'Cerezas', 'Chile', 'Fresas', 'Kiwi', 'Lechuga', 'Limones', 'Maíz',
             'Manzanas', 'Naranjas', 'Papa', 'Papayas', 'Pepino', 'Plátano', 'Sandías', 'Tomates', 'Uvas', 'Zanahorias']

inventarioProductos = []
inventarioKilosProductos = []
inventarioPrecioDeCompra = []
inventarioPrecioDeVenta = []


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
        input("\nSeleccione el producto que desea trabajar: \n1.Aguacate. 2.Apio. 3.Ayote. 4.Bananos. 5.Cerezas" +
              "\n6.Chile. 7.Fresas. 8.Kiwi. 9.Lechuga. 10.Limones.\n11.Maíz. 12.Manzanas. 13.Naranjas 14.Papa 15.Papayas" +
              "\n16Pepino. 17.Plátano. 18.Sandías 19.Tomates. 20.Uvas. 21.Zanahorias"))
    opcionNombreProducto = productos[opcionProducto]
    opcionAccionPorRealizar = int(
        input("Para el producto que seleccionó ¿qué acción desea realizar?\n1. Ingreso de productos." +
              "\n2. Modificación de productos.\n3. Modificación de precios."))
    if opcionAccionPorRealizar == 1:
        ingresoDeProductos(opcionNombreProducto)
    elif opcionAccionPorRealizar == 2:
        modificacionDeInventarios(opcionNombreProducto)
    elif opcionAccionPorRealizar == 3:
        modificacionDePrecios(opcionNombreProducto)


def ingresoDeProductos(nombreProductoSeleccionado):
    global inventarioProductos
    opcionKilos = int(input("Digite: \n-¿Cuantos kilos desea añadir al inventario?"))
    opcionPrecioDeCompraDelKilo = int(input("\n-El precio de compra del kilo."))
    opcionPrecioDeVentaDelKilo = int(input("\n-El precio de venta del kilo."))
    opcionFechaDeVencimientoDelPrecioDeVenta = input(
        "\n-Para finalizar, digite la fecha de vencimiento del precio de venta")

    print(
        "El producto es: " + nombreProductoSeleccionado +
        ".\nEl nuevo inventario del producto es: " + str(opcionKilos) + ".\nEl nuevo precio de compra es: " + str(
            opcionPrecioDeCompraDelKilo) +
        ".\nEl nuevo precio de venta es: " + str(
            opcionPrecioDeVentaDelKilo) + ".\nLa fecha de vencimiento del precio de venta es: " +
        opcionFechaDeVencimientoDelPrecioDeVenta)

    nuevoProducto = {
        'producto': nombreProductoSeleccionado,
        'kilos': opcionKilos,
        'precio_compra': opcionPrecioDeCompraDelKilo,
        'precio_venta': opcionPrecioDeVentaDelKilo,
        'fecha_vencimiento': opcionFechaDeVencimientoDelPrecioDeVenta
    }
    inventarioProductos.append(nuevoProducto)
    opcionDeMantenimiento()


def modificacionDeInventarios(producto):
    global inventarioProductos
    opcion = int(input("Digite si desea: \n1.Agregar\n2.Remover"))
    if opcion == 1:
        opcionAgregar = int(input("Digite la cantidad de unidades que desea agregar: "))
        cont = 0
        for i in inventarioProductos:
            if producto == inventarioProductos[cont]['producto']:
                inv_inicial = inventarioProductos[cont]['kilos']
                inv_inicial = inv_inicial + opcionAgregar
                inventarioProductos[cont]['kilos'] = inv_inicial
                print("\nLa cantidad de este producto es: " + str(inventarioProductos[cont]['kilos']))
            cont = cont + 1
        opcionDeMantenimiento()
    elif opcion == 2:
        opcionRemover = int(input("Digite la cantidad de unidades que desea remover: "))
        cont = 0
        for i in inventarioProductos:
            if producto == inventarioProductos[cont]['producto']:
                inv_inicial = inventarioProductos[cont]['kilos']
                inv_inicial = inv_inicial - opcionRemover
                inventarioProductos[cont]['kilos'] = inv_inicial
                print("\nLa cantidad de este producto es: " + str(inventarioProductos[cont]['kilos']))
            cont = cont + 1
        opcionDeMantenimiento()
    else:
        modificacionDeInventarios(producto)


def modificacionDePrecios(producto):
    global inventarioProductos
    opcionPrecioDeCompra = int(
        input("Digite las siguiente variables a como desea que sean modificadas: \n-Precio de comora: "))
    opcionPrecioDeVenta = int(input("\n- y el precio de venta para un kilo de producto: "))
    cont = 0
    for i in inventarioProductos:
        if producto == inventarioProductos[cont]['producto']:
            inventarioProductos[cont]['precio_compra'] = opcionPrecioDeCompra
            inventarioProductos[cont]['precio_venta'] = opcionPrecioDeVenta
            print("\nEl nuevo precio del kilo de venta es: " + str(inventarioProductos[cont]['precio_venta']) +
                  "\nEL nuevo precio del kilo de compra es: " + str(inventarioProductos[cont]['precio_compra']))
        cont = cont + 1
    opcionDeMantenimiento()


# seleccionarOpciones()
opcionDeMantenimiento()
