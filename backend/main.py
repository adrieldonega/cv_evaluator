import spacy
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import os

# Inicializa o aplicativo FastAPI
app = FastAPI()

# Carrega o modelo de PLN do Spacy uma vez ao iniciar a aplicação 
# disable=['parser', 'ner'] pode ser util caso precise de tokenização
nlp = spacy.load("pt_core_news_sm")

# --- Configuração CORS ---
# O CORS (Cross-Origin Resource Sharing) é necessário para permitir que seu frontend (Vue.js)
# que estará rodando em um endereço diferente, possa se comunicar com este backend.
# Para desenvolvimento, permitimos todas as origens. Em produção, você limitaria isso.
origins = [
    "http://localhost:8080",  # Endereço padrão do servidor de desenvolvimento do Vue.js
    "http://127.0.0.1:8080",
    # Adicione aqui os endereços de deploy do seu frontend quando for para produção (ex: "https://seufrotend.netlify.app")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)
# --- Fim Configuração CORS ---


# Função para extrair texto do PDF (AGORA FORA DAS ROTAS, NO NÍVEL SUPERIOR)
def extract_text_from_pdf(pdf_file_object):
    """
    Extrai todo o texto de um objeto de arquivo PDF.

    Args:
        pdf_file_object: O objeto de arquivo PDF (UploadFile).

    Returns:
        str: O texto extraído do PDF.
    """
    try:
        # pdfplumber pode abrir diretamente um objeto de arquivo
        with pdfplumber.open(pdf_file_object.file) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() or ""
        return full_text
    except Exception as e:
        # Levanta uma exceção HTTP para o cliente com um erro 500
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro ao processar o PDF: {e}")

# Rota de teste simples (AGORA NO NÍVEL SUPERIOR DO ARQUIVO)
@app.get("/")
async def read_root():
    return {"message": "Bem-vindo ao Avaliador de Currículos! A API está funcionando."}

# Rota para fazer upload e processar o currículo (AGORA NO NÍVEL SUPERIOR DO ARQUIVO)
@app.post("/upload-cv/")
async def upload_cv(file: UploadFile = File(...)):
    """
    Recebe um arquivo PDF de currículo, extrai seu texto e retorna o conteúdo.
    """
    # Verifica se o arquivo é um PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Por favor, envie apenas arquivos PDF.")
    
    # Você pode opcionalmente salvar o arquivo temporariamente se precisar,
    # mas pdfplumber pode ler diretamente do objeto UploadFile.
    # Exemplo de salvamento temporário (útil para depuração ou se a biblioteca exigir um caminho de arquivo):
    # file_location = f"temp_{file.filename}"
    # with open(file_location, "wb+") as file_object:
    #     file_object.write(file.file.read())
    # # Agora chame extract_text_from_pdf com file_location
    # # Lembre-se de deletar o arquivo temporário depois: os.remove(file_location)

    try:
        # Extrai o texto do PDF
        extracted_text = extract_text_from_pdf(file)

        # --- Processamento com SpaCy ---
        doc = nlp(extracted_text) # Processa o texto com o modelo SpaCy

         # Exemplo de extração de entidades nomeadas (NER)
        # SpaCy tenta identificar entidades como Pessoas (PER), Organizações (ORG), Locais (LOC), etc.
        # Currículos geralmente não têm todas essas categorias, mas podem ter "PER" (nome), "ORG" (empresas), etc.
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Exemplo de extração de tokens e suas propriedades (para habilidades, por exemplo)
        # Isso é mais complexo e será aprimorado no futuro, mas aqui está um exemplo básico
        # de como pegar verbos ou substantivos que podem ser habilidades
        potential_skills = []
        for token in doc:
            # Exemplo: identificar palavras que são substantivos ou adjetivos e podem ser habilidades
            if token.pos_ in ["NOUN", "ADJ"] and len(token.text) > 2 and not token.is_stop and not token.is_punct:
                potential_skills.append(token.text)
        
         # Para simplificar agora, vamos apenas pegar um conjunto limitado de entidades
        # No Módulo 3.2, refinaremos isso para extrair informações mais estruturadas.
        extracted_info = {
            "entities": entities,
            "first_500_chars_for_debug": extracted_text[:500] + "..." if len(extracted_text) > 500 else extracted_text
        }

        # --- FIM Processamento com SpaCy ---

        
        # Aqui, no futuro, você adicionaria a lógica para:
        # 1. Avaliar o currículo
        # 2. Gerar uma nota (0-10)
        # 3. Gerar sugestões de melhoria (usando Gemini API)
        # 4. Buscar e sugerir vagas (usando MySQL)

        # Por enquanto, apenas retorna o texto extraído
        return JSONResponse(content={
            "filename": file.filename,
            "content_type": file.content_type,
            "extracted_text": extracted_text,
            "extracted_info": extracted_info,
            "message": "Currículo processado com sucesso! (PLN básico aplicado.)"
        })
    except HTTPException as e:
        raise e # Re-lança exceções HTTP já criadas
    except Exception as e:
        # Captura qualquer outra exceção e retorna um erro genérico 500
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")
