from bottle import run, route

@route('/')
def index():
    return "Welcome to Rasp3!"

run(host = '0.0.0.0', port = 8080, debug = True)

