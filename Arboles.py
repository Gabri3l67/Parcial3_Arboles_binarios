import tkinter as tk
from tkinter import ttk
from ArbolBinario import ArbolBinario, Nodo, crear_arbol

def mostrar_resultado(resultado):
    resultado_label.config(text="Resultado: " + " → ".join(map(str, resultado)))

def realizar_recorrido(tipo_recorrido, tipo_arbol):
    arbol = crear_arbol(tipo_arbol)
    if tipo_recorrido == "Amplitud":
        resultado = arbol.amplitud()
    elif tipo_recorrido == "Preorden":
        resultado = arbol.preorden(arbol.raiz, [])
    elif tipo_recorrido == "Inorden":
        resultado = arbol.inorden(arbol.raiz, [])
    elif tipo_recorrido == "Postorden":
        resultado = arbol.postorden(arbol.raiz, [])
    mostrar_resultado(resultado)

# Interfaz gráfica con tkinter
ventana = tk.Tk()
ventana.title("Recorridos de Árbol Binario")

frame = ttk.Frame(ventana, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Selecciona el árbol:").grid(row=0, column=0, columnspan=2)

arbol_seleccionado = tk.IntVar()
arbol_seleccionado.set(1)

for i, texto in enumerate(["Árbol 1", "Árbol 2", "Árbol 3", "Árbol 4"], start=1):
    ttk.Radiobutton(frame, text=texto, variable=arbol_seleccionado, value=i).grid(row=i, column=0, sticky=tk.W)

ttk.Label(frame, text="Selecciona el tipo de recorrido:").grid(row=5, column=0, columnspan=2)

botones_recorridos = [
    ("Recorrido en Amplitud", "Amplitud"),
    ("Recorrido en Preorden", "Preorden"),
    ("Recorrido en Inorden", "Inorden"),
    ("Recorrido en Postorden", "Postorden"),
]

for idx, (texto, tipo) in enumerate(botones_recorridos, start=6):
    ttk.Button(frame, text=texto, command=lambda t=tipo: realizar_recorrido(t, arbol_seleccionado.get())).grid(row=idx, column=0, pady=5, padx=5)

resultado_label = ttk.Label(frame, text="Resultado: ")
resultado_label.grid(row=10, column=0, columnspan=2)

ventana.mainloop()
