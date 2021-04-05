from flask import *

app = Flask('app')

@app.route('/')
def hello_world():
    return 'Trabalho 2 - use a rota "/sum" para utilizar a função de soma'

@app.route('/sum', methods=['POST', 'GET'])
def sum():
    error = None
    if request.method == 'POST':        
        print(float(request.form['number']) + 2)
        result = float(request.form['number']) + 2
        return render_template('sum.html', error=error, txt=result)

    return render_template('sum.html', error=error)

app.run(port=8080)
