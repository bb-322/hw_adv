import xml.etree.ElementTree as ET
import xml.dom.minidom

root = ET.Element('streets')

house_id = 0
flat_id = 0
for i in range(10):
    street = ET.SubElement(root, 'street', attrib={'id': str(i + 1)})
    for _ in range(10):
        houses = ET.SubElement(street, 'house', attrib={'id': str(house_id + 1)})
        house_id += 1
        for _ in range(10):
            flat = ET.SubElement(houses, 'flat', attrib={'id': str(flat_id + 1)})
            flat_id += 1

xml_str = ET.tostring(root)
parsed = xml.dom.minidom.parseString(xml_str)
pretty_xml = parsed.toprettyxml(indent="  ")

with open('pretty.xml', 'w') as f:
    f.write(pretty_xml)

house69 = root.find('.//house[@id="69"]')
if house69 != None:
    for flat in house69:
        print(f'{flat.tag}_{flat.attrib["id"]}') # flats in house number 69

print()

street9 = root.find('.//street[@id="9"]')
if street9 != None:
    for house in street9:
        print(f'{house.tag}_{house.attrib["id"]}') # houses on street number 9