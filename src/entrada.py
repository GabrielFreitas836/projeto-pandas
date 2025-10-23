"""
    programa: entrada.py
    autor: Gabriel Freitas
    data: 21/10/2025
    descrição: leitura e validação de arquivos
"""

import pandas as pd
import time

class Entrada:
    def menu(self):
        while True:
            print("=" *50, "\n")
            print("Olá, seja bem-vindo!\n")
            print("=" *50, "\n")

            time.sleep(0.8)

            print("[1] - Ler arquivo de Excel\n[2] - Ler arquivo de banco MySQL\n[3] - Sair do programa\n")
            opcao = int(input("Escolha uma das opções acima: "))

            match opcao:
                case 1:
                    arquivo_excel = self.ler_excel()

                    if arquivo_excel:
                        break
                    else:
                        continue
                case 2:
                    self.ler_mysql()
                case 3:
                    print("Saindo do programa...")
                    time.sleep(0.8)
                    break
                case _:
                    print("Opção inválida! Tente novamente...")
                    time.sleep(1)
                    continue
    
    def ler_excel(self):
        try:
            print("=" *50)
            caminho_arquivo = input("Digite um caminho de arquivo válido: ")
            frame = pd.read_excel(caminho_arquivo)
            print("Procurando arquivo...")
            time.sleep(0.5)

            if not frame.empty:
                print("=" *50)
                print("Exibindo arquivo encontrado...")
                time.sleep(0.5)
                print(frame.head())
                return True
            else:
                print("Arquivo vazio! Escolha outro arquivo...")
                time.sleep(0.8)
                return False
                
                
        except Exception as error:
            print("Erro de execução: ", error)

    def ler_mysql():
        pass
