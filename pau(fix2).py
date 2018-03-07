import csv
# Cada uno tiene sus partes pero,
# si crees que puedes ayudar a uno de tus compañeros
# no dudes en hacerlo.

# Al final sera "False" pero
# por ahora sera "True"
# para poder probar el codigo:

# Por ahora sera "12345678"
# para poder probar el codigo:

# Esta es la parte de Snow:
path3= 'processed.csv'
student_id =input("Introduzca su matricula")
logueado = False
def login(student_id):
    if len(student_id)==8 and student_id.isnumeric():
        logueado = True
    else:
        print ("Matricula no valida")

if validacion==True:
    matricula=str(student_id)
    with open (path3,"w+") as archivo:
        archivo.write(matricula)
else:
    exit()
# Esta es la parte de Bidó
def codewars():

    print("Ingrese el path del archivo del cronograma de ejercicios:")
    ejercicios = input()
    print("Ingrese el path del archivo de Codewars:")
    code_wars = input()
    print("Ingrese el nombre con el que quiere salvar el archivo procesado:")
    procesado = input()

    if ejercicios == "":
        ejercicios = "exercises.csv"

    if code_wars == "":
        code_wars = "codewars.csv"

    if procesado == "":
        procesado = "processed.csv"

    lista_de_inputs = [ejercicios, code_wars, procesado]

    for item in lista_de_inputs:
        if not item[-4:] == ".csv":
            print("Tienes que escribir los nombres de todos los archivos terminando en .csv")
            print("Intenta denuevo.")
            return

    # Aqui va codigo de Numero 1
    path1 = ejercicios
    archivo_ejercicios = []
    with open (path1,"r") as file:
        for item in file.readlines():
            archivo_ejercicios.append(item.replace("https://www.codewars.com/kata/","").strip().split(","))

    path2 = code_wars
    archivo_codewars = []
    with open (path2,"r") as archivo:
        for line in archivo.readlines():
            archivo_codewars.append(line.strip().split(","))

    # Este es el algoritmo:
    # 1- Crear un diccionario para guardar la informacion de los ejercicios hechos en Codewars.
        # 'hechos' es un diccionario para poder confirmar el nombre facilmente.
    hechos = {}

    # 2- Crear una lista donde se guardaran las listas que se retornaran y escribiran en el archivo CSV.
        # ejemplo: [[lista1],[lista2]]
    lista_ejercicios = []
        # lista_ejercicios = [["Batch", "Exercise", "Completed", "Date Completed", "Completed Late"]]

    # 3- Llenar el diccionario con la informacion sacada del archivo de Codewars.
        # el diccionario es: {"slug": "fecha_completado"} (ambos son 'strings')
    del archivo_codewars[0]
    for item1 in archivo_codewars:
        hechos[item1[2]] = item1[4]

    # Hay que importar datetime para trabajar con las fechas en el paso 4.
    from datetime import datetime

    # 4- Este paso tiene varios sub-pasos. Comienza trabajando con la informacion del archivo de ejercicios.
        # Tenemos que llenar 'ejercicios' con la informacion que se escribira al CSV procesado.
    del archivo_ejercicios[0]
    for item2 in archivo_ejercicios:
        # Comprueba si el ejercicio fue realizado.
        if item2[3] in hechos.keys():
            # Hay que convertir los strings a fechas.
            date_completed = datetime.strptime(hechos[item2[3]], "%Y-%m-%dT%H:%M:%SZ")
            due_date = datetime.strptime(item2[1], "%Y,%m,%d")

            check = date_completed > due_date
            # Aqui revisamos si la fecha en la que se completo fue despues de la de entrega.
                # (devuelve un booleano)

            lista_ejercicios.append([item2[0], item2[3], True, hechos[item2[3]], check])
                # Aqui le agregamos una lista a la lista 'ejercicios'. Con el formato adecuado (See below).

        else:
            lista_ejercicios.append([item2[0], item2[3], False, None, False])
            # Aqui le agregamos una lista a la lista 'ejercicios'. Con el formato adecuado (See below).

    # Este es el formato de las listas en 'ejercicios':
        # Batch (string), Exercise (string),  Completed (bool), DateCompleted(String or None), CompletedLate (bool)

    # Aqui va el codigo para escribir 'ejercicios' al CSV.

    # Aqui continua el codigo que falta. (Retornar la informacion a la consola.)
    for item3 in lista_ejercicios:
        print("%s, %s, %s, %s, %s" % (item3[0], item3[1], item3[2], item3[3], item3[4]))

# Esta es la parte de Federico:
def summary():

    # Aqui va el codigo para leer el archivo procesado.
    # retorna una lista de listas en la variable "archivo_procesado"

    #nota: la lista debe estar en el formato pedido por el profe que es:
# list= [Batch (string), Exercise (string),  Completed (bool), DateCompleted(String or None), CompletedLate (bool)]
#cualquier duda ver la lista de prueba adjuntada abajo
    Total_Completed = 0   # se declara la variable
    Total_Late = 0      #se declara la variable
    Total_Excercises = len(archivo_procesado)    # esta variable sera igual a la cantidad de listas que tenga la lista ya que por cada lista habra un ejercicio
    for exercise in archivo_procesado:           #vamos a recorrer cada lista para sacar la data
        if exercise[2] == True:     #verificamos si el ejercicio fue hecho
            Total_Completed +=1
            if exercise[4] == True:     #verificamos si se entrego tarde
                Total_Late +=1
    Total_Missing = len(archivo_procesado) - Total_Completed   # los ejercicio no entregados son igual al total de ejercicios menos los realizados
    print ('report: \nStudentId:%i \nTotalExcercises:%i \nTotalCompleted:%i \nTotalLate:%i \nTotalMissing:%i' %(student_id,Total_Excercises,Total_Completed,Total_Late,Total_Missing))
    # lista de prueba debajo
    #list_=[[1,'ejer1',True,'28/2/2018',True],[2,'ejer2',False,'28/2/2018',False],[3,'ejer3',True,'28/2/2018',False]]
#print(summary(list_))    #con esto mostramos en pantalla la data de summary

# Esto es lo que vuelve nuestro codigo
# una aplicacion:
while True:

    # Printear las instrucciones. (Hacer)
    print('''
Bienvenido.
Comandos:
    - login
    - exit
''')

    # Primero recibimos un comando:
    comando1 = input().lower()

    # Luego vemos que dice el comando y corremos el codigo:
    # Escribir todos los comandos. (Hacer)
    if comando1 == "login":
        login()
        while logueado:
            print('''
Comandos:
    - codewars
    - summary
    - exit
''')
            comando2 = input()
            if comando2 == "codewars":
                codewars()
            elif comando2 == "summary":
                summary()
            elif comando2 == "exit":
                print("Adios.")
                exit()
            else:
                print("Comando no valido.")

    elif comando1 == "exit":
        print("Adios.")
        exit()

    else:
        print("Comando no valido.")
