import PyPDF2
import re

def pdf_para_txt(caminhoPDF, destino):
    try:
        # Abrir o arquivo PDF
        with open(caminhoPDF, 'rb') as pdf_arquivo:
            # Criar um objeto leitor do PyPDF2
            leitor_pdf = PyPDF2.PdfReader(pdf_arquivo)
            
            # Inicializar uma string para armazenar o conteúdo do PDF
            conteudo = ""
            
            # Iterar sobre todas as páginas do PDF
            for pagina in range(len(leitor_pdf.pages)):
                # Extrair o texto da página atual e concatená-lo ao conteúdo
                conteudo += leitor_pdf.pages[pagina].extract_text()
            
            # Criar o arquivo de texto no destino especificado e escrever o conteúdo
            with open(destino, 'w', encoding='utf-8') as txt_arquivo:
                txt_arquivo.write(conteudo)
        
        print("PDF convertido para TXT com sucesso!")
    
    except Exception as e:
        print("Ocorreu um erro:", e)

def identificar_perguntas_respostas(caminho_txt):
    try:
        # Abrir o arquivo de texto
        with open(caminho_txt, 'r', encoding='utf-8') as txt_arquivo:
            # Ler o conteúdo do arquivo
            conteudo = txt_arquivo.read()
            
            # Definir expressões regulares para identificar perguntas e respostas
            regex_pergunta = r'(?:Q:|Question:|Pergunta:)\s*(.*?)(?:\n\n|\n\n\n|\Z)'
            regex_resposta = r'(?:A:|Answer:|Resposta:)\s*(.*?)(?=\n\n|\n\n\n|\Z)'
            
            # Encontrar todas as correspondências de perguntas e respostas no texto
            perguntas = re.findall(regex_pergunta, conteudo, re.IGNORECASE | re.DOTALL)
            respostas = re.findall(regex_resposta, conteudo, re.IGNORECASE | re.DOTALL)
            
            # Verificar se o número de perguntas é igual ao número de respostas
            if len(perguntas) != len(respostas):
                raise ValueError("O número de perguntas não é igual ao número de respostas.")
            
            # Criar uma lista de tuplas contendo perguntas e respostas correspondentes
            perguntas_respostas = [(pergunta.strip(), resposta.strip()) for pergunta, resposta in zip(perguntas, respostas)]
            
            return perguntas_respostas
    
    except Exception as e:
        print("Ocorreu um erro:", e)
        return None

