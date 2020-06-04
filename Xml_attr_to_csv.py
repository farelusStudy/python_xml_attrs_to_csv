from xml.dom import minidom
import os

def Xml_attrs_to_csv_append(xml_file, tag, attrs, csv_file):
    mydoc = minidom.parse(xml_file)
    items = mydoc.getElementsByTagName(tag)
    with open(csv_file, 'a', encoding="utf-8") as the_file:
        for item in items:
            curLine = []
            for i in range(len(attrs)):
                curLine.append(item.getAttribute(attrs[i]))
            line = ";".join(curLine) + '\n'
            the_file.write(line)


print('Enter xml files directory path')
path = input()
print('Enter csv file path')
csv_file = input()

attrs = ["last_name", "first_name", "middle_name", "birthdate"]


with open(csv_file, 'w', encoding="utf-8") as the_file:
    the_file.write(";".join(attrs) + '\n')
    pass

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.xml' in file:
            path = os.path.join(r, file)
            Xml_attrs_to_csv_append(path, 'Order', attrs, csv_file)

print("Done!")