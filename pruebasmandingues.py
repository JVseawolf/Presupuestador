import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana con contenedores izquierdo y derecho")

# Crear el contenedor principal
contenedor_principal = tk.Frame(ventana)
contenedor_principal.pack(fill="both", expand=True)

# Crear el contenedor izquierdo
contenedor_izquierdo = tk.Frame(contenedor_principal, bg="red")
contenedor_izquierdo.pack(side="left", fill="both", expand=True)

# Crear el contenedor derecho
contenedor_derecho = tk.Frame(contenedor_principal, bg="blue")
contenedor_derecho.pack(side="right", fill="both", expand=True)

# Agregar widgets al contenedor izquierdo
etiqueta_izquierda = tk.Label(contenedor_izquierdo, text="Contenedor Izquierdo", font=("Arial", 16))
etiqueta_izquierda.pack(pady=20)

boton_izquierdo = tk.Button(contenedor_izquierdo, text="Botón Izquierdo")
boton_izquierdo.pack()

# Agregar widgets al contenedor derecho
etiqueta_derecha = tk.Label(contenedor_derecho, text="Contenedor Derecho", font=("Arial", 16))
etiqueta_derecha.pack(pady=20)

boton_derecho = tk.Button(contenedor_derecho, text="Botón Derecho")
boton_derecho.pack()

ventana.mainloop()
