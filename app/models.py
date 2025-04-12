from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

#Modelo de usuário para autenticação e associação de tarefas
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #ID único do usuário
    username = db.Column(db.String(150), unique=True, nullable=False) #Username único do usuário e obrigatório
    password_hash = db.Column(db.String(150), nullable=False) #Senha obrigatória e que será criptografada

    def set_password(self, password):
        '''Define a senha criptografando-a antes de salvar'''
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''Verifica se a senha informada corresponde ao hash armazenado'''
        return check_password_hash(self.password_hash, password)
    
#Modelo para as tarefas criadas pelo usuário
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) #ID único da tarefa
    title = db.Column(db.String(120), nullable=False) #Título da tarefa obrigatório
    description = db.Column(db.Text, nullable=True) #Descrição da tarefa opcional
    created_at = db.Column(db.DateTime, default=datetime.utcnow) #Data de criação da tarefa, com padrão da hora atual na criação
    completed = db.Column(db.Boolean, default=False) #Informa se a tarefa está completa ou não com padrão de não completa
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #Atribui a tarefa ao usuário que a criou
    
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def __repr__(self):
        return f'<Task {self.title}>'
