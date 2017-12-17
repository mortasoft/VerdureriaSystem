import datetime


def sum(x, y):
    return x + y


credencialesDeIngreso = [{'usuario': "admin", "contraseña": "admin"}]
productos = ['Aguacate', 'Apio', 'Ayote', 'Bananos', 'Cerezas', 'Chile', 'Fresas', 'Kiwi', 'Lechuga', 'Limones', 'Maíz',
             'Manzanas', 'Naranjas', 'Papa', 'Papayas', 'Pepino', 'Plátano', 'Sandías', 'Tomates', 'Uvas', 'Zanahorias']

inventarioProductos = []
inventarioKilosProductos = []
inventarioPrecioDeCompra = []
inventarioPrecioDeVenta = []

inventarioDeCotizaciones = []
inventarioDeVentasDiarias = [{'producto': 'Aguacate', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Apio', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Ayote', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Bananos', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Cerezas', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Chile', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Fresas', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Kiwi', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Lechuga', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Limones', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Maíz', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Manzanas', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Naranjas', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Papa', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Papayas', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Pepino', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Plátano', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Sandías', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Tomates', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Uvas', 'cantidad': 0, 'valor': 0},
                             {'producto': 'Zanahorias', 'cantidad': 0, 'valor': 0}]


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
        opcion = int(input("\nSeleccione la opción deseada: \n1. Mantenimiento.\n2. Cotización.3. Venta de productos." +
                           "\n4. Informe de ventas diarias.\n5. Informe de ganancias diarias.\n6. Salir\n"))
        if opcion == 1:
            opcionDeMantenimiento()
        elif opcion == 2:
            opcionCotizacion()
        elif opcion == 3:
            opcionVentaDeProductos()
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
        input("\nPara el producto que seleccionó ¿qué acción desea realizar?\n1. Ingreso de productos." +
              "\n2. Modificación de productos.\n3. Modificación de precios."))
    if opcionAccionPorRealizar == 1:
        ingresoDeProductos(opcionNombreProducto)
    elif opcionAccionPorRealizar == 2:
        modificacionDeInventarios(opcionNombreProducto)
    elif opcionAccionPorRealizar == 3:
        modificacionDePrecios(opcionNombreProducto)


def ingresoDeProductos(nombreProductoSeleccionado):
    global inventarioProductos
    opcionKilos = int(input("\nDigite: \n-¿Cuantos kilos desea añadir al inventario?"))
    opcionPrecioDeCompraDelKilo = int(input("\n-El precio de compra del kilo."))
    opcionPrecioDeVentaDelKilo = int(input("\n-El precio de venta del kilo."))
    opcionFechaDeVencimientoDelPrecioDeVenta = input(
        "\n-Para finalizar, digite la fecha de vencimiento del precio de venta")

    print(
        "\nEl producto es: " + nombreProductoSeleccionado +
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
    seleccionarOpciones()


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
        seleccionarOpciones()
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
        seleccionarOpciones()
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
    seleccionarOpciones()


def opcionCotizacion():
    global productos, inventarioProductos
    opcionNumCotizacion = int(input("Bienvenido a la realización de la cotización.\nPor favor, digite el número de " +
                                    "cotización"))
    nombreDelCliente = input("\nDigite el nombre del cliente")
    cedulaDelCliente = int(input("\nDigite el número de cédula del cliente"))
    correoDelCliente = input("\nDigite el coreo electrónico del cliente")
    productoDeseado = int(
        input("\nSeleccione el producto que desea cotizar: \n1.Aguacate. 2.Apio. 3.Ayote. 4.Bananos. 5.Cerezas" +
              "\n6.Chile. 7.Fresas. 8.Kiwi. 9.Lechuga. 10.Limones.\n11.Maíz. 12.Manzanas. 13.Naranjas 14.Papa 15.Papayas" +
              "\n16Pepino. 17.Plátano. 18.Sandías 19.Tomates. 20.Uvas. 21.Zanahorias"))

    opcionNombreProducto = productos[productoDeseado]

    opcionKilos = int(input("\n¿Cuantos kilos desea añadir a la cotización?"))
    cont = 0
    for i in inventarioProductos:
        if opcionNombreProducto == inventarioProductos[cont]['producto']:
            precioVenta = inventarioProductos[cont]['precio_venta']
        cont = cont + 1
    totalCotizacion = opcionKilos * precioVenta
    totalCotizacionConImpuestos = (totalCotizacion * 113) / 100
    fechaExacta = datetime.datetime.now()
    print("\nVerduleria la Vencedora S.A.\nCajero: admin.\nN° Cotización: " + str(opcionNumCotizacion) + "\nFecha: " +
          str(fechaExacta) + "\nCliente: " + nombreDelCliente + "\nProducto: " + opcionNombreProducto +
          "\nKilos: " + str(opcionKilos) + "\nTotal sin impuestos: " + str(
        totalCotizacion) + "\nTotal con impuestos: " +
          str(totalCotizacionConImpuestos) + "\nEsta cotización expira en 4 días.\n")
    nuevaCotizacion = {
        'cajero': 'usuario',
        'num_cotizacion': opcionNumCotizacion,
        'fecha': fechaExacta,
        'cliente': nombreDelCliente,
        'producto': opcionNombreProducto,
        'kilos': opcionKilos,
        'total_sin_impuestos': totalCotizacion,
        'total_con_impuestos': totalCotizacionConImpuestos
    }
    inventarioDeCotizaciones.append(nuevaCotizacion)


def opcionVentaDeProductos():
    global inventarioDeCotizaciones, inventarioDeVentasDiarias, productos
    cotizacion = input("\nBienvenido a la venta de producto.\n¿Al cliente se le realizó una cotización?\n")
    if cotizacion == "si":
        numCotizacion = int(input("\nDigita el número de la cotización\n"))
        cont = 0
        for i in inventarioDeCotizaciones:
            # venta confirmada por cotizacion
            if numCotizacion == inventarioDeCotizaciones[cont]['num_cotizacion']:
                print("\nVerdulería la Vencedora S.A\nCajero: admin\nCotización número: " + str(numCotizacion) +
                      "\nFecha: " + str(datetime.datetime.now()) + "\nCliente: " +
                      inventarioDeCotizaciones[cont]['cliente'] + "\nProducto: " +
                      inventarioDeCotizaciones[cont]['producto'] + "\nKilos: " +
                      str(inventarioDeCotizaciones[cont]['kilos']) + "\nTotal sin impuestos: " +
                      str(inventarioDeCotizaciones[cont]['total_sin_impuestos']) + "\nTotal con impuestos: " +
                      str(inventarioDeCotizaciones[cont]['total_con_impuestos']) + "\nForma de pago: Efectivo.\n")
                cont2 = 0
                # actualizamos la lista de ventas dirias
                for j in inventarioDeVentasDiarias:
                    if inventarioDeCotizaciones[cont]['producto'] == inventarioDeVentasDiarias[cont2]['producto']:
                        inventarioDeVentasDiarias[cont2]['cantidad'] = inventarioDeCotizaciones[cont]['kilos']
                        inventarioDeVentasDiarias[cont2]['valor'] = inventarioDeCotizaciones[cont][
                            'total_sin_impuestos']
                    cont2 = cont2 + 1
            cont = cont + 1
    elif cotizacion == "no":
        nombreDelCliente = input("\nDigite el nombre del cliente\n")
        cedulaDelCliente = input("\nDigite la cédula del cliente\n")
        productoDeseado = int(
            input("\nSeleccione el producto que desea comprar: \n1.Aguacate. 2.Apio. 3.Ayote. 4.Bananos. 5.Cerezas" +
                  "\n6.Chile. 7.Fresas. 8.Kiwi. 9.Lechuga. 10.Limones.\n11.Maíz. 12.Manzanas. 13.Naranjas 14.Papa 15.Papayas" +
                  "\n16Pepino. 17.Plátano. 18.Sandías 19.Tomates. 20.Uvas. 21.Zanahorias"))
        global productos
        nombreProducto = productos[productoDeseado]
        cantidadDeseasa = int(input("\nDigite la cantidad de kilos para este producto " + str(nombreProducto)))

        cont = 0
        for i in inventarioProductos:
            if nombreProducto == inventarioProductos[cont]['producto']:
                precioVenta = inventarioProductos[cont]['precio_venta']
            cont = cont + 1
        totalCompra = cantidadDeseasa * precioVenta
        totalCompraConImpuesto = (totalCompra * 113) / 100
        print("\nVerdulería la Vencedora S.A\nCajero: admin." +
              "\nFecha: " + str(datetime.datetime.now()) + "\nCliente: " + nombreDelCliente + "\nProducto: " +
              str(nombreProducto) + "\nKilos: " + str(cantidadDeseasa) + "\nTotal sin impuestos: " + str(totalCompra) +
              "\nTotal con impuestos: " + str(totalCompraConImpuesto) + "\nForma de pago: Efectivo.\n")
        cont2 = 0
        # actualizamos la lista de ventas dirias
        for j in inventarioDeVentasDiarias:
            if nombreProducto == inventarioDeVentasDiarias[cont2]['producto']:
                inventarioDeVentasDiarias[cont2]['cantidad'] = cantidadDeseasa
                inventarioDeVentasDiarias[cont2]['valor'] = totalCompra
            cont2 = cont2 + 1

    else:
        opcionVentaDeProductos()


# seleccionarOpciones()
opcionDeMantenimiento()
