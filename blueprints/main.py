# blueprints/main.py
from flask import Blueprint, render_template
from database import DB_NAME
import sqlite3

main_bp = Blueprint('main', __name__)


@main_bp.route("/")
def home_page():

    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_NAME)
    # Obtém coleções como tuplas e registros como dicionários
    conn.row_factory = sqlite3.Row 
    # Ativa o cursor
    cursor = conn.cursor()

    # Executa a consulta
    cursor.execute('''
        SELECT
            pad_id, pad_created_at, pad_title,
            own_id, own_display_name, own_photo_url,
            SUBSTR(pad_content, 1, 30) || '...' AS pad_content_preview
        FROM pads
        INNER JOIN owners ON pad_owner = own_id 
            WHERE pad_status = 'ON'
            ORDER BY pad_created_at DESC;
    ''')

    # Variável com os dados retornados
    rows = cursor.fetchall()
    all_pads = [dict(row) for row in rows]

    # print('\n\n\n', all_pads[0][2], '\n\n\n') # Assim funciona
    print('\n\n\n', all_pads, '\n\n\n')  # Mas quero assim

    # Fecha a conexão
    conn.close()

    # Passa os resultados para a página HTML
    return render_template("home.html", all_pads=all_pads)
