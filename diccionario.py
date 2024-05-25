import os, time
os.system("cls")

for x in range(3):
    idUsuario = int(input("Ingrese id usuarios\n"))
    nombre = input("Ingrese nombre de usuario\n")
    usuarios = input("Ingrese usuarios\n")
    correo = input("Ingrese correo\n")
    nivel = int(input("Ingrese nivel (1 a 100)\n"))
    
    #diccionario
    usuario = {
        "id" : idUsuario,
        "nombre" : nombre,
        "correo" : correo,
        "nivel" : nivel
    } 
    usuarios.append(usuario)
    
    #id minimo
    idMinimo = min(usuario["id"] for usuario in usuarios)
    
    #buscar el elemento con el id mas bajo y lo elimino
    for usuario in usuarios:
        if usuario["id"] == idMinimo:
            usuarios.remove(usuario)
            
    for usu in usuarios:
        print(usu)        