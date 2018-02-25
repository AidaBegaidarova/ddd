def wsgi_app(environ, start_response):
    status = '200 OK'
    resp = environ['QUERY_STRING'].split('&') 
    resp = [item.encode('utf-8')+b'\r\n' for item in resp]
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return resp
