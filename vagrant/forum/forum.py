#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from forumdb import get_posts, add_post

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Forum</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
      .banana
      {
   	color:blue:
	background:white;
      }
    </style>
  </head>
  <body>
    <h1>DB Forum</h1>
    <form method=POST>
      <div><textarea id="conteudo" name="content"></textarea></div>
      <div><button id="go" type="submit">Post message</button></div>
    </form>
    <form method=POST>
      <div><textarea class="banana" id="conteudo" name="content"></textarea></div>
      <div><button class="banana" id="go" type="submit">Teste</button></div>
    </form>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''


@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  posts = "".join(POST % (date, text) for text, date in get_posts())
  print(posts)
  html = HTML_WRAP % posts
  return html


@app.route('/', methods=['POST'])
def post():
  '''New post submission.'''
  message = request.form['content']
  print((message,))
  print('ENDERECO PARA A MAIN')
  print(url_for('main'))
  add_post(message)
  return redirect(url_for('main'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

