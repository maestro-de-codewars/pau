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
        # Aqui va codigo de Numero 1
        # Escribir codigo aqui
        from datetime import datetime
        archivo_ejercicios = []
        file.readlines()
        archivo_ejercicios.append()
        ejercicios = []
        hechos = {}
        for item in archivo_codewars:
            hechos.[item[1]] = item[4]

        for item in archivo_ejercicios:
            if item[2] in hechos.keys():
                date_completed = datetime.strptime(hechos[item[2]], "%Y-%m-%dT%H:%M:%SZ")
                due_date = datetime.strptime(item[1], "%Y,%m,%d")
                check = date_completed > due_date
                ejercicios.append([item[0], item[2], True, hechos[item[2]], check])
            else:
                

        return ()
        # Retorna:
        # Batch (string), Exercise (string),  Completed (bool), DateCompleted(String or None), CompletedLate (bool)

    else:
        print("Tienes que loguearte primero.")

# Esta es la parte de Federico:
def summary():
    if logueado:
        # Aqui va codigo de Numero 1

        # Escribir codigo aqui

        print (" StudentId: %s /n TotalExcercises: %i /n TotalCompleted: %i /n TotalLate: %i /n TotalMissing: %i" % (student_id, t_exercices, t_completed, t_late, t_missing))
        # Genera el siguiente reporte en consola:
        # StudentId: Matricula actualmente loggeada.
        # TotalExcercises: (int)
        # TotalCompleted: (int)
        # TotalLate: (int)
        # TotalMissing: (int)

        # Nota para Federico: Ponle el nombre que quieras a las variables. O trabaja con ellas asi. Your choice.
    else:
        print("Tienes que loguearte primero.")

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

# I hope this has been enough boilerplate ^.^
