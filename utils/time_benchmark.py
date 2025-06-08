import timeit
from sorting.bubble_sort import bubbleSort
from sorting.selection_sort import selection_sort,cargar_gastos_csv
import pandas as pd
import os

def benchmark_selection_sort(clave):
    archivos = ['data/gastos_50.csv', 'data/gastos_100.csv', 'data/gastos_1000.csv']
    resultados = []

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
        minimo = min(tiempos)
        promedio = sum(tiempos)/len(tiempos)
        maximo = max(tiempos)

        resultados.append({
    'algoritmo': 'Selection Sort',
    'archivo': archivo,
    'criterio': clave,
    'minimo': round(minimo, 6),
    'promedio': round(promedio, 6),
    'maximo': round(maximo, 6)
})

    df = pd.DataFrame(resultados)
    output_file = 'data/benchmark_resultados.csv'

    if os.path.exists(output_file):
        df.to_csv(output_file, mode='a', header=False, index=False)
    else:
        df.to_csv(output_file, mode='w', header=True, index=False)

    return resultados



def benchmark_bubble_sort(clave):
    archivos = ['data/gastos_50.csv', 'data/gastos_100.csv', 'data/gastos_1000.csv']
    resultados = []

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
        minimo = min(tiempos)
        promedio = sum(tiempos)/len(tiempos)
        maximo = max(tiempos)

        resultados.append({
    'algoritmo': 'Bubble Sort',
    'archivo': archivo,
    'criterio': clave,
    'minimo': round(minimo, 6),
    'promedio': round(promedio, 6),
    'maximo': round(maximo, 6)
})

    df = pd.DataFrame(resultados)
    output_file = 'data/benchmark_resultados.csv'

    if os.path.exists(output_file):
        df.to_csv(output_file, mode='a', header=False, index=False)
    else:
        df.to_csv(output_file, mode='w', header=True, index=False)

    return resultados


