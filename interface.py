import tkinter as tk
from tkinter import simpledialog

def main():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Entrada de dados
    user_input = simpledialog.askstring("Entrada de Dados", "Digite algo:")

    # Processamento e saída
    output_list = [user_input]  # Exemplo simples de processamento
    print("Saída:", output_list)

if __name__ == "__main__":
    main()
