from http.server import BaseHTTPRequestHandler, HTTPServer
import operations
import cgi
import sys
import re
import urllib.parse as urlparse


class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith('/'):
				self.send_response(200)
				self.send_header('content-type','text/html')
				self.end_headers()
				dados = operations.readAllRestaurantData()
				print(dados)
				output = ''
				output = '''<!doctype html>
<html>
	<head>
		<meta charset='utf-8'>
	</head>
	<style>
		article {{
			border: 1px solid blue;
			width: 50%;
			margin: 0 auto;
		}}
	</style>
	<body>
		<main>
			{0}
		</main>
	</body>
</html>'''
				restaurants = ''
				pre_output = ''
				restaurants = '<article><h2 id={0}>{1}</h2><a href="/restaurants/{0}/edit?content={1}">Editar</a>  <a href="/restaurant/{0}/delete">Excluir</a></article>'
				for id,content in dados.items():
					pre_output += restaurants.format(id,content)
				print(pre_output)
				output = output.format(pre_output)
				print(output)
				self.wfile.write(output.encode('utf-8'))


			if self.path.endswith('/restaurants/new'):
				self.send_response(301)
				self.send_header('content-type','text/html')
				self.end_headers()
				output = ''
				output = '''<!doctype html>
<html>
	<head>
		<meta charset='utf-8'>
		<meta http-equiv='content-type' content='text/html'>
	</head>
	<body>
		<main>
			<form method='POST' acept-charset='utf-8' enctype='multipart/form-data' action='/restaurants/new'>
				<input name='name' type='text'>
				<input type='submit'>
			</form>
		</main>
	</body>
</html> '''
				print(output)
				self.wfile.write(output.encode('utf-8'))

			regex = re.compile(r'/restaurants/\d+/edit\?content=\w+')
			if re.match(regex,self.path):
				print('opa, correspondeu a url de edicao')
				restaurant_id = re.search('\d+',self.path).group(0)
				print('Id do restaurante: ' + str(restaurant_id))
				content_index = 0
				output = ''
				content_index = self.path.index('content')
				name = urlparse.parse_qs(self.path[content_index:])
				print(name['content'][0])
				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = '''<!doctype html>
<html>
	<head>
		<meta charset='utf-8'>
		<meta http-equiv='content-type' content='text/html'>
		<title>Edit restaurant's name</title></head>
	<body>
		<h1>{name}</h1>
		<form method="POST" acept-charset='utf-8' enctype='multipart/form-data' action='/restaurant/{id}/edit'>
			<input name='restaurant' type='text' placeholder="New restaurant's name">
			<input type='submit'>
		</form>
	</body>
</html>
'''
				self.wfile.write(output.format(name = name['content'][0], id = restaurant_id).encode('utf-8'))
			regex = re.compile(r'/restaurant/\d+/delete')
			if re.match(regex,self.path):
				print('Request para deletar um item')
				self.send_response(200)
				self.send_header('content-type','text/html')
				self.end_headers()
				deleteItem = operations.deleteRestaurant(re.search('\d+',self.path).group(0))
				if deleteItem:
					print('Deletado')
					self.wfile.write('Restaurante deletado com sucesso'.encode('utf-8'))
				else:
					print('Nao deletado')
					self.wfile.write('Nao foi possivel deletar o restaurante informado.'.encode('utf-8'))
		except KeyboardInterrupt:
			print('Deu errado')
	def do_POST(self):
		if self.path.endswith('/restaurants/new'):
			self.send_response(301)
			self.send_header('content-type','text/html')
			self.send_header('Location','/')
			self.end_headers()
			tipoCodificacaoForm, dadosForm = cgi.parse_header (
				self.headers.get('content-type'))
			print(dadosForm)
			dadosForm['boundary'] = bytes(dadosForm['boundary'], 'utf-8')
			print(dadosForm)
			if tipoCodificacaoForm == 'multipart/form-data':
				fields = cgi.parse_multipart(self.rfile, dadosForm)
			if fields == b'':
				sys.exit()
			print(fields)
			name = fields['name']
			print(type(name))
			output = ''
			for i in name:
				print(i.decode('utf-8'))
				operations.insertRestaurant(i.decode('utf-8'))
				output = 'Voce acabou de inserir o restaurant {0} em sua base de dados...'
				print(output.format(i.decode('utf-8')))
			self.wfile.write(output.format(name).encode('utf-8'))

		regex = re.compile(r'/restaurant/\d+/edit')
		if re.match(regex,self.path):
			print('Tentando fazer um post para alterar o nome do restaurant')
			self.send_response(301)
			self.send_header('content-type', 'text/html')
			tipoCodificacaoForm, dadosForm = cgi.parse_header (
				self.headers.get('content-type')
			)
			print(tipoCodificacaoForm)
			print(dadosForm)
			dadosForm['boundary'] = bytes(dadosForm['boundary'],'utf-8')
			print(dadosForm)
			if tipoCodificacaoForm == 'multipart/form-data':
				fields = cgi.parse_multipart(self.rfile,dadosForm)
			new_name = fields['restaurant'][0].decode('utf-8')
			print(new_name)
			from_operations = operations.editRestaurant(re.search('\d+',self.path).group(0), new_name)
			print(from_operations)
			if not from_operations:
				self.wfile.write('O restaurante informado nao existe na sua base de dados...'.encode('utf-8'))
			else:
				self.wfile.write('Alterado com sucesso manolo'.encode('utf-8'))
if __name__ == '__main__':
	try :
		port = 8080
		server = HTTPServer(('',port), RequestHandler)
		print('Listening on port %s ' % port)
		server.serve_forever()
	except KeyboardInterrupt:
		server.socket_close()
