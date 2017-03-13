import broadlinkcontrol

def process_action(name):
	
	device = name.split('/')[0]
	action = name.split('/')[1]
	
	if device == 'broadlink':
		broadlinkcontrol.process_action(action)
	
	print device
	print action
	
	return name
