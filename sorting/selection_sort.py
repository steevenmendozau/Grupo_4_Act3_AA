import csv


def cargar_gastos_csv(ruta_archivo):
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        gastos = [dict(fila) for fila in lector]  # por si acaso aseguramos el tipo dict
        for gasto in gastos:
            gasto['monto'] = float(gasto['monto'])  # convertir a número
        return gastos

def selection_sort(gastos, clave):
    for i in range(len(gastos)):
        min_idx = i
        for j in range(i + 1, len(gastos)):
            if gastos[j][clave] < gastos[min_idx][clave]:
                min_idx = j
        gastos[i], gastos[min_idx] = gastos[min_idx], gastos[i]
    return gastos  