import netsnmp

class Router(object):
    def __init__(self, host, community):
        self.session = netsnmp.Session(DestHost=host,
                                        Community=community,
                                        Version=1)

    def get_value(self, oid):
        varbind = netsnmp.Varbind(oid)
        self.session.get(netsnmp.VarList(varbind))
        return varbind.val

    def set_value(self, oid, value):
        varbind = netsnmp.Varbind(oid)
        self.session.get(netsnmp.VarList(varbind))
        varbind.val = value
        self.session.set(netsnmp.VarList(varbind))

    def get_hostname(self):
        return self.get_value('.1.3.6.1.2.1.1.5.0')

    def set_hostname(self, new_value):
        self.set_value('.1.3.6.1.2.1.1.5.0', new_value)

    def get_contact(self):
        return self.get_value('.1.3.6.1.2.1.1.4.0')

    def get_location(self):
        return self.get_value('.1.3.6.1.2.1.1.6.0')


def main():
    r1 = Router("198.51.100.1", "icanhasnetworkaccess")
    r1.set_hostname("testers")
    print r1.get_hostname()

if __name__ == '__main__':
    main()
