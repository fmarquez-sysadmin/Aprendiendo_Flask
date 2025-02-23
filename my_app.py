from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = "Camilo"
    friends = ['Fabio', 'Kevin', 'Andres']
    return render_template('index.html', name = name, friends = friends)


@app.route('/my_app')
@app.route('/my_app/<name>')
@app.route('/my_app/<name>/<int:age>')
def my_app(name = None, age = None):
    
    if name == None and age == None:
        return '<h1>No hay edad<h1>'
    elif age == None:
        return f'<h1>Hola,{name}</h1>'
    else:
        return f'<h1>Hola, tu nombre es {name} y tu edad es {age}!</h1>'
    
from markupsafe import escape    
@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'