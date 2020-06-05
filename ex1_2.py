from bottle import run, route, template

@route('/<name>')
def index(name=None):
    return template("Hello {{name}}, welcome to bottle", name = name)

run(host = '0.0.0.0', port = 8080, debug = True)
