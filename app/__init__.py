from flask import Flask 
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from .models import db, User

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'suachavesecretaaqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskflow.db'

    db.init_app(app)
    
    Migrate(app,db)

    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    from .routes import main
    app.register_blueprint(main)

    return app
