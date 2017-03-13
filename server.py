import wsgiref.simple_server
import mimetypes

def application(environ, start_response):
	
	status = '200 OK'
	requestedPath = '/html' + environ['PATH_INFO']
	
	content = ''
	content_type = 'text/html'
	
	try:
		file_content = open(requestedPath[1:])
		content = file_content.read()
		content_type = mimetypes.guess_type(requestedPath[1:])[0]
	except IOError:
		status = '404 Not Found'
	
	start_response(status,[('content-type', content_type + ';charset=utf-8')])
	
	
	return [content.encode('utf-8')]

server = wsgiref.simple_server.make_server('', 8000, application)
server.serve_forever()