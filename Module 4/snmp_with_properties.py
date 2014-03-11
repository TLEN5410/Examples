import netsnmp

class Router(object):
    ''' In other languages, it is encouraged to wrap access to all public
        attributes using getter and setter methods.  This can allow
        you to change where the values come from for that attribute later on.  

        Python has an interesting solution for this, in that you can change
        an attribute into something called a property.  A property is simply
        a mapping from an attribute to a method that gets the value,
        and another method that returns a value.
    '''

    def __init__(self, host, community):
        self.session = netsnmp.Session(DestHost=host, Community=community, 
                                        Version=1)

    def _get_value(self, oid):
        varbind = netsnmp.Varbind(oid)
        self.session.get(netsnmp.VarList(varbind))
        return varbind.val

    def _set_value(self, oid, value):
        varbind = netsnmp.Varbind(oid)
        varbind.val = value
        self.session.set(netsnmp.Varlist(varbind))

    def get_hostname(self):
        self._get_value('.1.3.6.1.2.1.1.5')

    def set_hostname(self, new_value):
        self._set_value('.1.3.6.1.2.1.1.5', new_value)

    hostname = property(get_hostname, set_hostname)


def main():
    r1 = Router('100.64.254.22', 'private')
    print r1.hostname
    r1.hostname = "newname"
    print r1.hostname

if __name__ == '__main__':
    main()
