from bottle import post, get, delete, run

@get('/')
def index():
    return "Welcome to bottle"

@post('/')
def index_post():
    return "Welcome from POST"

@delete('/')
def index_delete():
    return "Welcome from DELETE"


run(host = '0.0.0.0', port = 8080, debug = True)

'''
>>> import requests
>>> requests.post('http://192.168.1.121:8080')
<Response [200]>
>>> requests.post('http://192.168.1.121:8080').text
'Welcome from POST'
>>> requests.get('http://192.168.1.121:8080').text
'Welcome to bottle'
>>> requests.delete('http://192.168.1.121:8080').text
'Welcome from DELETE'
>>> requests.delete('http://192.168.1.121:8080')
<Response [200]>
>>>
'''
