# "Database code" for the DB Forum.

import datetime
import psycopg2
POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  banco = 'forum'
  conexao = psycopg2.connect(database=banco,user='vagrant')
  manipula_banco = conexao.cursor()
  query = 'select content, time from posts'
  manipula_banco.execute(query)
  dados = manipula_banco.fetchall()
  conexao.close()
  print(dados)
  return reversed(dados)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  #POSTS.append((content, datetime.datetime.now()))
  banco = 'forum'
  conexao = psycopg2.connect(database=banco,user='vagrant')
  manipula_banco = conexao.cursor()  
  #query = "insert into posts values('{0}')"
  #for post in POSTS: 
  #manipula_banco.execute(query.format(post[0],post[1]))
  #manipula_banco.execute(query.format(content,))
  #manipula_banco.execute("insert into posts values ('%s')" % content)
  manipula_banco.execute('insert into posts values (%s)', (content,)) 
  conexao.commit()
  conexao.close()
  return True
