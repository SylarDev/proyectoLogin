from dbAppConfig import basededatos,gestor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@gestor.user_loader
def load_user(Usuario_id):
    return Usuario.query.get(Usuario_id)

class Usuario(basededatos.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    email = basededatos.Column(basededatos.String(64), unique=True, index=True)
    nombre = basededatos.Column(basededatos.String(64), unique=True, index=True)
    password_encriptada = basededatos.Column(basededatos.String(128))

    def __init__(self,email,nombre,password):
        self.email = email
        self.nombre = nombre
        self.password_encriptada = generate_password_hash(password)

    def verificar_password(self,password):
        return check_password_hash(self.password_encriptada,password)
