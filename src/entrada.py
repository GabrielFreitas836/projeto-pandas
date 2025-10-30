"""
    programa: entrada.py
    autor: Gabriel Freitas
    data: 21/10/2025
    descrição: leitura e validação de arquivos
"""

import pandas as pd
import time
from tabulate import tabulate
import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

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
                    conn = self.ler_mysql()
                    while True:
                        if conn is not None:
                            cursor = conn.cursor()
                            cursor.execute("""
                                SELECT TABLE_NAME 
                                FROM INFORMATION_SCHEMA.TABLES 
                                WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = %s
                            """, (conn.database,))
                            tables = [t[0] for t in cursor.fetchall()]

                            print(tabulate([[t] for t in tables], headers = ["Tabelas"], tablefmt = "fancy_grid"))
                            time.sleep(0.3)
                            print("\n")
                            table_name = input(f"Escolha uma das tabelas de {conn.database}: ")
                            time.sleep(0.3)
                            print("Procurando arquivo...")
                            time.sleep(0.8)

                            if table_name in tables:
                                query = f"SELECT * FROM `{table_name}`"
                                df_table = pd.read_sql(query, conn)

                                if df_table.empty:
                                    time.sleep(0.3)
                                    print("Tabela vazia")
                                    break
                                else:
                                    print("Exibindo arquivo...")
                                    print(tabulate(df_table.head(), headers = 'keys', tablefmt = "fancy_grid"))
                                    break
                            else:
                                print("Tabela não encontrada! Tente novamente!")
                                time.sleep(0.8)
                                continue

                    cursor.close()
                    conn.close()
                    break
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
                print(tabulate(frame.head(), headers = "keys", tablefmt = "fancy_grid"))
                return True
            else:
                print("Arquivo vazio! Escolha outro arquivo...")
                time.sleep(0.8)
                return False
                
                
        except Exception as error:
            print("Erro de execução: ", error)

    def ler_mysql(self):
        try:
            print("=" *50)
            database_name = input("Digite o nome do banco: ").lower()
            self.conn = mysql.connector.connect(
                host = os.getenv('DB_HOST'),
                user = os.getenv('DB_USER'),
                password = os.getenv('DB_PASSWORD'),
                database = database_name
            )
            if self.conn.is_connected():
                print(f"Conexão com banco {self.conn.database} realizada com sucesso!\n")
                return self.conn
            else:
                print("Não foi possível realizar a conexão!")
                return None
        except mysql.connector.DatabaseError as error:
            print("Erro de banco: ", error)
        except mysql.connector.InterfaceError as error:
            print("Erro de interface do banco: ", error)
        except mysql.connector.InternalError as error:
            print("Erro interno de banco: ", error)
        except Exception as error:
            print("Erro de execução: ", error)
