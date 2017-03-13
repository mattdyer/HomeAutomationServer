import json

def read_config():
	config_file = open('config.json','r')
	
	config = json.loads(config_file.read())
	
	return config