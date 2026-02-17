print("--- Cotizador Data Nautic ---")

cliente = input("Nombre del cliente: ")
print("Servicios disponibles: 1. Pagina Web ($500) | 2. Inteligencia Artificial ($1000)")

opcion = input("Elija el servicio (1 o 2): ")
horas_texto = input("Cantidad de horas estimadas: ")

#1. VALIDACION DE SEGURIDAD (¿Las horas son numeros?)
if horas_texto.isdigit():
    
    horas = int(horas_texto)
    
    #2. Logica del servicio (¿Que eligio?)
    if opcion == "1":
        precio_hora = 500
        servicio = "Pagina Web"
        es_valido = True # Usaremos este "bandera" para saber su todo va bien
    else:
        #Fijate en este TRUCO: Un "if" seguido de otro "if" (elif)
        if opcion == "2":
            precio_hora = 1000
            servicio = "Inteligencia Artificial"
            es_valido = True
        else:
            print("Error: La opcion de servicio no existe.")
            es_validos = False # Bajamos la bandera, algo salio mal
            
    #3. CALCULO FINAL (Solo si la opcion fue valida)
    if es_valido == True:
        
        total = horas * precio_hora
        
        print("-----------------------------------")
        print("Cliente: " + cliente)
        print("Servicio: " + servicio)
    print("Costo Base: $" + str(total))
    
    #4. DESCUENTO POR VOLUMEN (Si el proyecto es grande)
    if total > 50000:
        descuento = 5000
        total_final = total - descuento
        print("¡Descuento aplicado! (-$5000)")
        print("TOTAL A PAGAR: $" + str(total_final))
    else:
        print("TOTAL A PAGAR: $" + str(total))
       
else:
    print("Error: Las horas deben ser un numero entero.")
   
print("--- Fin de la cotizacion ---") 
    