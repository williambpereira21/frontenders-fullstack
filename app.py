# app.py
from flask import Flask, render_template
from database import init_db
from blueprints.owner import owner_bp
from blueprints.main import main_bp
from blueprints.contacts import contacts_bp
from blueprints.newpad import newpad_bp

app = Flask(__name__)

# Inicializa o banco de dados ao iniciar o aplicativo
init_db()

# Registra o blueprint para as rotas de owner
app.register_blueprint(owner_bp, url_prefix='/owner')

# Registra o blueprint para as rotas principais
app.register_blueprint(main_bp)             # Página inicial
app.register_blueprint(contacts_bp)         # Página de contatos
app.register_blueprint(newpad_bp)           # Novo Pad


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/privacy")
def privacy_page():
    return render_template("privacy.html")


@app.route("/search")
def search_page():
    return render_template("search.html")


if __name__ == '__main__':
    app.run(debug=True)
