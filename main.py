from sorting.selection_sort import cargar_gastos_csv, selection_sort
from utils.time_benchmark import benchmark_bubble_sort, benchmark_selection_sort


# gastos = cargar_gastos_csv('data/gastos_50.csv')
# gastos_ordenados = selection_sort(gastos, 'monto')
# for gasto in gastos_ordenados[:10]:  # mostrar solo los primeros 10
#     print(gasto)

# benchmark_selection_sort('fecha')
# benchmark_selection_sort('descripcion')
# benchmark_selection_sort('monto')
# benchmark_selection_sort('mes')   


benchmark_bubble_sort('fecha')
benchmark_bubble_sort('descripcion')
benchmark_bubble_sort('monto')
benchmark_bubble_sort('mes')  