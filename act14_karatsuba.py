import time
import random

def karatsuba(x, y):
    """algoritmo de Karatsuba Divide y Vencerás."""
    if x < 10 or y < 10:
        return x * y

    # 1 DIVISION
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    # 2 CONQUISTA
    z0 = karatsuba(b, d)
    z2 = karatsuba(a, c)
    z1 = karatsuba((a + b), (c + d))

    # 3 INTEGRACION DE LA SOLUCION
    return (z2 * 10**(2 * m)) + ((z1 - z2 - z0) * 10**m) + z0


def generar_numero(digitos):
    """Genera un número entero aleatorio de la cantidad de dígitos especificada."""
    rango_ini = 10**(digitos - 1)
    rango_fin = (10**digitos) - 1
    return random.randint(rango_ini, rango_fin)


def probar_multiplicacion(digitos):
    print(f"\n--- Prueba con números de {digitos} dígitos ---")
    x = generar_numero(digitos)
    y = generar_numero(digitos)

    inicio_k = time.perf_counter()
    resultado_k = karatsuba(x, y)
    fin_k = time.perf_counter()
    tiempo_k = (fin_k - inicio_k) * 1000

    inicio_t = time.perf_counter()
    resultado_t = x * y
    fin_t = time.perf_counter()
    tiempo_t = (fin_t - inicio_t) * 1000

    assert resultado_k == resultado_t, "¡Error en la multiplicación!"

    print(f"Tiempo Karatsuba: {tiempo_k:.5f} ms")
    print(f"Tiempo Tradicional: {tiempo_t:.5f} ms")


if __name__ == "__main__":
    print("INICIANDO PRUEBAS DE KARATSUBA (DIVIDE Y VENCERÁS)")
    probar_multiplicacion(20)
    probar_multiplicacion(50)
    probar_multiplicacion(100)
    probar_multiplicacion(500) 