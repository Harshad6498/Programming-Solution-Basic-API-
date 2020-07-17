
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
tree = ET.parse('sample.xml')
#root = tree.getroot()
#print(root.tag)
m_number1 = tree.find('.//{http://schemas.auf.com/integration/common}MobileNumber').text
m_number2 = tree.find('.//{http://schemas.auf.com/integration/common}MobileNo').text
mob_numbers = []
mob_numbers.append(m_number1)
mob_numbers.append(m_number2)
print(mob_numbers)
for num in mob_numbers:
    address = "https://api.datayuge.com/v1/lookup/"+num
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print(data)