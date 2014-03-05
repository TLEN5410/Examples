import netsnmp
import sys


def main():
    session = netsnmp.Session(Version=1, Community='prviate', DestHost='192.168.87.132')
    ifnumber = netsnmp.Varbind('.1.3.6.1.2.1.2.1.0')
    vl = netsnmp.VarList(ifnumber)
    result = session.get(vl)
    print result[0]
    print ifnumber.val

    ifindex = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.1')
    ifdesc = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.2')
    iftype = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.3')
    vl = netsnmp.VarList()
    vl.append(ifindex)
    vl.append(ifdesc)
    vl.append(iftype)

    for ifIndex in range(0, int(ifnumber.val)):
        session.getnext(vl)
        print ifindex.tag, ifindex.iid, ifindex.val, ifindex.type
        print ifdesc.tag, ifdesc.iid, ifdesc.val, ifdesc.type
        print iftype.tag, iftype.iid, iftype.val, iftype.type
        sys.exit(1)

    '''ifdesc = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.3.' + indicies[0])
    vl = netsnmp.VarList(ifdesc)
    session.get(vl)
    print ifdesc.val'''
    
    

if __name__ == '__main__':
    main()
