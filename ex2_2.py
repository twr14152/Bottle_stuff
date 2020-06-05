from bottle import error, route, run, abort

@error(404)
def not_found(error):
    return "The requested content was not found!"

@error(409)
def not_found(error):
    return "Do not do that!"

@error(401)
def not_found(error):
    return "Forbidden!"

@route("/")
def index():
    return "Welcome to bottle"

@route("/youshallnotpass")
def shownotpass():
    abort(401)

@route("/doNot")
def doNot():
    abort(409)

run(host = '0.0.0.0', port = 8080, debug = True)

