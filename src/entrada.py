"""
    programa: entrada.py
    autor: Gabriel Freitas
    data: 21/10/2025
    descrição: leitura e validação de arquivos
"""

import pandas as pd

class Entrada:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        