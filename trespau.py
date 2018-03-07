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
