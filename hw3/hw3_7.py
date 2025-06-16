import csv
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom
import re
import os

data = []
human_id = 1

date_pattern = r'\d{2}\.\d{2}\.\d{4}'
filename = 'people.csv'

fieldnames = ['id', 'name', 'surname', 'birth_date', 'place_of_residence']

if os.path.isfile(filename):
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f, delimiter='|')
        rows = list(reader)
        for row in rows:
            row['id'] = int(row['id'])
            data.append(row)
        if rows:
            human_id = data[-1]['id'] + 1

has_header = False
if os.path.isfile(filename):
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        try:
            first_row = next(reader)
            has_header = (first_row == fieldnames)
        except StopIteration:
            pass

while True:
    print('1 - add human\n2 - edit human\n3 - delete human\n4 - convert to json\n5 - convert to xml\n6 - break')
    user_c = int(input())
    match user_c:
        case 1:
            name = input('name: ')
            surname = input('surname: ')
            birth_date = input('birth_date (day.month.year): ')
            if not re.match(date_pattern, birth_date):
                print('invalid birth_date')
                continue
            lives_in = input('place_of_residence: ')

            new_data = {'id': human_id, 'name': name, 'surname': surname, 'birth_date': birth_date, 'place_of_residence': lives_in}
            data.append(new_data)

            human_id += 1

            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, delimiter='|', fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data)

        case 2:
            edit_id = int(input("enter human's id to edit: "))
            new_name = input('new name: ')
            new_surname = input('new surname: ')
            new_birth_date = input('new birth_date: ')
            new_lives_in = input('new place_of_residence: ')
            new_data = {'id': edit_id, 'name': new_name, 'surname': new_surname, 'birth_date': new_birth_date, 'place_of_residence': new_lives_in}
            for human in data:
                if human['id'] == edit_id:
                    human['name'] = new_data['name']
                    human['surname'] = new_data['surname']
                    human['birth_date'] = new_data['birth_date']
                    human['place_of_residence'] = new_data['place_of_residence']
            
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, delimiter='|', fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data)
            
        case 3:
            delete_id = int(input("enter human's id to delete: "))
            for human in data:
                if human['id'] == delete_id:
                    data.remove(human)
            human_id -= 1
            
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, delimiter='|', fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data)

        case 4:
            with open('people.json', 'w') as f:
                json.dump(data, f, indent=4)
        
        case 5:
            root = ET.Element('data')
            people = []
            with open(filename, 'r', newline='') as f:
                reader = csv.DictReader(f, delimiter='|')
                rows = list(reader)
                for row in rows:
                    human = ET.SubElement(root, 'human', attrib={'id': row['id']})
                    name = ET.SubElement(human, 'name')
                    name.text = row['name']

                    surname = ET.SubElement(human, 'surname')
                    surname.text = row['surname']

                    birth_date = ET.SubElement(human, 'birth_date')
                    birth_date.text = row['birth_date']

                    lives_in = ET.SubElement(human, 'place_of_residence')
                    lives_in.text = row['place_of_residence']
                
                # tree = ET.ElementTree(root)
                # tree.write('data.xml', encoding='utf-8', xml_declaration=True)
                xml_str = ET.tostring(root, encoding='utf-8')
                parsed = xml.dom.minidom.parseString(xml_str)
                pretty_xml = parsed.toprettyxml(indent="  ")

                with open('pretty.xml', 'w', encoding='utf-8') as f:
                    f.write(pretty_xml)
                
        case 6:
            break

        case _:
            print('invalid value')
            continue