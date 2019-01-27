import xml.etree.ElementTree as ET

tree = ET.parse('users-100.xml')
print(tree)

users_root = tree.getroot()
print(users_root.tag)

print(len(list(users_root.getchildren())))

print(users_root[0].tag)
print(users_root[0].attrib)
