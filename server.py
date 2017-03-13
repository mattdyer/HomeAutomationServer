import wsgiref.simple_server
import mimetypes
import hasactions

def application(environ, start_response):
	
	status = '200 OK'
	requestedPath = environ['PATH_INFO']
	
	content = ''
	content_type = 'text/html'
	
	try:
		htmlPath = '/html' + requestedPath
		file_content = open(htmlPath[1:])
		content = file_content.read()
		content_type = mimetypes.guess_type(htmlPath[1:])[0]
	except IOError:
		if (requestedPath[:7] == '/action'):
			
			hasactions.process_action(requestedPath[8:])
			
		else:
			status = '404 Not Found'
	
	start_response(status,[('content-type', content_type + ';charset=utf-8')])
	
	
	return [content.encode('utf-8')]

server = wsgiref.simple_server.make_server('', 8000, application)
server.serve_forever()