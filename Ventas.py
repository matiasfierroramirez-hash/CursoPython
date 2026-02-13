print("--- SISTEMA DE VENTAS PYTHON ---")

# 1. ENTRADA DE DATOS
producto = input("¿Que producto desea comprar? ")
precio_texto = input("Ingrese el precio del producto: ")
cantidad_texto = input("Ingrese la cantidad a llevar: ")

# 2. VALIDACION DE SEGURIDAD (doble chequeo con "and")
# Ambas cosas deben ser numeros para continuar
if precio_texto.isdigit() and cantidad_texto.isdigit():

    #3. CONVERSION (Casting)
    precio = int(precio_texto)
    cantidad = int(cantidad_texto)

    #4. CALCULO MATEMATICO BASICO
    total = precio * cantidad

    print("__________________________________")
    print("Subtotal: $" + str(total))

    #5. LOGICA DE NEGOCIO (Descuentos)
    #Si compra mas de $5000, le damos un descuento
    if total > 5000:
        descuento = 1000
        total_final = total - descuento
        print("¡Felicidades! Tienes un descuento de $1000.")
        print("Total a pagar: $" + str(total_final))
    else:
        print("No aplicas para descuento.")
        print("Total a pagar: $" + str(total))

    print("Gracias por su compra, disfrute su " + producto)

else:
    # SI LA VALIDACION FALLA
    print("Error: El precio y la cantidad deben ser numeros enteros.")
