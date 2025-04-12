from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import RegisterForm, LoginForm, TaskForm
from .models import User, db, Task
from flask_login import login_user, logout_user, login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    '''Registra um novo usuário, verificando se o nome de usuário já está em uso'''
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Usuário já existe. Tente outro.')
            return redirect(url_for('main.register'))

        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form, title='Cadastro')

@main.route('/login', methods=['GET', 'POST'])
def login():
    '''Realiza login verificando usuário e senha'''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Usuário ou senha inválidos.')
    return render_template('login.html', form=form, title='Login')

@main.route('/logout')
@login_required
def logout():
    '''Sair da conta'''
    logout_user()
    flash('Você saiu da conta.')
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    '''Mostra o dashboard com as tarefas do usuário autenticado'''
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', title='Dashboard', user=current_user, tasks=tasks)

@main.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    '''Adiciona uma nova tarefa do usuário autenticado'''
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Tarefa criada com sucesso!')
        return redirect(url_for('main.dashboard'))
    return render_template('new_task.html', form=form, title='Nova Tarefa')

@main.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    '''Edita uma tarefa do usuário autenticado'''
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('Você não tem permissão para editar esta tarefa.')
        return redirect(url_for('main.dashboard'))
    
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.completed = form.completed.data
        db.session.commit()
        flash('Tarefa atualizada com sucesso!')
        return redirect(url_for('main.dashboard'))
    
    return render_template('edit_task.html', form=form, title='Editar Tarefa', task=task)

@main.route('/task/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    '''Deleta uma tarefa do usuário autenticado'''
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('Você não tem permissão para excluir esta tarefa.')
        return redirect(url_for('main.dashboard'))
    
    db.session.delete(task)
    db.session.commit()
    flash('Tarefa excluída com sucesso!')
    return redirect(url_for('main.dashboard'))