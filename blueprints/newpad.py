# blueprints/newpad.py
from flask import Blueprint, render_template, request, redirect, url_for
from database import DB_NAME
import sqlite3

newpad_bp = Blueprint('newpad', __name__)


@newpad_bp.route("/newpad")
def newpad_page():

    # EXEMPLO
    # Verifica se o cookie 'owner_uid' foi enviado com a requisição
    # Se não existir, redireciona para a home (ou uma página de login, se existir)
    if 'owner_uid' not in request.cookies:
        # Ajuste 'main.home_page' para o nome do blueprint/rota da home
        return redirect(url_for('main.home_page'))

    # EXEMPLO
    # Obtém o valor do UID do cookie
    owner_uid = request.cookies.get('owner_uid')

    # Aqui você pode usar o owner_uid para lógica adicional, como:
    # - Verificar no banco se o usuário existe e está ativo (exemplo abaixo)
    # - Passar o UID ou dados do usuário para o template (ex: para personalizar a página)

    # EXEMPLO
    # Consulta rápida no banco para obter dados do owner (opcional, para enriquecer o template)
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        'SELECT own_display_name, own_photo_url FROM owners WHERE own_uid = ? AND own_status = "ON"', (owner_uid,))
    user_data = cursor.fetchone()
    conn.close()

    if not user_data:
        # Se o UID não for válido ou usuário inativo, redireciona
        return redirect(url_for('main.home_page'))

    # Converte para dict para passar ao template
    user = dict(user_data) if user_data else None

    # Se o cookie existir e for válido, prossegue para renderizar a página
    # Passa o user (ou apenas o owner_uid) para o template newpad.html, se necessário
    return render_template("newpad.html", user=user)
