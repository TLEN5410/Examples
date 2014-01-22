
def configure_fa00():
	cfg = "interface FastEthernet 0/0\n"
	print 'Configuring interface FastEthernet 0/0'
	duplex = raw_input('Enable full duplex (Y/N)? ')
	cfg += "\t%s\n" % (duplex)
	enter_ip = raw_input('Assign an IP address (Y/N)? ')
	
	if enter_ip == 'Y':
		ip = raw_input("Enter IP address: ")
		nm = raw_input("Enter Netmask: ")
		cfg += "\tip address %s %s" % (ip, nm)
		
	print cfg
	
def configure_fa01():
	pass

def configure_interface():
	interface = raw_input("Enter new interface name: ")
	cfg = "interface %s\n"
	duplex = raw_input('Enable full duplex (Y/N)? ')
	cfg += "\t%s\n" % (duplex)
	enter_ip = raw_input('Assign an IP address (Y/N)? ')
	
	if enter_ip == 'Y':
		ip = raw_input("Enter IP address: ")
		nm = raw_input("Enter Netmask: ")
		cfg += "\tip address %s %s" % (ip, nm)
		
	print cfg
	
configure_fa00()
configure_interface()
	
	
	