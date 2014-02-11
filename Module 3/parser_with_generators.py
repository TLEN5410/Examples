''' One basic generator example using file parsing... more details
    can be found at:
    https://wiki.python.org/moin/Generators
    http://linuxgazette.net/100/pramode.html
'''
def parse_cisco_cfg(cfg_file):
    cfg = open(cfg_file)
    for line in cfg:
        if line.startswith('hostname'):
            print "I found hostname!"
            yield line.split()

        if line.startswith('version'):
            print "I found hostname!"
            yield line.split()

        print "I found nothing"

for setting, value in parse_cisco_cfg('startup-config'):
    print "The {0} is {1}".format(setting, value)

