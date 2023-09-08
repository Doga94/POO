import time

def medir_tiempo_ejecucion(funcion):

    """
    Este decorador mide el tiempo de ejecución de una función.

    Toma una función como argumento y devuelve una nueva función.
    La nueva función es una envoltura de la función original.
    La envoltura mide el tiempo que tarda la función original en ejecutarse.
    """

    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo total de ejecucion: {fin-inicio}")
    return wrapper

def decorador_puntos(funcion):

    """
    Este decorador imprime tres puntos antes y después de que la función original se ejecute.

    Toma una función como argumento y devuelve una nueva función.
    La nueva función es una envoltura de la función original.
    La envoltura imprime tres puntos antes y después de que la función original se ejecute.
    """

    def wrapper(*args, **kwargs):
        print("..........")
        funcion(*args, **kwargs)
        print("..........")
    return wrapper

@decorador_puntos
@medir_tiempo_ejecucion
def recorrer_ciclo(rango):
    """
    Esta función imprime los números del 0 al rango especificado, y luego espera un segundo.

    El decorador `medir_tiempo_ejecucion()` mide el tiempo que tarda esta función en ejecutarse.
    """
    for i in range(rango):
        print(i)
        time.sleep(1)

recorrer_ciclo(rango=5)

