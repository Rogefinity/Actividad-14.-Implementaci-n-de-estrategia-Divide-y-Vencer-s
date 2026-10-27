# Actividad 14: Implementación de estrategia Divide y Vencerás (Karatsuba)

## Objetivo
Aplicar el paradigma algorítmico de Divide y Vencerás mediante la implementación del algoritmo de Karatsuba para multiplicar números enteros gigantes, reduciendo drásticamente la cantidad de multiplicaciones elementales en comparación con el método tradicional.

## Análisis Asintótico

### Complejidad Temporal: $T(N)$
El algoritmo tradicional de multiplicación requiere multiplicar cada dígito de un número por cada dígito del otro, resultando en una complejidad de $O(N^2)$.
Karatsuba aplica la estrategia divide y vencerás para calcular solo 3 multiplicaciones recursivas en lugar de 4 al dividir los números a la mitad.
* **Relación de recurrencia:** $T(N) = 3T(N/2) + O(N)$
* **Complejidad resultante:** Aplicando el Teorema Maestro, la complejidad es $O(N^{\log_2 3})$, lo que equivale a **$O(N^{1.585})$**. Esto lo hace sustancialmente más rápido para números grandes.

### Complejidad Espacial: $S(N)$
Dado que el algoritmo es puramente recursivo, la memoria principal consumida está dictada por la profundidad de la pila de llamadas del sistema (Call Stack).
* En cada nivel, el tamaño del número (N) se divide a la mitad hasta llegar a 1.
* El número máximo de llamadas activas en la pila es $\log_2(N)$.
* Sin embargo, debido al almacenamiento temporal de las variables fragmentadas (`a`, `b`, `c`, `d`) en memoria en cada capa de recursión, la memoria total consumida escala linealmente en relación al tamaño de los datos de entrada.
* **Complejidad resultante:** **$O(N)$**.

## Conclusiones de las Pruebas
Durante las pruebas con números de 20, 50 y 100 dígitos, se observó que Python optimiza de forma nativa la multiplicación tradicional para números pequeños. Sin embargo, al sobrepasar el umbral de los cientos o miles de dígitos, la curva de rendimiento se invierte y Karatsuba demuestra su superioridad teórica $O(N^{1.585})$ procesando los cálculos en menor tiempo que la aproximación cuadrática $O(N^2)$.
