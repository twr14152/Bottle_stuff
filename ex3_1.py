from bottle import post, get, delete, run

@get('/')
def index():
    return "Get method"

@post('/')
def index_post():
    return "POST method"

@delete('/')
def index_delete():
    return "DELETE method"


run(host = '0.0.0.0', port = 8080, debug = True)

'''
In [1]: import requests                                                                        

In [2]: requests.get("http://192.168.1.121:8080")                                              
Out[2]: <Response [200]>

In [3]: requests.get("http://192.168.1.121:8080").text                                         
Out[3]: 'Get method'

In [4]: requests.post("http://192.168.1.121:8080")                                             
Out[4]: <Response [200]>

In [5]: requests.post("http://192.168.1.121:8080").text                                        
Out[5]: 'POST method'

In [6]: requests.delete("http://192.168.1.121:8080")                                           
Out[6]: <Response [200]>

In [7]: requests.delete("http://192.168.1.121:8080").text                                      
Out[7]: 'DELETE method'

In [8]:   
'''
