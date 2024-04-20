# #Ejerciocio 4

# numero=int(input("Numero:"))
# factorial=1
# if numero!=0:
#     for i in range(1,numero+1):
#         factorial=factorial*i
# print("Factorial:",factorial)        

#Ejercicio 5

# while True:
#     valor = int(input("Ingrese un número impar\n"))
#     if valor % 2 != 0:
#         print("Enhorabuena, has ingresado un número impar.")
#         break
#     else:
#         print("Error: El número ingresado es par. Intentalo nuevamente")
        
#Ejercicio 6

resultado = 1
base = int(input("Ingrese base\n"))
exponente = int(input("Ingrese exponente\n"))
for i in range(exponente):
    resultado = resultado * base
print(f"El resultado de la potencia de base es {base} elevado a {exponente} es: {resultado}")