import broadlinkcontrol

def process_action(name,config):
	
	device = name.split('/')[0]
	action = name.split('/')[1]
	
	if device == 'broadlink':
		broadlinkcontrol.process_action(action,config['broadlink'])
	
	print device
	print action
	
	return name
