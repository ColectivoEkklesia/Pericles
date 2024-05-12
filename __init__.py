from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

pericles = Flask(__name__)
pericles.config.from_pyfile('config.py')  # Carga la configuración desde config.py
db = SQLAlchemy(pericles)
login_manager = LoginManager()
login_manager.init_app(pericles)

from pericles import modelos  # Importa los modelos después de la inicialización de db

@app.context_processor
def inject_user():
    """Inyecta el usuario actual en el contexto de la plantilla"""
    return {'current_user': current_user}

from app import rutas  # Importa las rutas después de la inicialización de login_manager

if __name__ == '__main__':
    pericles.run(debug=True)
