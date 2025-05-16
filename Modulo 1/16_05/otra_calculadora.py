import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = operacion_var.get()

        if operacion == "Suma":
            resultado = num1 + num2
        elif operacion == "Resta":
            resultado = num1 - num2
        elif operacion == "Multiplicación":
            resultado = num1 * num2
        elif operacion == "División":
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = num1 / num2
        elif operacion == "Potencia":
            resultado = num1 ** num2
        elif operacion == "Módulo":
            resultado = num1 % num2
        else:
            raise ValueError("Operación no válida.")

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

def limpiar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_resultado.config(text="Resultado:")
    operacion_var.set(opciones[0])

def salir():
    ventana.destroy()

# Configuración de ventana
ventana = tk.Tk()
ventana.title("Calculadora Avanzada")
ventana.resizable(False, False)
ventana.configure(padx=10, pady=10)

# Widgets de entrada
ttk.Label(ventana, text="Primer número:").grid(row=0, column=0, sticky="w")
entry_num1 = ttk.Entry(ventana)
entry_num1.grid(row=0, column=1, pady=5)

ttk.Label(ventana, text="Segundo número:").grid(row=1, column=0, sticky="w")
entry_num2 = ttk.Entry(ventana)
entry_num2.grid(row=1, column=1, pady=5)

# Menú de operaciones
ttk.Label(ventana, text="Operación:").grid(row=2, column=0, sticky="w")
opciones = ["Suma", "Resta", "Multiplicación", "División", "Potencia", "Módulo"]
operacion_var = tk.StringVar(value=opciones[0])
menu_operacion = ttk.OptionMenu(ventana, operacion_var, *opciones)
menu_operacion.grid(row=2, column=1, pady=5)

# Botones
ttk.Button(ventana, text="Calcular", command=calcular).grid(row=3, column=0, pady=10)
ttk.Button(ventana, text="Limpiar", command=limpiar).grid(row=3, column=1, pady=10)
ttk.Button(ventana, text="Salir", command=salir).grid(row=4, column=0, columnspan=2, pady=5)

# Resultado
label_resultado = ttk.Label(ventana, text="Resultado:", font=("Arial", 12, "bold"))
label_resultado.grid(row=5, column=0, columnspan=2, pady=10)

ventana.mainloop()
