from flask import Flask 
app = Flask(__name__)
css = ''' .imagem{display:block;margin:auto;width:100px; height:100px;} '''
html = '''<!doctype html>
<html>
	<title>titulo</title>
	<style type="text/css">
	{0}
	</style>
	<body>
		<img class="imagem" src="https://i.ytimg.com/vi/bJk7pYRSy38/maxresdefault.jpg">
	</body>
</html> '''
@app.route('/')
def index():
	print()
	return html.format(css)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port='8000')
