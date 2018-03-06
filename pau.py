# Cada uno tiene sus partes pero,
# si crees que puedes ayudar a uno de tus compañeros
# no dudes en hacerlo.

# Al final sera "False" pero
# por ahora sera "True"
# para poder probar el codigo:
logueado = True

# Por ahora sera "12345678"
# para poder probar el codigo:
student_id = "12345678"

# Esta es la parte de Snow:
def login(matricula):
    logueado = True
    student_id = matricula

# Esta es la parte de Bidó
def codewars(code_wars = "codewars.csv", ejercicios = "ejercicios.csv", procesado = "processed.csv"):
    if logueado:
	path1=ejercicios
	archivo_ejercicios=[]
	with open (path1,"r") as file:
    		for item in file.readlines():
        		archivo_ejercicios.append(item.replace("https://www.codewars.com/kata/","").split(",")) 

	path2=code_wars
	archivo_codewars=[]
	with open (path2,"r") as archivo:
    		for line in archivo.readlines():
        		archivo_codewars.append(line.split(","))
       
	
        # Este es el algoritmo:
        # 1- Crear un diccionario para guardar la informacion de los ejercicios hechos en Codewars.
            # 'hechos' es un diccionario para poder confirmar el nombre facilmente.
        hechos = {}

        # 2- Crear una lista donde se guardaran las listas que se retornaran y escribiran en el archivo CSV.
            # ejemplo: [[lista1],[lista2]]
        ejercicios = []

        # 3- Llenar el diccionario con la informacion sacada del archivo de Codewars.
            # el diccionario es: {"nombre_del_ejercicio": "fecha_completado"} (ambos son 'strings')
        for item in archivo_codewars:
            hechos.[item[2]] = item[4]

        # Hay que importar datetime para trabajar con las fechas en el paso 4.
        from datetime import datetime

        # 4- Este paso tiene varios sub-pasos. Comienza trabajando con la informacion del archivo de ejercicios.
            # Tenemos que llenar 'ejercicios' con la informacion que se escribira al CSV procesado.

        for item in archivo_ejercicios:

            # Comprueba si el ejercicio fue realizado.
            if item[3] in hechos.keys():

                # Hay que convertir los strings a fechas.
                date_completed = datetime.strptime(hechos[item[3]], "%Y-%m-%dT%H:%M:%SZ")
                due_date = datetime.strptime(item[1], "%Y,%m,%d")

                check = date_completed > due_date
                # Aqui revisamos si la fecha en la que se completo fue despues de la de entrega.
                    # (devuelve un booleano)

                ejercicios.append([item[0], item[3], True, hechos[item[3]], check])
                # Aqui le agregamos una lista a la lista 'ejercicios'. Con el formato adecuado (See below).

            else:
                ejercicios.append([item[0], item[3], False, None, False])
                # Aqui le agregamos una lista a la lista 'ejercicios'. Con el formato adecuado (See below).

        # Este es el formato de las listas en 'ejercicios':
            # Batch (string), Exercise (string),  Completed (bool), DateCompleted(String or None), CompletedLate (bool)

        # Aqui continua el codigo que falta. (Retornar la informacion a la consola.)

    else:
        print("Tienes que loguearte primero.")

# Esta es la parte de Federico:
def summary(list_):
    #nota: la lista debe estar en el formato pedido por el profe que es: 
# list= [Batch (string), Exercise (string),  Completed (bool), DateCompleted(String or None), CompletedLate (bool)]
#cualquier duda ver la lista de prueba adjuntada abajo 
    Total_Completed = 0   # se declara la variable
    Total_Late = 0      #se declara la variable
    Total_Excercises = len(list_)    # esta variable sera igual a la cantidad de listas que tenga la lista ya que por cada lista habra un ejercicio
    for exercise in list_:           #vamos a recorrer cada lista para sacar la data 
        if exercise[2] == True:     #verificamos si el ejercicio fue hecho
            Total_Completed +=1
            if exercise[4] == True:     #verificamos si se entrego tarde
                Total_Late +=1     
    Total_Missing = len(list_) - Total_Completed   # los ejercicio no entregados son igual al total de ejercicios menos los realizados 
    return 'report: \nStudentId:%i \nTotalExcercises:%i \nTotalCompleted:%i \nTotalLate:%i \nTotalMissing:%i' %(20157443,Total_Excercises,Total_Completed,Total_Late,Total_Missing ) 
# lista de prueba debajo
#list_=[[1,'ejer1',True,'28/2/2018',True],[2,'ejer2',False,'28/2/2018',False],[3,'ejer3',True,'28/2/2018',False]]
print(summary(list_))    #con esto mostramos en pantalla la data de summary



# Esto es lo que vuelve nuestro codigo
# una aplicacion:
while True:

    # Printear las instrucciones. (Hacer)
    print('''
Bienvenido.
''')

    # Primero recibimos un comando:
    comando = input().lower()

    # Luego vemos que dice el comando y corremos el codigo:
    # Escribir todos los comandos. (Hacer)
    if comando == "exit":
        exit()
