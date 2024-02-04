import tkinter as tk

# Funções para realizar as operações
def adicao():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado.set(num1 + num2)

def subtracao():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado.set(num1 - num2)

def multiplicacao():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado.set(num1 * num2)

def divisao():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 == 0:
        resultado.set("Erro: Divisão por zero!")
    else:
        resultado.set(num1 / num2)

# Configuração da janela
window = tk.Tk()
window.title("Calculadora")

# Variáveis de entrada
entry_num1 = tk.Entry(window, width=10)
entry_num2 = tk.Entry(window, width=10)
resultado = tk.StringVar()

# Rótulos e botões
label_num1 = tk.Label(window, text="Número 1:")
label_num2 = tk.Label(window, text="Número 2:")
label_resultado = tk.Label(window, text="Resultado:")

button_adicao = tk.Button(window, text="Adição", command=adicao)
button_subtracao = tk.Button(window, text="Subtração", command=subtracao)
button_multiplicacao = tk.Button(window, text="Multiplicação", command=multiplicacao)
button_divisao = tk.Button(window, text="Divisão", command=divisao)

# Layout dos widgets
entry_num1.grid(row=0, column=1)
entry_num2.grid(row=1, column=1)
label_num1.grid(row=0, column=0)
label_num2.grid(row=1, column=0)

label_resultado.grid(row=3, column=0)
resultado_label = tk.Label(window, textvariable=resultado)
resultado_label.grid(row=3, column=1)

button_adicao.grid(row=2, column=0)
button_subtracao.grid(row=2, column=1)
button_multiplicacao.grid(row=2, column=2)
button_divisao.grid(row=2, column=3)

# Iniciar a interface gráfica
window.mainloop()
