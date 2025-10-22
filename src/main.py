"""
    programa: main.py
    autor: Gabriel Freitas
    data: 20/10/2025
    descrição: entrada principal da execução do programa
"""

from entrada import Entrada

if __name__ == "__main__":
    try:
        c = Entrada()
        c.menu()
    except Exception as error:
        print("Erro: ", error)
        