from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

app = Flask(__name__)
app.config['HOST'] = os.getenv('HOST')
app.config['PORT'] = os.getenv('PORT')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
