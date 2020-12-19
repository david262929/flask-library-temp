from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from flask_pymongo import PyMongo
# from flask_login import LoginManager


# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from flask_pymongo import PyMongo
# from flask_login import LoginManager

app = Flask(__name__, template_folder='../client/build') #,

app.config.from_object('app.configuration.DevelopmentConfig')

# bs = Bootstrap(app) #flask-bootstrap
# db = SQLAlchemy(app) #flask-sqlalchemy

# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'


from app import views, models
