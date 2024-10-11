from flask import Flask 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import render_template

# create a function that creates a web application
# a web server will run this web application

db = SQLAlchemy()

def create_app():
    print(__name__)  # let us be curious - what is this __name__
    app = Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug = True
    Bootstrap(app)
    app.secret_key = 'asecret'

    # initialise the login manager
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traveldb.sqlite'
    db.init_app(app)

    # config upload folder
    UPLOAD_FOLDER = '/static/img'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("error.html")


    # add the Blueprint
    from . import views
    app.register_blueprint(views.mainbp)
    from . import destinations
    app.register_blueprint(destinations.destbp)
    from . import auth
    app.register_blueprint(auth.authbp)
    return app
    
