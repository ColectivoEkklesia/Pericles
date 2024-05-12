from flask import render_template, redirect, url_for, flash, request, current_user
from pericles import modelos
from pericles.forms import LoginForm

@app.route('/')
def index():
    """Ruta para la página principal."""
    iniciativas = models.Iniciativa.query.order_by(models.Iniciativa.fecha_creacion.desc()).limit(10).all()
    return render_template('index.html', iniciativas=iniciativas)

@app.route('/iniciativa/<int:id_iniciativa>')
def detalle_iniciativa(id_iniciativa):
    """Ruta para el detalle de una iniciativa."""
    iniciativa = models.Iniciativa.query.get(id_iniciativa)
    if not iniciativa:
        flash('Iniciativa no encontrada.')
        return redirect(url_for('index'))
    return render_template('detalle_iniciativa.html', iniciativa=iniciativa)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Ruta para el inicio de sesión."""
    form = LoginForm()
    if form.validate_on_submit():
        usuario = models.Usuario.query.filter_by(nombre_usuario=form.nombre_usuario.data).first()
        if usuario and usuario.verificar_contrasena(form.contrasena.data):
            login_user(usuario, remember=form.recordar.data)
            flash('¡Inicio de sesión exitoso!')
            return redirect(url_for('index'))
        else:
            flash('Nombre de usuario o contraseña incorrectos.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    """Ruta para cerrar la sesión."""
    logout_user()
    flash('Sesión cerrada exitosamente.')
    return redirect(url_for('index'))

@app.route('/firmar/<int:id_iniciativa>', methods=['GET', 'POST'])
@login_required
def firmar_iniciativa(id_iniciativa):
    """Ruta para firmar una iniciativa."""
    iniciativa = models.Iniciativa.query.get(id_iniciativa)
    if not iniciativa:
        flash('Iniciativa no encontrada.')
        return redirect(url_for('index'))
    if models.Firma.query.filter_by(id_usuario=current_user.id, id_iniciativa=id_iniciativa).first():
        flash('Ya has firmado esta iniciativa.')
        return redirect(url_for('detalle_iniciativa', id_iniciativa=id_iniciativa))
    nueva_firma = models.Firma(id_usuario=current_user.id, id_iniciativa=id_iniciativa)
    iniciativa.firmas += 1
    db.session.add(nueva_firma)
    db.session.commit()
    flash('¡Has firmado la iniciativa exitosamente!')
    return redirect(url_for('detalle_iniciativa', id_iniciativa=id_iniciativa))

@app.route('/crear_iniciativa', methods=['GET', 'POST'])
@login_required
def crear_iniciativa():
    """Ruta para crear una iniciativa."""
    # Se agrega la importación del formulario correspondiente
    from pericles.forms import CreateInitiativeForm

    form = CreateInitiativeForm()
    if form.validate_on_submit():
        nueva_iniciativa = models.Iniciativa(
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            proponentes=form.proponentes.data,
            categoria=form.categoria.data
        )
        db.session.add(nueva_iniciativa)
        db.session.commit()
        flash('¡Iniciativa creada exitosamente!')
        return redirect(url_for('index'))
    return render_template('crear_iniciativa.html', form=form)
