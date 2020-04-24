from collections import defaultdict
def valor_defecto():
    return "Ese elemento no existe en el diccionario."

usuario = defaultdict(valor_defecto)
usuario["ID"] = 1
usuario["Nombre"] = "Enrique"
usuario["Apellidos"] = "Barros Fernández"
usuario["Edad"] = 28

print(usuario["ID"]) 
print(usuario["Nombre"]) 
print(usuario["Apellidos"]) 
print(usuario["Edad"])
print(usuario["Dirección"]) 

print(type(usuario))



#Diccionario sin control de excepciones.
"""usuario = {
    "ID" : 1,
    "Nombre" : "Enrique",
    "Apellidos" : "Barros Fernández",
    "Edad" : 28
    }

print(usuario["ID"]) 
print(usuario["Nombre"]) 
print(usuario["Apellidos"]) 
print(usuario["Edad"]) 
print(usuario["Dirección"]) """

