# -*- coding: utf-8 -*-
import math

def tiempo_ejecucion_busqueda(n, costo_lineal=1):
    if n <= 1:
        return 1

    costo_recursivo = 2 * tiempo_ejecucion_busqueda(n / 2, costo_lineal)
    costo_combinacion = costo_lineal * n

    return costo_recursivo + costo_combinacion

tamanos_n = [100, 200, 400, 800, 1600, 3200]
tiempos_simulados = []

print("Análisis de la Complejidad T(n) = 2*T(n/2) + O(n)")
for n in tamanos_n:
    tiempo = tiempo_ejecucion_busqueda(n)
    tiempos_simulados.append(tiempo)
    print(f"Para n = {n}, el tiempo simulado es: {tiempo:.2f}")

def analisis_metodo_maestro(a, b, f_n_potencia):

    log_b_a = math.log(a, b)

    print("\n--- Aplicación del Método Maestro ---")
    print(f"Ecuación: T(n) = {a}*T(n/{b}) + O(n^{f_n_potencia})")
    print(f"El valor de referencia es n^(log_b a): n^{log_b_a:.2f}")

    if f_n_potencia < log_b_a:
        complejidad = f"O(n^{log_b_a:.2f})"
        caso = "Caso 1"
    elif f_n_potencia == log_b_a:
        complejidad = f"O(n^{log_b_a:.2f} * log n)"
        caso = "Caso 2"
    else:
        complejidad = f"O(n^{f_n_potencia})"
        caso = "Caso 3"

    print(f"f(n) = n^{f_n_potencia} (d) es comparado con n^{log_b_a:.2f} (log_b a)")
    print(f"Resultado: {caso}. La complejidad es: {complejidad}")
    return complejidad

print("\n" + "="*50)
resultado_maestro = analisis_metodo_maestro(a=2, b=2, f_n_potencia=1)
print("="*50)
print(f"La complejidad final del algoritmo es: {resultado_maestro}")
