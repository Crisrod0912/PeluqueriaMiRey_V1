# ==================== Variables Globales ====================
usuario = "admin"
blockLogin = True
can = 0
afluenciaManana = 0
afluenciaTarde = 0

# ==================== Módulo de Reservas ====================
def ModuloReservas():
    global can
    global afluenciaManana
    global afluenciaTarde

    can = int(input("Ingrese la cantidad de personas: "))

    horarios = ["8:00", "9:00", "10:00", "11:00", "12:00", 
                "13:00", "14:00", "15:00", "16:00", "17:00"]
    
    horas_reservadas = []

    x = 0
    while x < can:
        print("\nHorarios disponibles: ")
        print(horarios)
        
        hora = input("Indique el horario deseado: ")

        if hora in horarios:
            horarios.remove(hora)
            horas_reservadas.append(hora)

            if hora <= "11:00":
                afluenciaManana += 1
            else:
                print("Horario no válido, inténtelo de nuevo. ")

            x += 1
            print("Horario reservado correctamente. ")
        else:
            print("Horario no válido, inténtelo de nuevo. ")

        if can == 1:
            numReserva = 1
            peluquero = "Gabriel"
        elif can == 2:
            numReserva = 2
            peluquero = "Zaid"
        elif can == 3:
            numReserva = 3
            peluquero = "Lilith"
        else:
            print("Máximo permitido: 3 personas. ")
            return
        
        print("\nNúmero de reserva: ", numReserva)
        print("\nPeluquero asignado: ", peluquero)
        print("\nHorarios reservados: ", horas_reservadas)

        archivo = open("reservas.txt", "a")
        archivo.write(f"Reserva: {numReserva}\n")
        archivo.write(f"Cliente: {usuario}\n")
        archivo.write(f"Peluquero: {peluquero}\n")
        archivo.write(f"Cantidad: {can}\n")
        archivo.write(f"Horarios: {horas_reservadas}\n")
        archivo.write("-----------------------\n")
        archivo.close()

# ==================== Módulo de Facturación ====================
def ModuloFacturacion():
    global can
    total = 0

    nombre = input("Ingrese su nombre completo: ")
    cedula = input("Ingrese su cédula: ")
    reserva = int(input("Ingrese el número de reserva: "))

    x = 0
    while x < can:
        print(f"\nPersona {x + 1}")
        condicion = input("Condición (niño/adulto/adulto mayor): ")

        if condicion == "adulto":
            total += 5000
        else:
            total += 2500

        x += 1

    impuesto = total * 0.13
    totalFinal = total + impuesto

    archivo = open("facturacion.txt", "a")
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Cédula: {cedula}\n")
    archivo.write(f"Reserva: {reserva}\n")
    archivo.write(f"Subtotal: {total}\n")
    archivo.write(f"Impuesto: {impuesto}\n")
    archivo.write(f"Total: {totalFinal}\n")
    archivo.close()

    print("\n¡FACTURA GENERADA CORRECTAMENTE! ")
    print("Total a pagar: ", totalFinal)

# ==================== Módulo de Informes ====================
def ModuloInformes():
    print("\n--- Módulo de Informes ---")
    print("1. Afluencia por horario ")
    print("2. Salir ")

    op = int(input("Seleccione una opción: "))

    if op == 1:
        if afluenciaManana > afluenciaTarde:
            print("Mayor afluencia en la mañana. ")
        elif afluenciaTarde > afluenciaManana:
            print("Mayor afluencia en la tarde. ")
        else:
            print("Misma afluencia en la mañana y tarde. ")
    elif op == 2:
        return
    else:
        print("Opción inválida. ")

# ==================== Menú Principal ====================
while True:
    opcion = int(input(
        "\nBienvenido a la Peluquería Mi Rey\n"
        "1. Login\n"
        "2. Módulo de Reservas\n"
        "3. Módulo de Facturación\n"
        "4. Módulo de Informes\n"
        "5. Salir\n"
        "Seleccione una opción: "
    ))

    if opcion == 1:
        usuario = input("Digite su nombre de usuario: ")
        blockLogin = 1

    elif opcion == 2:
        if blockLogin == 1:
            ModuloReservas()
        else:
            print("Debe de iniciar sesión primero. ")

    elif opcion == 3:
        ModuloFacturacion()

    elif opcion == 4:
        if blockLogin == 1:
            ModuloInformes()
        else:
            print("Debe de iniciar sesión primero. ")

    elif opcion == 5:
        print("Gracias por utilizar el sistema. ¡Nos vemos pronto! ")
        break

    else:
        print("Opción inválida, inténtelo de nuevo. ")
