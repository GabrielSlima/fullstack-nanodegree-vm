from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello():
	return 'Hello world'
@app.route('/endereco_legal')
def falai():
	return '<h1>XABLAU</H1>'
@app.route('/user/<name>')
def perfil_usuario(name):
	return '<h1>HELLO, %s! </h1>' % name
if __name__ == '__main__':
	app.run(host='0.0.0.0',port='8000')
