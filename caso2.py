'''
ESTUDIO DE CASO 2: Gestión de inventario de una tienda de artículos deportivos
Estudiante: K. Andrés Baltodano Ramírez
Facultad de Ingeniería, Universidad Fidélitas
SC-115: Programación Básica
Profesores: Edward Jiménez, Mariela Ugalde
Diciembre, 2025
'''

'''
MÓDULO 1: Registro de productos
Función que permite ingresar los datos del inventario.
'''

def registro(listaProductos, detalleProductos):
    print("\nREGISTRO DE PRODUCTOS") 
    print("\nSeleccione una opción del menú")
    print("1. Registrar productos | 0. Volver al menú anterior")
    inputProductos = input("\nSeleccione una opción del menú: ")
    while True:
        if inputProductos == "0": # 0. Volver al menú anterior
            break
        if inputProductos == "1":
            # Solicitar nombre del producto y validar que no esté vacío
            nombreProducto = input("Escriba el nombre del producto: ")
            if nombreProducto == "":
                print("El nombre del producto no puede estar vacío, por favor intente nuevamente.")
                return
            
            # Solicitar cantidad inicial del producto y validar que no esté vacío ni sea negativa
            inputCantidad = input("Escriba la cantidad inicial del producto: ") # Todavía no convertir a entero para poder validar si está vacío
            if inputCantidad == "":
                print("La cantidad no puede estar vacía, por favor intente nuevamente.")
                return
            cantidad = int(inputCantidad) # Ahora sí convertir a entero
            if cantidad < 0:
                print("La cantidad no puede ser negativa, por favor intente nuevamente.")
                return
            
            # Solicitar precio unitario del producto y validar que no esté vacío ni sea negativo
            inputPrecio = input("Escriba el precio unitario del producto: ")
            if inputPrecio == "": 
                print("El precio no puede estar vacío, por favor intente nuevamente.")
                return
            precio = float(inputPrecio)
            if precio < 0:
                print("El precio no puede ser negativo, por favor intente nuevamente.")
                return
            
            # Si no hubo errores, almacenar datos
            listaProductos.append(nombreProducto) # Agregar producto a la lista
            producto = [cantidad, precio] # Guardar cantidad y precio en una lista para agregarla a la lista madre
            detalleProductos.append(producto)
                    
            # Confirmar datos guardados
            print(f"\nNombre del producto: {nombreProducto}")
            print(f"Cantidad en inventario: {cantidad}")
            print(f"Precio unitario: {MONEDA}{precio}")
                    
            # Opción para agregar otro producto
            print("\n1. Registrar otro producto \n0. Volver al menú principal")
            inputProductos = input("\nSeleccione una opción: ")

        else: # Validar opción seleccionada
            print("Opción no válida, por favor intente nuevamente.")
            return
            
    return listaProductos, detalleProductos

'''
MÓDULO 2: Consultar inventario
Función que muestra el nombre, cantidad y precio de cada producto.
'''

def inventario(listaProductos, detalleProductos):
    if len(listaProductos) == 0: # No proceder si aún no hay productos. Usamos len() en vez de la bandera que se definió inicialmente en el diagrama de flujo
        print("\nAún no se han registrado productos. Volviendo al menú principal")
        return

    print("\nCONSULTA DE INVENTARIO") 
    print("\nProductos disponibles:") 

    for i in range(len(listaProductos)): # Recorrer la lista de productos
        print(f"\nID del producto: [[{i+1}]]") # Para mostrar el ID de producto, sumamos 1 para que inicie en 1 y no en 0
        print(f"Nombre del producto: {listaProductos[i]}")
        print(f"Cantidad en inventario: {detalleProductos[i] [0]}") # Cantidad está en la posición [i][0] del arreglo
        print(f"Precio unitario: {MONEDA}{detalleProductos[i] [1]}") # Precio está en la posición [i][1] del arreglo

'''
MÓDULO 3: Registro de ventas
Función que permite a la persona usuaria seleccionar un producto y la cantidad por vender,
actualizando el inventario si hay suficiente stock.
'''

def ventas(listaProductos, detalleProductos):
    if len(listaProductos) == 0: # No proceder si aún no hay productos
        print("\nAún no se han registrado productos. Volviendo al menú principal")
        return
    
    productoSeleccionado = "" # Variable para almacenar el producto seleccionado
    inventario(listaProductos, detalleProductos) # Llamar a módulo inventario para mostrar productos disponibles y no duplicar código
    
    print("\nNUEVA VENTA") 
    print("1. Crear venta | 0. Volver al menú anterior")
    inputVentas = input("\nSeleccione una opción del menú: ")
    while True:
        if inputVentas == "0": # 0. Volver al menú anterior
            break
        if inputVentas == "1":
            # Seleccionar el producto a vender
            seleccionProducto = input("\nEscriba el [[ID]] del producto a vender: ")    
            if seleccionProducto == "": # Validar que se escriba algún ID
                print("El ID del producto no puede estar vacío, por favor intente nuevamente.")
                break
            indiceProducto = int(seleccionProducto) - 1 # Restar 1 al input del usuario, para que coincida con el índice de la lista
            if indiceProducto < 0 or indiceProducto > len(listaProductos): # Validar que el ID corresponda a un producto existente
                print("El ID del producto no existe, por favor intente nuevamente.")
                break
            
            # Indicar y validar la cantidad a vender
            inputCantidadVenta = input("\nEscriba la cantidad a vender: ")
            if inputCantidadVenta == "": # Validar que no esté vacío
                print("La cantidad a vender no puede estar vacía, por favor intente nuevamente.")
                break

            cantidadVenta = int(inputCantidadVenta)
            
            if cantidadVenta > detalleProductos[indiceProducto][0]: # Validar si hay suficiente inventario para no dejar en negativos. Posición 0 del arreglo es la cantidad en inventario
                print("No hay suficiente inventario para completar la venta. Por favor intente nuevamente.")
                break

            # Si no hay errores de validación, proceder
            productoSeleccionado = listaProductos[indiceProducto]          
            detalleProductos[indiceProducto][0] -= cantidadVenta # Actualizar cantidad en inventario
            subtotal = cantidadVenta * detalleProductos[indiceProducto][1] # Posición 1 del arreglo es el precio unitario
            print("\nResumen de la venta:")
            print(f"Producto a vender: {productoSeleccionado}")
            print(f"Cantidad a vender: {cantidadVenta} unidad(es)")
            print(f"Subtotal: {MONEDA}{subtotal}")
            print(f"Cantidad restante: {detalleProductos[indiceProducto][0]} unidad(es)")
    
            # Opción para registrar otra venta
            print("\n1. Registrar otra venta \n0. Volver al menú principal")
            inputVentas = input("\nSeleccione una opción: ")
        
        else: # Validar opción seleccionada
            print("Opción no válida, por favor intente nuevamente.")
            return

    return listaProductos, detalleProductos

'''
MÓDULO 4: Reabastecer inventario
Función que permite añadir más stock a un producto.
'''

def reabastecer(listaProductos, detalleProductos):

    if len(listaProductos) == 0: # No proceder si aún no hay productos
            print("\nAún no se han registrado productos. Volviendo al menú principal")
            return

    inventario(listaProductos, detalleProductos) # Llamar a módulo inventario para mostrar productos disponibles y no duplicar código

    print("\nREABASTECER INVENTARIO") 
    print("1. Reabastecer inventario | 0. Volver al menú anterior")
    inputRestock = input("\nSeleccione una opción del menú: ")
    while True:
        if inputRestock == "0": # 0. Volver al menú anterior
            break
        if inputRestock == "1":
            # Seleccionar el producto a reabastecer
            seleccionRestock = input("\nEscriba el [[ID]] del producto a reabastecer: ")    
            if seleccionRestock == "": # Validar que se seleccione algún ID
                print("El ID del producto no puede estar vacío, por favor intente nuevamente.")
                break
            indiceRestock = int(seleccionRestock) - 1 # Restar 1 al input del usuario, para que coincida con el índice de la lista
            if indiceRestock < 0 or indiceRestock > len(listaProductos): # Validar que el ID corresponda a un producto existente
                print("El ID del producto no existe, por favor intente nuevamente.")
                break
            
            # Indicar y validar la cantidad a reabastecer
            inputCantidadRestock = input("\nEscriba la cantidad a reabastecer: ")
            if inputCantidadRestock == "": # Validar que no esté vacío
                print("La cantidad a reabastecer no puede estar vacía, por favor intente nuevamente.")
                break

            cantidadRestock = int(inputCantidadRestock)
            if cantidadRestock < 0: # Validar que no sea negativa
                print("La cantidad a reabastecer no puede ser negativa, por favor intente nuevamente.")
                break

            # Si no hay errores de validación, proceder
            detalleProductos[indiceRestock][0] += cantidadRestock # Actualizar cantidad en inventario. Posición [i][0] del arreglo es la cantidad en inventario
            print("\nReabastecimiento exitoso")
            print(f"Ahora hay {detalleProductos[indiceRestock][0]} unidades de {listaProductos[indiceRestock]}")

            # Opción para reabastecer otro producto
            print("\n1. Reabastecer otro producto \n0. Volver al menú principal")
            inputRestock = input("\nSeleccione una opción: ")
        
        else: # Validar opción seleccionada
            print("Opción no válida, por favor intente nuevamente.")
            return listaProductos, detalleProductos
    
    return listaProductos, detalleProductos

'''
ESTRUCTURA PRINCIPAL DEL PROGRAMA
Gestión de inventario de una tienda de artículos deportivos.
'''

MONEDA = "CRC" # Definir la moneda como CONSTANTE global. Si la tienda usa otra moneda, solo se necesita cambiar este valor
listaProductos = [] # Arreglo unidimensional para almacenar los nombres de los productos
detalleProductos = [] # Arreglo bidimensional para almacenar las cantidades y precios

while True:
        print("\n¡Hola! Le damos la bienvenida al sistema.")    
        print("\nMENÚ PRINCIPAL")    
        print("1. Registrar producto | 2. Consultar inventario | 3. Realizar venta | 4. Reabastecer inventario | 0. Salir del programa")
        inputMenu = input("\nSeleccione una opción del menú: ")
        
        if inputMenu == "1": # Módulo 1: Registro de productos
            registro(listaProductos, detalleProductos)
        
        elif inputMenu == "2": # Módulo 2: Consulta de inventario
            inventario(listaProductos, detalleProductos)
        
        elif inputMenu == "3": # Módulo 3:Realizar venta
            ventas(listaProductos, detalleProductos)
        
        elif inputMenu == "4": # Módulo 4: Reabastecer inventario
            reabastecer(listaProductos, detalleProductos)
       
        elif inputMenu == "0":  # Salir del programa
            print("Gracias por usar el sistema. Hasta la próxima. \n")
            break
        
        # Validar opción seleccionada
        else:
            print("Opción no válida, por favor seleccione una opción del menú.")