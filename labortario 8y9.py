#problema1
#EJERCICIO PARTE1
# 1. Validar la edad de un usuario.
from datetime import datetime

def validar_edad(fecha_nacimiento):
    """Valida la edad de un usuario a partir de su fecha de nacimiento.

    Args:
        fecha_nacimiento: La fecha de nacimiento del usuario en formato YYYY-MM-DD.

    Returns:
        True si el usuario es mayor de edad, False en caso contrario.
    """

    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year

    if fecha_actual.month < fecha_nacimiento.month:
        edad -= 1

    return edad >= 18

# Ejemplo de uso

fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

if validar_edad(fecha_nacimiento):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# 2. Verificar el tipo de dato de una variable.
    
# 3. Validar el rango de una calificación.
# 4. Asegurar que una lista no esté vacía.
# 5. Validar la igualdad de dos objetos.
# 6. Asegurar que un ciclo while se ejecuta al menos una vez.
# 7. Asegurar que una función retorna un valor específico.
# 8. Validar el estado de una variable después de una operación.
# 9. Asegurar que un módulo se ha importado correctamente.

