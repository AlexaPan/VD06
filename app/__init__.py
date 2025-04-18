from flask import Flask

app = Flask(__name__)   # создаем экземпляр класса Flask

app.config['SECRET_KEY'] = 'MySecret_key'
from app import routes
