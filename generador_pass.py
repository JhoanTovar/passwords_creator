import random
import string


def generar_contraseña(longitud, num_min, min_mayus, min_minus):
    caracteres = string.ascii_letters + string.digits
    caracteres_mayus = string.ascii_uppercase
    caracteres_minus = string.ascii_lowercase
    
    if longitud < num_min + min_mayus + min_minus:
        raise ValueError('La longitud mínima especificada no es suficiente para cumplir con los requisitos.')
    
    
    # Calcular la longitud restante para caracteres aleatorios.
    longitud_restante = longitud - (num_min + min_mayus + min_minus)
    
    # Generar caracteres aleatorios.
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud_restante))
    
    # Generar dígitos.
    contraseña += ''.join(random.choice(string.digits) for _ in range(num_min))
    
    # Generar letras mayúsculas.
    contraseña += ''.join(random.choice(caracteres_mayus) for _ in range(min_mayus))
    
    # Generar letras minúsculas.
    contraseña += ''.join(random.choice(caracteres_minus) for _ in range(min_minus))
    
    # Mezclar la contraseña.
    contraseña = ''.join(random.sample(contraseña, len(contraseña)))

    return contraseña