def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    resp = environ['QUERY_STRING'].split('&') 
    resp = [item+'\n\r' for item in resp]
    start_response(status, headers)
    return resp
