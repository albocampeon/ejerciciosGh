import os, time
pacientes = []
banderaMenu = True

while banderaMenu:
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Gestionar Paciente")
    print("4) Salir")
    try:
        opcion = int(input("Ingrese opcion\n"))
        if opcion == 1:
            banderaPaciente = True
            while banderaPaciente:
                banderaRut = True
                banderaEdad = True
                print("Registrar Paciente")
                while banderaRut:
                    try:
                        rut = int(input("Ingrese rut\n"))
                        while rut < 5000000 or rut > 99999999:
                            rut = int(input("Ingrese rut\n"))
                        banderaRut = False
                    except:
                        print("Para campo rut, no permite caracteres") 
                    nombre = input("Ingrese nombre \n") 
                    while nombre == "" and nombre == " ":
                        nombre = input("Ingrese nombre, no puede quedar vacío \n") 
                    direccion = input("Ingrese dirección \n")
                    while direccion == "" and direccion == " ":
                        direccion = input("Ingrese dirección, no puede quedar vacío \n")
                    correo = input("Ingrese correo\n")
                    while "@" not in correo:
                        correo = input("Ingrese correo, deber contener al menos un @\n")
                    while banderaEdad:
                        edad = int(input("Ingrese edad \n"))
                        while edad < 0 or edad > 110:
                            edad = int(input("Ingrese edad, debe estar en rango 0 a 110\n"))
                        banderaEdad = False
                    sexo = input("Ingrese sexo\n").lower()
                    while sexo != 'f' and sexo != 'm':
                        sexo = input("Ingrese sexo, solo acepta 'f' o 'm'\n")
                    #registros, lo añadire solo si el dr toma al paciente
                    prevision = input("Ingrese prevision de salud\n").lower()
                    while prevision != 'fonasa' and prevision != 'isapre':
                        prevision = input("Ingrese prevision de salud\n").lower()
                    paciente = [rut, nombre, direccion, correo, edad, sexo, prevision]
                    pacientes.append(paciente)
                    agregarPaciente = input("¿Deseas agregar otro paciente?   's' o 'n'").lower()
                    if agregarPaciente == 's':
                        continue
                    else:
                        banderaPaciente = False
                        print(pacientes)        
        elif opcion == 2:
            print("Atención Paciente ")
            rutPaciente = int(input("Ingrese rut del paciente\n"))
            for paciente in pacientes:
                if paciente[0] == rutPaciente:
                    print("Hola ", paciente[1])
                    registro == input("Motivo de la consulta\n")
                    while registro == "":
                        registro = input("Motivo de la consulta\n")
                        paciente.append(registro)
                        print(pacientes)
                        input("Enter para continuar")
        elif opcion == 3:
            print("Gestionar Paciente")
            
        elif opcion == 4:
            print("Salir")
            print("Ha salido del sistema...")
            
    except:
        print("Opcion ingresada no es valida.")                                           
                                