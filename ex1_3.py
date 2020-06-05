from bottle import run, route, view

@route('/<name>')
@view('templates/hello.html')
def index(name=None):
    return dict(name = name)

run(host = '0.0.0.0', port = 8080, debug = True)
