from bottle import run, get
import random

@get('/random')
def random_integer():
  return str(random.randint(0, 100))

@get('/')
def index():
  return '<p>Hello</p>'

run(reloader=True, debug=True)