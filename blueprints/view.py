# blueprints\view.py
# Exibe um único registro (pad) com detalhes

import sqlite3
from flask import Blueprint, render_template, request
from database import DB_NAME

view_bp = Blueprint('view', __name__)


@view_bp.route("/view/<int:pad_id>")
def search_page(pad_id):

    # Lê o cookie 'owner_uid'
    owner_uid = request.cookies.get('owner_uid')

    # Conecta ao banco de dados
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # SQL de consulta com preparated query
    cursor.execute('''
        SELECT 
            pads.*, own_id, own_display_name, own_photo_url, own_status
        FROM pads
        INNER JOIN owners ON pad_owner = own_uid
        WHERE pad_id = ? AND pad_status = 'ON'
    ''', (pad_id,))

    # Obtém o resultado da conulta
    row = cursor.fetchone()
    
    print('\n\n\n', row['pad_title'])
    print(pad_id, owner_uid,'\n\n\n')
    
    return render_template("view.html")
