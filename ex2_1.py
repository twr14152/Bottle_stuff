from bottle import redirect, run, route

@route('/')
def index():
    return 'Please login'

@route('/restricted')
def restricted():
    #authenticate func
    #if it fails rediect
    redirect('/')

run(host = '0.0.0.0', port = 8080, debug = True)

