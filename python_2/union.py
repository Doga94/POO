from typing import Union

# Esta función calcula el perímetro de un cuadrado.
# El parámetro `lado` puede ser un número entero o un número flotante.

# El tipo `Union[int, float]` indica que el parámetro `lado` puede ser un número entero o un número flotante.
# Esto se utiliza para garantizar que la función funcione correctamente, independientemente del tipo de dato que se proporcione para el parámetro `lado`.
def calcular_perimetro_cuadrado(lado: Union[int, float]) -> Union[int, float]:
    # Calcula el perímetro multiplicando el lado por 4.
    return 4 * lado

# Imprime el perímetro de un cuadrado con lado 5.1.
print(calcular_perimetro_cuadrado(lado=5.1))