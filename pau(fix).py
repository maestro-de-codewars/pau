# Cada uno tiene sus partes pero,
# si crees que puedes ayudar a uno de tus compañeros
# no dudes en hacerlo.

# Al final sera "False" pero
# por ahora sera "True"
# para poder probar el codigo:
logueado = True

# Por ahora sera "12345678"
# para poder probar el codigo:
student_id = ""

# Esta es la parte de Snow:
def login():
    def validacion(s):
        student_id = len(s)
            if len(s) == 8:
                print(student_id.isnumeric())
            else:
                 return False
        print("This student_id is valid")
    entrada1 = input()
    logueado = validacion(entrada1)


# Esta es la parte de Bidó
def codewars(code_wars = "codewars.csv", ejercicios = "ejercicios.csv", procesado = "processed.csv"):

    print("Ingrese ")
    entrada2 = input()
    print("Ingrese ")
    entrada3 = input()
    print("Ingrese ")
    entrada4 = input()

    # Aqui va codigo de Numero 1
	path1 = ejercicios
	archivo_ejercicios = []
	with open (path1,"r") as file:
		for item in file.readlines():
    		archivo_ejercicios.append(item.replace("https://www.codewars.com/kata/","").split(","))

	path2 = code_wars
	archivo_codewars = []
	with open (path2,"r") as archivo:
		for line in archivo.readlines():
    		archivo_codewars.append(line.split(","))



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
        hechos.[item1[2]] = item1[4]

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
    # Aqui va codigo de Numero 1

    # Escribir codigo aqui:
    # Total de ejercicios:
    t_exercises =

    # Total de completados:
    t_completed =

    # Total de tardes:
    t_late =

    # Total de sin hacer:
    t_missing =

    # student_id esta declarada arriba
    print (" StudentId: %s \n TotalExcercises: %i \n TotalCompleted: %i \n TotalLate: %i \n TotalMissing: %i" % (student_id, t_exercices, t_completed, t_late, t_missing))
    # Genera el siguiente reporte en consola:
    # StudentId: Matricula actualmente loggeada.
    # TotalExcercises: (int)
    # TotalCompleted: (int)
    # TotalLate: (int)
    # TotalMissing: (int)

    # Nota para Federico: Ponle el nombre que quieras a las variables. O trabaja con ellas asi. Your choice.

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
            print("Instrucciones")
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
