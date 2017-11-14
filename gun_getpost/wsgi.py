from pprint import pformat
from cgi import parse_qsl, escape

def hello_world(environ, start_response):
    output = ['<h1>Hello, World!</h1>']

    output.append('Post here:')
    output.append('<form method="post">')
    output.append('<input type="text" name="post">')
    output.append('<input type="submit" value="ok">')
    output.append('</form>')

    d = parse_qsl(environ['QUERY_STRING'])
    if environ['REQUEST_METHOD'] == 'POST':
        output.append('<h5>Post method:</h5>')
        output.append(pformat(environ['wsgi.input'].read()))

    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            output.append('<h5>Get method:</h5>')
            for ch in d:
                output.append(' : '.join(ch))
                output.append('<br>')

    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output
