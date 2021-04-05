from flask import *

app = Flask('app')

@app.route('/')
def hello_world():
    return 'Tarefa6 - use a rota com o número que deseja somar Ex: "/10" realiza a soma 10 + 2'

@app.route('/<number>')
def number(number):
    result = float(number) + 2
    return f'O Resultado é: {result}'
    
app.run(port=8080)
