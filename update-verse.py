# update_verse.py
import requests
import json
import os
from datetime import date

# Função para buscar o versículo
def get_daily_verse():
    """
    Busca um versículo aleatório da API bible-api.com.
    Para uma API que forneça especificamente um "versículo do dia",
    a lógica de requisição pode precisar ser ajustada.
    """
    try:
        # A API bible-api.com não tem um endpoint "versículo do dia" direto.
        # Vamos usar o endpoint de versículo aleatório para simplificar.
        # Se você encontrar uma API com "versículo do dia", adapte esta parte.
        response = requests.get("https://bible-api.com/?random=verse")
        response.raise_for_status() # Lança exceção para erros HTTP
        data = response.json()

        # A estrutura da resposta pode variar. Adapte se a API que você usar for diferente.
        # Exemplo de estrutura de bible-api.com:
        # { "text": "...", "reference": "..." }
        verse_text = data.get('text', 'Versículo não encontrado.')
        reference = data.get('reference', 'Referência desconhecida.')

        return f"{verse_text} - {reference}"
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao buscar versículo: {e}")
        return "Erro ao conectar com a API. Tente novamente mais tarde."
    except json.JSONDecodeError:
        print("Erro ao decodificar JSON da API.")
        return "Erro na resposta da API. Tente novamente mais tarde."
    except Exception as e:
        print(f"Erro inesperado ao buscar versículo: {e}")
        return "Ocorreu um erro inesperado ao carregar o versículo."

def main():
    """
    Função principal que busca o versículo e o salva em um arquivo JSON.
    """
    daily_verse = get_daily_verse()

    # Define o caminho para o arquivo daily_verse.json.
    # O script assume que está sendo executado no diretório raiz do projeto.
    # Para o Render, isso funcionará bem.
    project_root = os.path.dirname(os.path.abspath(__file__))
    verse_file_path = os.path.join(project_root, "daily_verse.json")

    # Cria/sobrescreve o arquivo JSON com o versículo do dia e a data atual.
    with open(verse_file_path, 'w', encoding='utf-8') as f:
        json.dump({"date": str(date.today()), "verse": daily_verse}, f, ensure_ascii=False, indent=4)
    print(f"Versículo atualizado e salvo em {verse_file_path}: {daily_verse}")

if __name__ == "__main__":
    main()