# gastos_fijos.py
import tkinter as tk

class GastosFijos:
    def __init__(self, root):
        self.root = root

        # Agrega aquí las variables necesarias para el control de gastos fijos
        self.categorias = {
            "Alquiler": ["Alquiler"],
            "Servicios": ["Licencias Software", "Internet"],
            "Administrativo": ["Contador"],
            "Financieros": ["Cuotas"],
            "Impuestos": {
                "Ana": ["Monotributo", "IIBB"],
                "Her": ["Monotributo", "IIBB"],
                "Javi": ["Monotributo", "IIBB"],
                "Flor": ["Monotributo", "IIBB"],
            },
            "Amortización": ["Amortización de equipos"],
            "Operativos": ["Movilidad"],
            "Sueldos": ["Director de Negocios y Finanzas", "Director de Operaciones"],
        }

        self.control_gastos()

    def control_gastos(self):
        # Crea un frame para contener los renglones con sus respectivos valores editables
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=10)

        # Recorre las categorías y agrega los renglones al frame
        for categoria, subcategorias in self.categorias.items():
            if isinstance(subcategorias, list):
                costo_categoria = self.calcular_total_costo(subcategorias)
                self.agregar_renglon(frame, categoria, costo_categoria)
            else:
                for subcategoria, subcategoria_gastos in subcategorias.items():
                    costo_subcategoria = self.calcular_total_costo(subcategoria_gastos)
                    self.agregar_renglon(frame, f"{categoria} - {subcategoria}", costo_subcategoria)

        # Calcula el 10% de los gastos totales como Imprevistos
        imprevistos = self.calcular_imprevistos()
        self.agregar_renglon(frame, "Imprevistos", imprevistos)

    def agregar_renglon(self, frame, descripcion, valor):
        label = tk.Label(frame, text=descripcion, width=40, anchor="w")
        label.grid(row=frame.grid_size()[1], column=0, padx=5, pady=5)

        entry = tk.Entry(frame, width=10)
        entry.insert(0, f"{valor:.2f}")
        entry.grid(row=frame.grid_size()[1] - 1, column=1, padx=5, pady=5)

    def calcular_total_costo(self, gastos):
        # Agrega aquí la lógica para calcular el costo total para una categoría o subcategoría
        # Puedes utilizar tus propias variables y cálculos para obtener el costo
        return 1000  # Solo como ejemplo, debes reemplazarlo con los cálculos correctos

    def calcular_imprevistos(self):
        # Agrega aquí la lógica para calcular los imprevistos
        # Puedes utilizar tus propias variables y cálculos para obtener el porcentaje
        return 100  # Solo como ejemplo, debes reemplazarlo con los cálculos correctos