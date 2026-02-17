print("--- BIENVENIDO AL CAJERO AUTOMATICO ---")

# 1. SALDO INICIAL
saldo_actual = 1000
print("Su saldo disponible es: $" + str(saldo_actual))

# 2. INPUT
retiro_texto = input("¿Cuánto dinero desea retirar? ")

# 3. PRIMER GUARDIA (¿Es número?)
if retiro_texto.isdigit():

    # 4. CONVERSIÓN
    # Fíjate: Aquí hay 4 espacios de sangría
    retiro_numero = int(retiro_texto)

    # 5. SEGUNDO GUARDIA (¿Tiene saldo?)
    # Este if está DENTRO del anterior (mantiene la sangría)
    if retiro_numero <= saldo_actual:
        
        # OPERACIÓN (Éxito)
        # Aquí hay 8 espacios (doble sangría)
        saldo_nuevo = saldo_actual - retiro_numero

        print("¡Retiro exitoso!")
        print("Su nuevo saldo es: $" + str(saldo_nuevo))
        print("Por favor tome su dinero.")

      else:
        # OPERACIÓN (Fallo de saldo)
        # Este else debe alinearse verticalmente con el if de arriba (línea 18)
        # HE QUITADO LOS # PARA QUE FUNCIONE:
        print("OPERACION DENEGADA: Fondos insuficientes.")
        print("Solo tienes $" + str(saldo_actual))

else:
    # FALLO DEL PRIMER GUARDIA
    # Este else se alinea con el primer if (línea 11)
    print("ERROR: Por favor ingrese solo numeros enteros.")

print("--- Gracias por preferirnos ---")