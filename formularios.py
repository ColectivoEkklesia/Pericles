from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    """Formulario para el inicio de sesión."""
    nombre_usuario = StringField('Nombre de usuario', validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    recordar = BooleanField('Recordarme')
    submit = SubmitField('Iniciar sesión')


class InitiativeTitleForm(FlaskForm):
    """Formulario para el título de la iniciativa."""
    titulo = StringField('Título', validators=[DataRequired(), Length(min=5, max=255)])

class InitiativeAuthorsForm(FlaskForm):
    """Formulario para los autores de la iniciativa."""
    autores = TextAreaField('Autores', validators=[DataRequired()])

class InitiativeExpositionForm(FlaskForm):
    """Formulario para la exposición de motivos de la iniciativa."""
    exposicion_motivos = TextAreaField('Exposición de motivos', validators=[DataRequired()])

class InitiativeChapterForm(DynamicForm):
    """Formulario para un capítulo de la iniciativa."""
    titulo_capitulo = StringField('Título del capítulo', validators=[DataRequired()])
    secciones = FieldList(FormField(InitiativeSectionForm))

class InitiativeSectionForm(DynamicForm):
    """Formulario para una sección de la iniciativa."""
    titulo_seccion = StringField('Título de la sección', validators=[DataRequired()])
    articulos = FieldList(FormField(InitiativeArticleForm))

class InitiativeArticleForm(Form):
    """Formulario para un artículo de la iniciativa."""
    numero_articulo = StringField('Número de artículo', validators=[DataRequired()])
    contenido_articulo = TextAreaField('Contenido del artículo', validators=[DataRequired()])

class CreateInitiativeForm(FlaskForm):
    """Formulario completo para crear una iniciativa (propuesta de ley)."""
    titulo_iniciativa = FormField(InitiativeTitleForm)
    autores_iniciativa = FormField(InitiativeAuthorsForm)
    exposicion_motivos_iniciativa = FormField(InitiativeExpositionForm)
    capitulos_iniciativa = FieldList(FormField(InitiativeChapterForm))
    submit = SubmitField('Crear iniciativa')
