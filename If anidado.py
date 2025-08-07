# Programa simple con If anidado

edad = int(input("¿Cuantos años tienes?  "))

if edad >= 18:
    print("Eres mayor de edad")
    if edad >= 65:
        print("Eres un adulto mayor")
    else:
        print("Eres un adulto joven")
else:
    print("Eres menor de edad")
    if edad >= 13:
        print("Eres un adolescente")
    else:
        print("Eres un niño o niña")

        