import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter location: ')
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()

tree =ET.fromstring(data)
lst  = counts = tree.findall('.//count')
print(lst)
for x in lst:
    count= count + int(x.text)
        
print(count)    
