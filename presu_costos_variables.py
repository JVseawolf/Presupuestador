import tkinter as tk

class CostosVar:
    def __init__(self, id, item="", valor_jornada=0, q_jornadas=0, total=0):
        self.id = id
        self.item = item
        self.valor_jornada = valor_jornada
        self.q_jornadas = q_jornadas
        self.total = total

costos_variables = {}

for i in range(1,13):
    costos_variables[i] = CostosVar(i)

def registrar_costo(id):
    precio_str = entry_valor[id].get()
    precio_int = int(precio_str)    
    q_str = entry_q_jornadas[id].get()
    q_int = int(q_str)
    costos_variables[id].item = entry_item[id].get()
    costos_variables[id].valor_jornada = precio_int
    costos_variables[id].q_jornadas = q_int
    costos_variables[id].total = costos_variables[id].valor_jornada * costos_variables[id].q_jornadas
    actualizar_etiquetas()
    actualizar_presu()

def actualizar_etiquetas():
    for idx in (costos_variables):
        etiquetas_totales[idx].config(text=f"${costos_variables[idx].total}")

def actualizar_presu():
    parcial_costos_variables = 0
    for i in costos_variables:
        parcial_costos_variables += costos_variables[i].total


# Crear ventana
ventana = tk.Tk()
ventana.title("Presupuesto Costos Variables")
# Centrar ventana en la pantalla
ancho_ventana = 500
alto_ventana = 600
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

id_costo = []
etiquetas_totales = {}
entry_item = {}
entry_valor = {}
entry_q_jornadas = {}

for id in costos_variables:
    contenedor = tk.Frame(ventana)
    contenedor.pack(anchor="w", fill="x")

    boton_aplicar_costo = tk.Button(contenedor, text="Aplicar", command=lambda id=id: registrar_costo(id))
    boton_aplicar_costo.pack(anchor="e", side="right", padx=10)

    etiqueta_id = tk.Label(contenedor, text=f"{id}", font=("Arial", 10))
    etiqueta_id.pack(anchor="w", side="left")
    id_costo.append(etiqueta_id)

    etiqueta_item = tk.Label(contenedor, text="Item", font=("Arial", 10))
    etiqueta_item.pack(anchor="w", side="left")

    celda_item = tk.Entry(contenedor)
    celda_item.pack(anchor="w", side="left", fill="x")
    entry_item[id] = celda_item

    etiqueta_item = tk.Label(contenedor, text="$", font=("Arial", 10))
    etiqueta_item.pack(anchor="w", side="left")

    celda_valor_jornada = tk.Entry(contenedor, width=7)
    celda_valor_jornada.pack(anchor="w", side="left")
    celda_valor_jornada.insert(0, "0")
    entry_valor[id] = celda_valor_jornada

    etiqueta_item = tk.Label(contenedor, text="Q", font=("Arial", 10))
    etiqueta_item.pack(anchor="w", side="left")

    celda_q_jornadas = tk.Entry(contenedor, width=2)
    celda_q_jornadas.pack(anchor="w", side="left")
    celda_q_jornadas.insert(0, "0")
    entry_q_jornadas[id] = celda_q_jornadas

    etiqueta_total = tk.Label(contenedor, text=f"${costos_variables[id].total}", font=("Arial", 14))
    etiqueta_total.pack(side="right")
    etiquetas_totales[id] = etiqueta_total


ventana.mainloop()