def bubbleSort(gastos, clave):
    n = len(gastos)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if(gastos[j+1][clave] < gastos[j][clave]):
              gastos[j][clave], gastos[j+1][clave] = gastos[j+1][clave], gastos[j][clave]
    return gastos