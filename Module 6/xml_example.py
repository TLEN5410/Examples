import xml.etree.ElementTree as etree
# More information at: http://docs.python.org/2/library/xml.etree.elementtree.html

xml = '''<rpc-reply><configuration>
    <version>9.3R4.4</version>
    <system>
        <host-name>misers</host-name>
        <login>
            <user>
                <name>admin</name>
                <full-name>Administrator</full-name>
                <uid>2001</uid>
                <class>superuser</class>
            </user>
            <user>
                <name>netman</name>
                <uid>2000</uid>
                <class>super-user</class>
            </user>
            
        </login>
        <services>
            <ssh>
            </ssh>
            <netconf>
                <ssh>
                </ssh>
            </netconf>
            
        </services>
    </system>
    <interfaces>
        <interface>
            <name>ge-0/0/0</name>
            <unit>
                <name>0</name>
                <family>
                    <inet>
                    </inet>
                </family>
            </unit>
        </interface>
        <interface>
            <name>ge-0/0/1</name>
            <unit>
                <name>0</name>
                <mtu>1500</mtu>
                <family>
                    <inet>
                    </inet>
                </family>
            </unit>
        </interface>
    </interfaces>
    <snmp>
        <community>
            <name>euFohca7na</name>
            <authorization>read-write</authorization>
        </community>
    </snmp>
</configuration></rpc-reply>
'''

root = etree.fromstring(xml)
print root.find('.//snmp')
for child in root.iter():
    print child.tag, child.attrib

