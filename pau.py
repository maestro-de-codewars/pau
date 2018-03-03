# Cada uno tiene sus partes pero,
# si crees que puedes ayudar a uno de tus compañeros
# no dudes en hacerlo.

# Al final sera "False" pero
# por ahora sera "True"
# para poder probar el codigo:
logueado = True

# Esta es la parte de Snow:
def login(matricula):
    logueado = False

# Esta es la parte de Bidó
def codewars(code_wars = "codewars.csv", ejercicios = "ejercicios.csv", procesado = "processed.csv"):
    if logueado:
        print(code_wars)
        # Escribir codigo aqui
        # Aqui va codigo de Numero 1
    else:
        print("Tienes que loguearte primero.")

# Esta es la parte de Federico:
def summary():
    if logueado:
        print(logueado)
        # Escribir codigo aqui
        # Aqui va codigo de Numero 1
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
