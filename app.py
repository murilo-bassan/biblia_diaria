# app.py
from flask import Flask, render_template
import json
import os
from datetime import date

print("Iniciando a aplicação Flask...") # Adicione esta linha

app = Flask(__name__)

print(f"Flask app instanciado. app.root_path: {app.root_path}") # Adicione esta linha

@app.route('/')
def index():
    print("Rota '/' acessada.") # Adicione esta linha
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
                        date_obj = date.date.fromisoformat(loaded_data['date']) # Corrigido para date.date.fromisoformat
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

if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get("PORT", 5000))