import timeit
from sorting.bubble_sort import bubbleSort
from sorting.selection_sort import selection_sort, cargar_gastos_csv
import pandas as pd
import os

def benchmark_selection_sort(clave):
    archivos = ['data/gastos_50.csv', 'data/gastos_100.csv', 'data/gastos_1000.csv']
    resultados = []
    output_file = 'data/benchmark_selection_sort.csv'
    debe_escribir_header = not os.path.exists(output_file)

    for archivo in archivos:
        try:
            datos = cargar_gastos_csv(archivo)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")
            continue

        def wrapper():
            copia = datos.copy()
            selection_sort(copia, clave)

        tiempos = timeit.repeat(stmt=wrapper, repeat=5, number=1)
        resultados.append({
            'algoritmo': 'Selection Sort',
            'archivo': archivo,
            'criterio': clave,
            'minimo': round(min(tiempos), 6),
            'promedio': round(sum(tiempos) / len(tiempos), 6),
            'maximo': round(max(tiempos), 6)
        })

    df = pd.DataFrame(resultados)
    df.to_csv(output_file, mode='a', header=debe_escribir_header, index=False)
    return resultados

def benchmark_bubble_sort(clave):
    archivos = ['data/gastos_50.csv', 'data/gastos_100.csv', 'data/gastos_1000.csv']
    resultados = []
    output_file = 'data/benchmark_bubble_sort.csv'
    debe_escribir_header = not os.path.exists(output_file)

    for archivo in archivos:
        try:
            datos = cargar_gastos_csv(archivo)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")
            continue

        def wrapper():
            copia = datos.copy()
            bubbleSort(copia, clave)

        tiempos = timeit.repeat(stmt=wrapper, repeat=5, number=1)
        resultados.append({
            'algoritmo': 'Bubble Sort',
            'archivo': archivo,
            'criterio': clave,
            'minimo': round(min(tiempos), 6),
            'promedio': round(sum(tiempos) / len(tiempos), 6),
            'maximo': round(max(tiempos), 6)
        })

    df = pd.DataFrame(resultados)
    df.to_csv(output_file, mode='a', header=debe_escribir_header, index=False)
    return resultados