
from flask import render_template, flash, request, url_for, redirect
from flask_login import login_user, login_required, logout_user

from formulario import Formulario_Registro, Formulario_Login
from modelos import Usuario
from dbAppConfig import app, basededatos
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def principal():
    return render_template('principal.html')

@app.route("/bienvenido")
@login_required
def bienvenido():
    return render_template('bienvenido.html')

@app.route("/salir")
@app.login_required
def salir():
    logout_user()
    flash('Sesion de usuario cerrada.')
    return redirect(url_for('principal'))

@app.route("/entrar", methods=['GET', 'POST'])
def entrar():
    formulario = Formulario_Login()
    if formulario.validate_on_submit():
        usuario =  Usuario.query.filter_by(email=formulario.email.data).first()
        if usuario is not None:
            if check_password_hash(usuario.password_encriptada, formulario.password.data):
                login_user(usuario)
                flash('Usuario ha entrado correctamente.')
                proxima_pagina = request.args.get('next')
                if proxima_pagina == None or not next[0] == '/':
                    proxima_pagina = url_for('bienvenido')
                return redirect(proxima_pagina)
            
    return render_template('entrar.html', formulario = formulario)

@app.route('/registrar', methods = ['GET', 'POST']) 
def registrar():
    formulario = Formulario_Registro()
    if formulario.validate_on_submit():
        usuario = Usuario(email = formulario.email.data, nombre = formulario.nombre.data,
                                   password = formulario.password.data)
        basededatos.session.add(usuario)
        basededatos.session.commit()
        flash('Usuario registrado correctamente.')
        return redirect(url_for('entrar'))
    
    return render_template('registrar.html', formulario = formulario)



if __name__ == '__main__':
    app.run(debug = True)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
                
                
                
                
        