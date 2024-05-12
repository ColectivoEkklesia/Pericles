from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')  # Carga la configuración desde config.py
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from app import models  # Importa los modelos después de la inicialización de db

@app.context_processor
def inject_user():
    """Inyecta el usuario actual en el contexto de la plantilla"""
    return {'current_user': current_user}

from app import routes  # Importa las rutas después de la inicialización de login_manager

if __name__ == '__main__':
    app.run(debug=True)
