from logging import root
import tkinter as tk
from tkinter import filedialog


    
def carregar_arquivo():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Abre a caixa de diálogo para selecionar arquivos
    arquivo = filedialog.askopenfilename(
        title="Selecionar arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*")]
    )

    # Verifica se um arquivo foi selecionado
    if arquivo:
        return arquivo
        # Faça o que precisar com o arquivo selecionado, como abrir, ler ou processar
    else:
        print("Nenhum arquivo PDF selecionado.")

def selecionar_pasta():
    root = tk.Tk()
    root.withdraw()

    destino = filedialog.askdirectory(
        title="Selecionar destino"
    )

    if destino:
        return destino
        # Faça o que precisar com o arquivo selecionado, como abrir, ler ou processar
    else:
        print("Nenhum destino selecionado.")

def selecionar_arquivo_txt():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Abre a caixa de diálogo para selecionar arquivos
    arquivo = filedialog.askopenfilename(
        title="Selecionar arquivo de texto",
        filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
    )

    # Verifica se um arquivo foi selecionado
    if arquivo:
        print("Arquivo de texto selecionado:", arquivo)
        # Faça o que precisar com o arquivo selecionado, como abrir, ler ou processar
    else:
        print("Nenhum arquivo de texto selecionado.")

def selecionar_arquivo_ph5():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Abre a caixa de diálogo para selecionar arquivos
    arquivo = filedialog.askopenfilename(
        title="Selecionar arquivo PH5",
        filetypes=[("Arquivos PH5", "*.ph5"), ("Todos os arquivos", "*.*")]
    )

    # Verifica se um arquivo foi selecionado
    if arquivo:
        print("Arquivo PH5 selecionado:", arquivo)
        # Faça o que precisar com o arquivo selecionado, como abrir, ler ou processar
    else:
        print("Nenhum arquivo PH5 selecionado.")

def criar_arquivo_txt():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Abre a caixa de diálogo para salvar o arquivo
    arquivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
    )

    # Verifica se um nome de arquivo foi especificado
    if arquivo:
        with open(arquivo, 'w') as f:
            # Escreve algum conteúdo no arquivo, por exemplo:
            f.write("Este é um arquivo de texto criado pelo seu programa.")
        return arquivo
    else:
        print("Nenhum arquivo foi criado.")

def lista_para_string(lista):
    resultadoString = [str(element) for element in lista]
    delimiter = ", "
    resultadoString = delimiter.join(resultadoString)
    return resultadoString
