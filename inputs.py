from generador_pass import generar_contraseña

def inputs_user():
    while True:
        
        try:
            print('#### HOLA, BIENVENID@ A ESTE GENERADOR DE CONTRASEÑAS ALEATORIAS ###')
            longitud = int(input("Ingresa la longitud de la contraseña deseada: "))
            num_min = int(input("Ingresa el número mínimo de dígitos: "))
            min_mayus = int(input("Ingresa el número mínimo de letras mayúsculas: "))
            min_minus = int(input("Ingresa el número mínimo de letras minúsculas: "))

            nueva_contraseña = generar_contraseña(longitud, num_min, min_mayus, min_minus)
            print("Contraseña generada: ", nueva_contraseña)
            
            continuar = (input("¿Desea volver a generar una contraseña? (s) continuar, (cualquier otra tecla) salir:  ")) 
            
            continuar = continuar.lower()
            
            if continuar != 's':
                print('Gracias por usar este programa, hasta luego.')
                break
            
            
        except ValueError as e:
            print(e)