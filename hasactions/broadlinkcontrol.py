import broadlink



def process_action(action,config):
	
	ircodes = config['ircodes']
	
	ircode = ircodes[action]
	
	print ircode
	
	print action + ' successful'
