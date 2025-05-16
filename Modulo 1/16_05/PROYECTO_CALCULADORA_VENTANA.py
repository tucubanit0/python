import tkinter as tk
from tkinter import messagebox

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
                messagebox.showerror("Error", "No se puede dividir por cero.")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Error", "Seleccione una operación.")
            return
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos.")
        
def limpiar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_resultado.config(text="Resultado:")
    operacion_var.set("Suma")

def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Calculadora Básica")

tk.Label(ventana, text="Primer número:").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Segundo número:").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

operacion_var = tk.StringVar(value="Suma")
opciones = ["Suma", "Resta", "Multiplicación", "División"]
tk.Label(ventana, text="Operación:").grid(row=2, column=0, padx=5, pady=5)
menu_operacion = tk.OptionMenu(ventana, operacion_var, *opciones)
menu_operacion.grid(row=2, column=1, padx=5, pady=5)

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.grid(row=3, column=0, padx=5, pady=5)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.grid(row=3, column=1, padx=5, pady=5)

btn_salir = tk.Button(ventana, text="Salir", command=salir)
btn_salir.grid(row=4, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.grid(row=5, column=0, columnspan=2, pady=5)

ventana.mainloop()