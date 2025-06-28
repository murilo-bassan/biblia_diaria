# app.py
from flask import Flask, jsonify, render_template
import json
import os
from datetime import date
import requests

print("Iniciando a aplicação Flask...") 
app = Flask(__name__)

print(f"Flask app instanciado. app.root_path: {app.root_path}")

@app.route('/')
def index():
    print("Rota '/' acessada.") 
    verse_file_path = os.path.join(app.root_path, "daily_verse.json")

    daily_verse_data = {
        "verse": "O versículo do dia ainda não foi carregado. Por favor, tente novamente mais tarde.",
        "date": str(date.today().strftime('%d/%m/%Y'))
    }

    if os.path.exists(verse_file_path):
        try:
            with open(verse_file_path, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
                if 'verse' in loaded_data and 'date' in loaded_data:
                    daily_verse_data['verse'] = loaded_data['verse']
                    try:
                        date_obj = date.date.fromisoformat(loaded_data['date']) 
                        daily_verse_data['date'] = date_obj.strftime('%d/%m/%Y')
                    except ValueError:
                        daily_verse_data['date'] = loaded_data['date']
                else:
                    print(f"Atenção: Arquivo '{verse_file_path}' não contém 'verse' ou 'date'.")
        except json.JSONDecodeError:
            print(f"Erro ao decodificar JSON do arquivo '{verse_file_path}'. O arquivo pode estar corrompido.")
        except Exception as e:
            print(f"Erro ao ler o arquivo '{verse_file_path}': {e}")
    else:
        print(f"Arquivo '{verse_file_path}' não encontrado. O versículo será exibido como padrão.")

    return render_template('index.html', verse=daily_verse_data['verse'], date=daily_verse_data['date'])

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/get_new_verse')
def get_new_verse():
    try:
        # Chama a API da Bíblia diretamente (como no update_verse.py)
        # Usei o mesmo parâmetro translation=almeida para português
        response = requests.get("https://bible-api.com/?random=verse&translation=almeida")
        response.raise_for_status() # Lança exceção para erros HTTP (4xx ou 5xx)
        data = response.json()

        verse_text = data.get('text', 'Versículo não encontrado.')
        reference = data.get('reference', 'Referência desconhecida.')

        # Retorna os dados como JSON para o JavaScript no frontend
        return jsonify(text=verse_text, reference=reference)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar novo versículo: {e}")
        return jsonify(text="Erro ao carregar versículo.", reference=""), 500 # Retorna erro HTTP 500
    except json.JSONDecodeError:
        print("Erro ao decodificar JSON da API.")
        return jsonify(text="Erro na resposta da API.", reference=""), 500
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return jsonify(text="Erro inesperado ao carregar versículo.", reference=""), 500



if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get("PORT", 5000))