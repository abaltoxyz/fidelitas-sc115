''' 
PRACTICA 2: Gestión de notas de estudiantes
Estudiante: K. Andrés Baltodano Ramírez
Facultad de Ingeniería, Universidad Fidélitas
SC-115: Programación Básica
Profesores: Edward Jiménez, Mariela Ugalde
Noviembre, 2025
'''

''' 
MÓDULO 1: REGISTRO DE ESTUDIANTES Y NOTAS
Función que permite ingresar los datos (Nombre del estudiante y notas de sus exámenes)
'''

def registroEstudiantes(listaGrupo, notasGrupo):
    
    # Submenú de registro
    print("\nREGISTRO DE ESTUDIANTES Y NOTAS")
    print("1. Registrar un estudiante \n0. Volver al menú principal")
    inputRegistro = input("\nSeleccione una opción: ")
    
    while True:
        if inputRegistro == "0": # 0. Volver al menú principal
            break

        if inputRegistro == "1": # 1. Registrar un estudiante
            nombreEstudiante = input("\nIngrese el nombre del estudiante: ")
            if nombreEstudiante == "": # Atrapar input vacío
                print("Por favor escriba algún nombre.")
                return
            
            # Mensaje de confirmación
            print(f"Estudiante registrado correctamente.")

            # Agregar notas
            notasEstudiante = []
            for examen in range (CANTIDAD_EXAMENES): # Cantidad de exámenes definida globalmente
                inputNota = (input(f"\nEscriba la nota del exámen #{examen+1}: ")) # Para enumerar los exámenes en los mensajes se empieza en 1 y no en 0
                # Atrapar inputs vacíos y mostrar error
                if inputNota == "":
                    print("Por favor escriba algún valor e intente nuevamente")
                    break
                nota = float(inputNota) # Si el input existe, convertirlo a float. De momento es imposible validar que no sea string sin usar funciones no vistas en clase.
                # Validar valor de la nota
                if 0 <= nota <= 100:
                    notasEstudiante.append(nota) 
                else:
                    print("La nota debe ser un número entre 0 y 100. Por favor intente nuevamente.") # Mensaje de error en caso de números negativos o superiores a 100
                    break
            
            # Solo proceder si las notas han sido ingresadas correctamente
            if len(notasEstudiante) == CANTIDAD_EXAMENES:
                listaGrupo.append(nombreEstudiante) # Agregar nombre a la lista de estudiantes
                notasGrupo.append(notasEstudiante) # Agrega notas a la lista
                print("Notas registradas correctamente.")

            # Opción para agregar otro estudiante
            print("\n1. Registrar otro estudiante \n0. Volver al menú principal")
            inputRegistro = input("\nSeleccione una opción: ")
        
        else: # Validar opción seleccionada
            print("Opción no válida, por favor intente nuevamente.")
            return
    
    # Devolver listas para usarlas en otros módulos
    return listaGrupo, notasGrupo

''' 
MÓDULO 2: CÁLCULO DE PROMEDIO
Función que permite calcular el promedio de las notas por cada estudiante
'''
def calculoPromedio(listaGrupo, notasGrupo):
    print("\nPROMEDIO DE NOTAS POR ESTUDIANTE")

    # Validar que existan estudiantes registrados
    if listaGrupo == []:
        print("Aún no hay estudiantes registrados.")
        return
        
    promedios = [] # Resetear promedios cada vez que se vuelvan a calcular
    i = 0 # Índice compartido de ambos arreglos para recorrer las listas (Las notas en la posición i corresponden al estudiante en la posición i)
        
    for i in range (len(listaGrupo)):
        # Seleccionar estudiante [i] y sus notas
        nombreEstudiante = listaGrupo[i]
        notasEstudiante = notasGrupo[i]
        sumaNotas = 0 # Necesario para calcular el promedio
        # Suma de notas
        for nota in notasEstudiante:
            sumaNotas += nota # Agregar cada nota a la suma
            
        # Cálculo del promedio según variable global
        promedioEstudiante = sumaNotas / CANTIDAD_EXAMENES 
            
        promedios.append(promedioEstudiante) # Agregar promedio a la lista

        # Mostrar datos
        print (f"Estudiante: {nombreEstudiante} | Promedio: {promedioEstudiante:.2f}") # :.2f para mostrar solo dos decimales
    
    return promedios # Para usar en Módulo 3

''' 
MÓDULO 3: ESTADO DE LOS ESTUDIANTES
Función que permite evaluar si las personas estudiantes aprobaron o reprobaron según el promedio.
'''
def estadoEstudiantes(listaGrupo, promedios):
    print("\nESTADO DE LOS ESTUDIANTES")
    
    # Validar que existan estudiantes registrados
    if listaGrupo == []:
        print("Aún no hay estudiantes registrados.")
        return
    
    i = 0 # Índice para recorrer las listas
    estado = "" # Inicializar variable en blanco para reemplazar valor según el promedio

    # Si después de calcular el promedio se registra un nuevo estudiante, las listas podrían tener tamaños distintos.
    if len(promedios) != len(listaGrupo):
        print("Antes debe calcular los promedios de TODOS los estudiantes. Ingrese primero al Módulo #2 e intente nuevamente.")
    
    else:
        for i in range (len(listaGrupo)):
            # Selecccionar estudiante [i] y su promedio
            nombreEstudiante = listaGrupo[i]
            promedio = promedios[i]

            # Definir estado según variable global
            if promedio >= NOTA_CORTE:
                estado = "APROBADO(A)"
            else:
                estado = "REPROBADO(A)"
            
            # Mostrar datos
            print ("Estudiante: ", nombreEstudiante, f" | Promedio de notas:  {promedio:.2f}", " | Estado: ", estado)
    
    return

''' 
ESTRUCTURA PRINCIPAL DEL PROGRAMA: Gestión de notas de estudiantes.
Si se necesita cambiar los criterios de cantidad de exámenes o nota de corte, solamente será necesario modificar las constantes globales.
Es posible incluir a cuantos estudiantes se necesite.
'''
    
# Definir CONSTANTES para usar en varios módulos, y listas para almacenar los datos
CANTIDAD_EXAMENES = 3 # Cantidad de exámenes por estudiante
NOTA_CORTE = 70 # La nota mínima para aprobar

listaGrupo = [] # Los nombres de los estudiantes
notasGrupo = [] # Las notas de los estudiantes
promedios = [] # Los promedios de los estudiantes

# Menú principal    
while True:
    print("\n*****MENÚ PRINCIPAL*****")    
    print("1. Registro de estudiantes y notas \n2. Promedio de notas por estudiante \n3. Estado del estudiante \n0. Salir del programa")
    inputMenu = input("\nSeleccione una opción del menú: ")
    
    if inputMenu == "1": # Módulo 1: Registro de estudiantes y notas
        registroEstudiantes(listaGrupo, notasGrupo)
    
    elif inputMenu == "2": # Módulo 2: Promedio de notas por estudiante
        promedios = calculoPromedio(listaGrupo, notasGrupo)
    
    elif inputMenu == "3": # Módulo3: Estado de los estudiantes
        if promedios != []: # Continuar solo si se han calculado los promedios
            estadoEstudiantes(listaGrupo, promedios)
        else: 
            print("\nNo se han calculado los promedios aún.")
            continue

    elif inputMenu == "0": # Salir del programa
        print("\nGracias por usar el sistema. Hasta la próxima. ")
        break
    
    else: # Validar opción seleccionada
        print("\nOpción no válida, por favor intente nuevamente.")
