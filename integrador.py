import time
import random

""" Busqueda Lineal """
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

""" Busqueda Binaria """
def busqueda_binaria(lista, objetivo):
    
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

""" Acá vamos a medir el tiempo """

def medir_tiempo(funcion, lista, objetivo, repeticiones=1000):

    inicio = time.perf_counter()
    for _ in range(repeticiones):
        funcion(lista, objetivo)
    fin = time.perf_counter()
    return (fin - inicio) / repeticiones

def comparar_algoritmos():

    print("---Comparacion de algoritmos ---")
    
    # Configuración
    tamaño_lista = 10000  
    lista = random.sample(range(1, 1000000), tamaño_lista) 
    
    # En objetivo elegimos un número aleatoriamente
    objetivo = random.choice(lista)
    
    print(f"El tamaño de la lista es: {tamaño_lista}")
    print(f"Numero buscado: {objetivo}")
    print("-" * 50)
    
    # Busqueda lineal

    inicio_lineal = time.perf_counter()
    resultado_lineal = busqueda_lineal(lista, objetivo)
    fin_lineal = time.perf_counter()
    tiempo_lineal = fin_lineal - inicio_lineal
    
    # Busqueda Binaria

    lista_ordenada = sorted(lista)  # Lista ordenada para búsqueda binaria
    
    inicio_binaria = time.perf_counter()
    resultado_binaria = busqueda_binaria(lista_ordenada, objetivo)
    fin_binaria = time.perf_counter()
    tiempo_binaria = fin_binaria - inicio_binaria
    
    # RESULTADOS
    print("--- RESULTADOS ---")
    print(f"Busqueda Lineal: Resultado = {resultado_lineal}, Tiempo = {tiempo_lineal:.8f} segundos")
    print(f"Busqueda Binaria: Resultado = {resultado_binaria}, Tiempo = {tiempo_binaria:.8f} segundos")
    
    # ANÁLISIS DE EFICIENCIA
    if tiempo_lineal > 0 and tiempo_binaria > 0:
        mejora = tiempo_lineal / tiempo_binaria
        print(f"\nLa busqueda binaria fue {mejora:.2f} veces mas rapida")
    
    return tiempo_lineal, tiempo_binaria


""" En esta parte nos proponemos probar diferentes tamaños para ver la comparación entre ambos algoritmos """
def probar_diferentes_tamaños():

    print("\n=== PRUEBA CON DIFERENTES TAMAÑOS ===\n")
    
    tamaños = [1000, 5000, 10000, 50000, 100000]
    
    print(f"{'Tamaño':<8} {'Lineal (s)':<15} {'Binaria (s)':<15} {'Mejora':<10}")
    print("-" * 55)
    
    for tamaño in tamaños:
        # Lista de prueba
        lista = random.sample(range(1, tamaño * 10), tamaño)
        objetivo = random.choice(lista)
        
        # Búsqueda lineal 
        tiempo_lineal = medir_tiempo(busqueda_lineal, lista, objetivo, 100)
        
        # Búsqueda binaria 
        lista_ordenada = sorted(lista)
        tiempo_binaria = medir_tiempo(busqueda_binaria, lista_ordenada, objetivo, 100)
        
        # Calcular mejora
        if tiempo_binaria > 0:
            mejora = tiempo_lineal / tiempo_binaria
        else:
            mejora = 0
        
        print(f"{tamaño:<8} {tiempo_lineal:<15.8f} {tiempo_binaria:<15.8f} {mejora:<10.2f}x")


""" Ejecutamos la función principal de la aplicación """
def main():

    print("ALGORITMOS DE BUSQUEDA: LINEAL VS BINARIA")
    print("=" * 50)
    
    # Comparación básica
    comparar_algoritmos()
    
    # Prueba con diferentes tamaños
    probar_diferentes_tamaños()

    
if __name__ == "__main__":
    main()