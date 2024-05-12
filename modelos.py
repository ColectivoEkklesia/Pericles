from flask_sqlalchemy import SQLAlchemy

# Definición de la base de datos
db = SQLAlchemy()

class Usuario(db.Model):
    """Modelo para representar a los usuarios del sistema."""
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(64), unique=True, nullable=False)
    correo_electronico = db.Column(db.String(128), unique=True, nullable=False)
    contrasena_hash = db.Column(db.String(128), nullable=False)

    def establecer_contrasena(self, contrasena):
        """Establece la contraseña del usuario."""
        self.contrasena_hash = generate_password_hash(contrasena)

    def verificar_contrasena(self, contrasena):
        """Verifica la contraseña del usuario."""
        return check_password_hash(self.contrasena_hash, contrasena)

class Iniciativa(db.Model):
    """Modelo para representar a las iniciativas populares legislativas."""
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    proponentes = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(64), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(64), nullable=False, default='En curso')
    firmas = db.Column(db.Integer, default=0)

class Firma(db.Model):
    """Modelo para representar las firmas de apoyo a las iniciativas."""
    id = db.Column(db.Integer, primary_key=True)
    id_iniciativa = db.Column(db.Integer, db.ForeignKey('iniciativa.id'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fecha_firma = db.Column(db.DateTime, default=datetime.utcnow)
