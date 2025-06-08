from customtkinter import *
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import csv
from sorting.selection_sort import selection_sort  # usamos selection_sort
import os

def lanzar_interfaz():
    set_appearance_mode("light")
    set_default_color_theme("blue")

    gastos = []

    def cargar_gastos_csv(ruta_archivo):
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = [dict(fila) for fila in lector]
            for gasto in datos:
                gasto['monto'] = float(gasto['monto'])  # asegurar tipo
            return datos

    MESES_ES = {
        "January": "Enero", "February": "Febrero", "March": "Marzo", "April": "Abril",
        "May": "Mayo", "June": "Junio", "July": "Julio", "August": "Agosto",
        "September": "Septiembre", "October": "Octubre", "November": "Noviembre", "December": "Diciembre"
    }

    def mostrar_gastos():
        criterio = menu_criterio.get().lower()
        descendente = menu_direccion.get() == "Descendente"

        for fila in tabla.get_children():
            tabla.delete(fila)

        ordenados = selection_sort(gastos.copy(), criterio)
        if descendente:
            ordenados = ordenados[::-1]

        for g in ordenados:
            fecha = datetime.strptime(g['fecha'], "%Y-%m-%d")
            mes = MESES_ES[fecha.strftime("%B")]
            tabla.insert("", "end", values=(g['fecha'], mes, g['descripcion'], f"${g['monto']:.2f}"))

    def cargar_csv():
        archivo = filedialog.askopenfilename(
            initialdir="data",
            filetypes=[("CSV files", "*.csv")])
        if archivo:
            try:
                datos = cargar_gastos_csv(archivo)
                gastos.clear()
                gastos.extend(datos)
                mostrar_gastos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar:\n{e}")

    def abrir_ventana_agregar():
        ventana_sec = CTkToplevel()
        ventana_sec.title("Agregar Gasto")
        ventana_sec.geometry("400x350")
        ventana_sec.grab_set()

        CTkLabel(ventana_sec, text="Fecha (YYYY-MM-DD):").pack(pady=(10, 0))
        entrada_fecha = CTkEntry(ventana_sec)
        entrada_fecha.pack(pady=5)

        CTkLabel(ventana_sec, text="Descripción:").pack(pady=(10, 0))
        entrada_desc = CTkEntry(ventana_sec)
        entrada_desc.pack(pady=5)

        CTkLabel(ventana_sec, text="Valor ($):").pack(pady=(10, 0))
        entrada_monto = CTkEntry(ventana_sec)
        entrada_monto.pack(pady=5)

        def guardar():
            try:
                fecha = entrada_fecha.get().strip()
                descripcion = entrada_desc.get().strip()
                monto = float(entrada_monto.get().strip())
                datetime.strptime(fecha, "%Y-%m-%d")  # validar formato
                gastos.append({'fecha': fecha, 'descripcion': descripcion, 'monto': monto})
                mostrar_gastos()
                ventana_sec.destroy()
            except:
                messagebox.showerror("Error", "Datos inválidos. Formato correcto: fecha YYYY-MM-DD, monto numérico.")

        CTkButton(ventana_sec, text="Guardar Gasto", command=guardar).pack(pady=20)

    # Ventana principal
    ventana = CTk()
    ventana.title("Gestor de Gastos")
    ventana.geometry("800x600")
    ventana.resizable(False, False)

    # Filtros de orden
    orden_frame = CTkFrame(ventana)
    orden_frame.pack(pady=(15, 10))

    CTkLabel(orden_frame, text="Ordenar por:").pack(side="left", padx=5)
    menu_criterio = CTkOptionMenu(orden_frame, values=["Fecha", "Monto"])
    menu_criterio.set("Fecha")
    menu_criterio.pack(side="left", padx=5)

    CTkLabel(orden_frame, text="Dirección:").pack(side="left", padx=5)
    menu_direccion = CTkOptionMenu(orden_frame, values=["Ascendente", "Descendente"])
    menu_direccion.set("Ascendente")
    menu_direccion.pack(side="left", padx=5)

    CTkButton(orden_frame, text="Aplicar", command=mostrar_gastos).pack(side="left", padx=10)

    # Tabla
    tabla = ttk.Treeview(ventana, columns=("Fecha", "Mes", "Descripción", "Monto"), show="headings", height=15)
    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Mes", text="Mes")
    tabla.heading("Descripción", text="Descripción")
    tabla.heading("Monto", text="Monto")

    tabla.column("Fecha", width=100, anchor="center")
    tabla.column("Mes", width=100, anchor="center")
    tabla.column("Descripción", width=400, anchor="w")
    tabla.column("Monto", width=100, anchor="center")
    tabla.pack(fill="x", padx=20, pady=10)

    # Botones
    botones_frame = CTkFrame(ventana, fg_color="transparent")
    botones_frame.pack(pady=10)

    CTkButton(botones_frame, text="Agregar Gasto", command=abrir_ventana_agregar, width=160).pack(side="left", padx=10)
    CTkButton(botones_frame, text="Cargar desde CSV", command=cargar_csv, width=160).pack(side="left", padx=10)

    ventana.mainloop()