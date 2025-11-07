''' 
AVANCE 2: Sistema de citas y facturación de clínica odontológica
Estudiante: K. Andrés Baltodano Ramírez
Facultad de Ingeniería, Universidad Fidélitas
SC-115: Programación Básica
Profesores: Javier Montoya, Edward Jiménez
Noviembre, 2025
'''

''' 
Función/Módulo #0: Login. Se valida el usuario y se manejan los datos de los encargados con acceso a la aplicación.
'''
def login():
    '''
    Credenciales de acceso USUARIO 1
    ---------------
    Usuario : admin
    Contraseña : 1234

    Credenciales de acceso USUARIO 2
    ---------------
    Usuario : user
    Contraseña : 0000
    '''

    usuarioPrincipal = "admin"
    clavePrincipal = "1234"
    usuarioSecundario = "user"
    claveSecundaria = "0000"

    '''
    Se definen 3 intentos de acceso como máximo. En caso de exceder intentos el programa se termina
    0 = acceso denegado
    1 = acceso concedido
    '''
    intentos = 3
    acceso = 0

    while intentos > 0 and acceso != 1:
        # Mensaje de bienvenida y solicitud de credenciales
        print("Bienvenido al sistema, por favor escriba sus credenciales: ")
        inputUsuario = input("Escriba su usuario: ")
        inputClave = input("Escriba su contraseña: ")
        if ((inputUsuario == usuarioPrincipal) and (inputClave == clavePrincipal)) or ((inputUsuario == usuarioSecundario) and (inputClave == claveSecundaria)):
            acceso = 1
            print("Acceso concedido.")
        else:
            intentos -= 1 # restar un intento para respetar el límite
            print("Usuario y/o contraseña incorrecto(s): Quedan ", intentos, " intentos")
    
    # Mostrar mensaje de salida si se exceden los intentos
    if intentos == 0:
        print("Ha excedido el número de intentos permitidos. Saliendo del programa.")
    return acceso

''' 
Función/Módulo #1: Registro de clientes. Se registran los datos del cliente.
'''
def registroClientes(listaClientes):
    print("\nRegistro de clientes: seleccione una opción del menú")
    print("1. Registrar cliente | 0. Volver al menú anterior")
    inputClientes = input("\nSeleccione una opción del menú: ")
    while True:
        if inputClientes == "0":
            break
        if inputClientes == "1":
            #recoger datos del cliente
            nombreCliente = input("Escriba el nombre del cliente: ")
            cedulaCliente = input("Escriba la cédula del cliente: ")
            celularCliente = input("Escriba el número de celular del cliente: ")
            correoCliente = input("Escriba el correo electrónico del cliente: ")
            direccionCliente = input("Escriba la dirección del cliente: ")
            # concatenar datos de clientes en una nueva variable para agregar a la lista
            nuevoCliente = "\nNombre: " + nombreCliente + " Cédula: " + cedulaCliente + " Celular: " + celularCliente + " Correo: " + correoCliente + " Dirección: " + direccionCliente
            listaClientes += nuevoCliente
            # confirmar que el cliente ha sido registrado y sus datos guardados
            print(f"Clientes registrados: {listaClientes}")
            print("1. Registrar cliente | 0. Volver al menú anterior")
            inputClientes = input("\nSeleccione una opción del menú: ")
    return listaClientes

''' 
Función/Módulo #2: Venta de paquetes. Se definen 4 paquetes de venta con su costo. 
'''
def paquetes(paqueteSeleccionado, subtotalPaquetes):
    # definir los paquetes y sus precios
    paqueteClean = "Paquete CLEAN: Valoración y Limpieza"
    precioClean = 50000
    paqueteSilver = "Paquete SILVER: Limpieza y Blanqueamiento"
    precioSilver = 100000
    paqueteGold = "Paquete GOLD: Valoración, Limpieza y Blanqueamiento"
    precioGold = 140000
    paqueteDiamante = "Paquete DIAMANTE: Valoración, Placas, Limpieza y Blanqueamiento"
    precioDiamante = 200000
    
    while True:
        print("\nConsulta de paquetes: seleccione una opción del menú")
        print(f"Paquetes disponibles:\n1. {paqueteClean} | Precio: ₡{precioClean}\n2. {paqueteSilver} | Precio: ₡{precioSilver}\n3. {paqueteGold} | Precio: ₡{precioGold}\n4. {paqueteDiamante} | Precio: ₡{precioDiamante}\n0. Volver al menú anterior")
        #print("Seleccione el paquete que desea comprar: 1. CLEAN | 2. SILVER | 3. GOLD | 4. DIAMANTE | 0. Volver al menú anterior")
        inputPaquete = input("\nSeleccione el paquete que desea comprar: ")
        # Salir del módulo
        if inputPaquete == "0":
            break
        # Sólo un paquete por cliente, no tiene sentido que compra varios paquetes a la vez
        elif inputPaquete == "1":
            paqueteSeleccionado = paqueteClean 
            subtotalPaquetes = precioClean
            # Confirmar selección y subtotal de paquete seleccionado
            print(f"Paquete seleccionado: {paqueteSeleccionado} | Subtotal: ₡{subtotalPaquetes}.")
            break
        elif inputPaquete == "2":
            paqueteSeleccionado = paqueteSilver
            subtotalPaquetes = precioSilver
            print(f"Paquete seleccionado: {paqueteSeleccionado} | Subtotal: ₡{subtotalPaquetes}.")
            break
        elif inputPaquete == "3":
            paqueteSeleccionado = paqueteGold
            subtotalPaquetes = precioGold
            print(f"Paquete seleccionado: {paqueteSeleccionado} | Subtotal: ₡{subtotalPaquetes}.")
            break
        elif inputPaquete == "4":
            paqueteSeleccionado = paqueteDiamante
            subtotalPaquetes = precioDiamante
            print(f"Paquete seleccionado: {paqueteSeleccionado} | Subtotal: ₡{subtotalPaquetes}.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del menú.")
    return paqueteSeleccionado, subtotalPaquetes

''' 
Función/Módulo #3: Citas / Horario de atención. Se definen 3 opciones según preferencia del cliente. 
'''
def citas(citaSeleccionada):
    # Definir citas disponibles
    citaManana = "Cita Mañana: 8am a 11am"
    citaTarde = "Cita Tarde: 2pm a 5pm"
    citaNoche = "Cita Noche: 6pm a 9pm"

    while True:
        print("\nConsulta de citas: seleccione una opción del menú")
        print(f"Citas disponibles:\n1. {citaManana}\n2. {citaTarde}\n3. {citaNoche}\n0. Volver al menú anterior")
        inputCita = input("\nSeleccione la cita que desea agendar: ")
        # Salir del módulo
        if inputCita == "0":
            break
        elif inputCita == "1":
            citaSeleccionada = citaManana
            # Confirmar selección de cita
            print(f"Cita seleccionada: {citaSeleccionada}.")
            break
        elif inputCita == "2":
            citaSeleccionada = citaTarde
            print(f"Cita seleccionada: {citaSeleccionada}.")
            break
        elif inputCita == "3":
            citaSeleccionada = citaNoche
            print(f"Cita seleccionada: {citaSeleccionada}.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del menú.")
    return citaSeleccionada

''' 
Función/Módulo #4: Productos. Se definen 5 productos con el precio de cada uno.
Por la naturaleza de los productos/servicios, algunos no deberían poder ser agregados más de una vez.
'''
def productos(productoSeleccionado, subtotalProductos):
    # Definir productos disponibles. 
    # Valoración, limpieza, placas, blanqueamiento no deberían poder ser agregados más de una vez. Se controla inicializando banderas en false.
    valoracion = "Valoración"
    precioValoracion = 25000
    valoracionAgregado = False
    limpieza = "Limpieza dental"
    precioLimpieza = 40000
    limpiezaAgregada = False
    placas = "Placas / Radiografías"
    precioPlacas = 30000
    placasAgregada = False
    blanqueamiento = "Blanqueamiento dental"
    precioBlanqueamiento = 100000
    blanqueamientoAgregado = False
    calza = "Calza(s) / relleno(s) dental(es)"
    precioCalza = 15000

    while True:
        print("\nConsulta de productos: seleccione una opción del menú")
        print(f"Productos disponibles:\n1. {valoracion} Precio: ₡{precioValoracion}\n2. {limpieza} Precio: ₡{precioLimpieza}\n3. {placas} Precio: ₡{precioPlacas}\n4. {blanqueamiento} Precio: ₡{precioBlanqueamiento}\n5. {calza} Precio: ₡{precioCalza}\n0. Volver al menú anterior")
        inputProducto = input("\nSeleccione el producto que desea comprar: ")

        # Salir del módulo
        if inputProducto == "0":
            break

        elif inputProducto == "1": # Valoración
            # Omitir si la valoración ya fue agregada
            if valoracionAgregado:
                print("La valoración ya ha sido agregada previamente.")
                continue
            productoSeleccionado += "\n" + valoracion
            valoracionAgregado = True # Marcar que la valoración ha sido agregada
            subtotalProductos += precioValoracion
            # Confirmar selección de producto y mostrar proforma actualizada
            print(f"Producto seleccionado: \n{valoracion} - Precio: ₡{precioValoracion}")
            print(f"--------PROFORMA-------- {productoSeleccionado} \nSubtotal: ₡{subtotalProductos}")
        
        elif inputProducto == "2": # Limpieza dental
            if limpiezaAgregada:
                print("La limpieza dental ya ha sido agregada previamente.")
                continue
            productoSeleccionado += "\n" + limpieza
            limpiezaAgregada = True
            subtotalProductos += precioLimpieza
            print(f"Producto seleccionado: \n{limpieza} - Precio: ₡{precioLimpieza}")
            print(f"--------PROFORMA-------- {productoSeleccionado} \nSubtotal: ₡{subtotalProductos}")
        
        elif inputProducto == "3": # Placas / Radiografías
            if placasAgregada:
                print("Las placas / radiografías ya han sido agregadas previamente.")
                continue
            productoSeleccionado += "\n" + placas
            placasAgregada = True
            subtotalProductos += precioPlacas
            print(f"Producto seleccionado: \n{placas} - Precio: ₡{precioPlacas}")
            print(f"--------PROFORMA-------- {productoSeleccionado} \nSubtotal: ₡{subtotalProductos}")
        
        elif inputProducto == "4": # Blanqueamiento dental
            if blanqueamientoAgregado:
                print("El blanqueamiento dental ya ha sido agregado previamente.")
                continue
            productoSeleccionado += "\n" + blanqueamiento
            blanqueamientoAgregado = True
            subtotalProductos += precioBlanqueamiento
            print(f"Producto seleccionado: \n{blanqueamiento} - Precio: ₡{precioBlanqueamiento}")
            print(f"--------PROFORMA-------- {productoSeleccionado} \nSubtotal: ₡{subtotalProductos}")
        
            # Calzas dentales: Único producto que puede ser agregado múltiples veces
        elif inputProducto == "5":
            cantidadCalzas = int(input("Ingrese la cantidad de calzas: "))
            # Validar que no se digite un número negativo o cero
            if cantidadCalzas <= 0:
                print("Cantidad no válida, por favor ingrese un número positivo.")
                continue
            productoSeleccionado += "\n" + str(cantidadCalzas) + " " + calza
            subtotalProductos += (cantidadCalzas * precioCalza)
            print(f"Producto seleccionado: \n{cantidadCalzas} {calza} - Precio: ₡{cantidadCalzas * precioCalza}")
            print(f"--------PROFORMA-------- {productoSeleccionado} \nSubtotal: ₡{subtotalProductos}")
        else:
            print("Opción no válida, por favor seleccione una opción del menú.")

        # Opción para agregar otro producto
        print("\n1. Agregar un producto | 0. Volver al menú anterior")
        inputClientes = input("Seleccione una opción del menú: ")
        if inputClientes == "0":
            break
        if inputClientes == "1":
            continue
        else:
            print("Opción no válida, por favor seleccione una opción del menú.")
            break

    return productoSeleccionado, subtotalProductos

''' 
Función/Módulo #5: Historial. Se muestra información que se capuró en los módulos anteriores.
'''
def historial(listaClientes, paqueteSeleccionado, citaSeleccionada, productoSeleccionado, subtotalPaquetes, subtotalProductos):
    # Mostrar detalle de clientes
    if listaClientes == "":
        print("Aún no hay clientes registrados.")
    else: 
        print("Lista de clientes: ", listaClientes)
    
    # Mostrar detalle de paquetes
    if paqueteSeleccionado == "":
        print("Aún no se ha seleccionado ningún paquete.")
    else:
        print("Paquete(s) seleccionado(s): ", paqueteSeleccionado)
    
    # Mostrar detalle de subtotal de paquetes
    if subtotalPaquetes == 0:
        print("No existen cargos por paquetes.")
    else:
        print("Subtotal Paquetes: ₡", subtotalPaquetes)
    
    # Mostrar detalle de citas
    if citaSeleccionada == "":
        print("Aún no se ha seleccionado ninguna cita.")
    else:
        print("Cita seleccionada: ", citaSeleccionada)
    
    # Mostrar detalle de productos
    if productoSeleccionado == "":
        print("Aún no se han seleccionado productos.")
    else:
        print("Producto(s) seleccionado(s): ", productoSeleccionado)

    # Mostrar detalle de subtotal de productos
    if subtotalProductos == 0:
        print("No existen cargos por productos.")
    else:
        print("Subtotal por productos: ₡", subtotalProductos)

    return listaClientes, paqueteSeleccionado, citaSeleccionada, productoSeleccionado, subtotalPaquetes, subtotalProductos

''' 
Función/Módulo #6: Facturación. Se muestra una factura con los datos del cliente y los productos/paquetes seleccionados.
'''
def facturar(paqueteSeleccionado, productoSeleccionado, subtotalPaquetes, subtotalProductos):
    # Si no hay productos o paquetes seleccionados, no se puede facturar
    if paqueteSeleccionado == "" and productoSeleccionado == "":
        print("No hay productos o paquetes para facturar.")
        return paqueteSeleccionado, productoSeleccionado, subtotalPaquetes, subtotalProductos
    # Solicitar datos para facturación, podrían ser diferentes a los del cliente registrado
    nombreCliente = input("Escriba nombre para facturación: ")
    cedulaCliente = input("Escriba cédula para facturación: ")
    correoCliente = input("Escriba correo electrónico para facturación: ")
    # Consultar descuento a aplicar
    descuentoFactura = float(input("Descuento a aplicar (%): "))
    print("****FACTURA****")
    print("Cliente: ", nombreCliente)
    print("Cédula: ", cedulaCliente)    
    print("Correo electrónico: ", correoCliente)    
    print("Descripción: ", paqueteSeleccionado, productoSeleccionado)
    # Calcular subtotal general
    subtotal = subtotalPaquetes + subtotalProductos
    print("Subtotal: ₡", subtotal)
    # Validar y calcular descuento
    if descuentoFactura < 0 or descuentoFactura > 100:
        print("Descuento no válido, se aplicará un 0% de descuento.")
        descuentoFactura = 0
    descuento = subtotal * (descuentoFactura / 100)
    print(f"Descuento: ₡ {descuento:.2f} ({descuentoFactura:.2f}%)") #2f: solo mostrar dos decimales
    # Calcular impuesto, 4% de IVA para servicios dentales
    impuesto = (subtotal - descuento) * 0.04
    print(f"IVA (4%): ₡ {impuesto:.2f}")
    # Calcular total a pagar
    totalPagar = subtotal - descuento + impuesto
    print(f"Total a pagar: ₡ {totalPagar:.2f}")
    print("****GRACIAS POR SU COMPRA****")

    return paqueteSeleccionado, productoSeleccionado, subtotalPaquetes, subtotalProductos

''' 
ESTRUCTURA PRINCIPAL DEL PROGRAMA
Sistema de citas y facturación de clínica odontológica
'''

# Inicio del programa solo tras validar credenciales
if login() == 1: #1: acceso concedido
    print("Bienvenido al sistema")
    
    # definir variables que pueden cambiar a lo largo del programa, para mostrarlas luego en el módulo de historial y facturación.
    listaClientes = ""
    paqueteSeleccionado = ""
    citaSeleccionada = ""
    productoSeleccionado = ""
    subtotalPaquetes = 0
    subtotalProductos = 0
    
    while True:
        print("\nMenú principal")    
        print("1. Registro de clientes | 2. Paquetes | 3. Citas | 4. Productos | 5. Historial | 6. Facturar | 0. Salir del programa")
        inputMenu = input("\nSeleccione una opción del menú: ")
        #Módulo: Registro de clientes
        if inputMenu == "1":
            listaClientes = registroClientes(listaClientes)
        #Módulo:Paquetes
        elif inputMenu == "2":
            paqueteSeleccionado, subtotalPaquetes = paquetes(paqueteSeleccionado, subtotalPaquetes)
        #Módulo:Citas
        elif inputMenu == "3":
            citaSeleccionada = citas(citaSeleccionada)
        #Módulo:Productos
        elif inputMenu == "4":
            productoSeleccionado, subtotalProductos = productos(productoSeleccionado, subtotalProductos)
        #Módulo:Historial
        elif inputMenu == "5":
            listaClientes, paqueteSeleccionado, citaSeleccionada, productoSeleccionado, subtotalPaquetes, subtotalProductos = historial(listaClientes, paqueteSeleccionado, citaSeleccionada, productoSeleccionado, subtotalPaquetes, subtotalProductos)
        #Módulo:Facturar
        elif inputMenu == "6":
            paqueteSeleccionado, productoSeleccionado, subtotalPaquetes, subtotalProductos = facturar(paqueteSeleccionado, productoSeleccionado, subtotalPaquetes, subtotalProductos)
        #Salir del programa
        elif inputMenu == "0":
            print("Gracias por usar el sistema. Hasta la próxima. ")
            break
        #Validar opción seleccionada
        else:
            print("Opción no válida, por favor seleccione una opción del menú.")