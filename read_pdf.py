import pdfplumber

def extract_text_from_pdf(pdf_path):
# Extrai todo o texto de um arquivo PDF.
#     Args:
#         pdf_path (str): O caminho para o arquivo PDF.
#     Returns:
#         str: O texto extraido do PDF, ou uma mensagem de erro
#

    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() or "" # Garante que adicione string vazia se a página não tiver texto
        return full_text
    except FileNotFoundError:
        return f"Erro: O arquivo '{pdf_path}' não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro ao ler o PDF: {e}"
    
if __name__ == "__main__":
    # Caminho para o seu arquivo PDF de exemplo
    pdf_file = "curriculo_exemplo.pdf"

    print(f"Tentando extrair texto de: {pdf_file}")
    extracted_content = extract_text_from_pdf(pdf_file)
    print("\n---Conteúdo do PDF ---")
    print(extracted_content)
    print("------------------------")
