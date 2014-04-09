import xml.etree.ElementTree as etree

somexml = '''<rpc-reply>
	<configuration>
		<system>
			<hostname>myrouter</hostname>
		</system>
	</configuration>
</rpc-reply>
'''

oureditconfig_template = '''
<rpc>
    <edit-config>
        <target>
            <running/>
        </target>
        <config>
'''

edit_config = etree.Element('edit-config')
#print edit_config.tag

root = etree.fromstring(somexml)
needle = root.find('.//hostname')
needle.text = "mynewhostname"


edit_config_request = oureditconfig_template + etree.tostring(needle) + '</config></rpc>'
print edit_config_request

'''
for child in root.getiterator():
    if child.tag == "hostname":
        print child.text
'''
