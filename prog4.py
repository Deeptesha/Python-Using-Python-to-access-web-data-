import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
sum=0

address = input('Enter location: ')
uh = urllib.request.urlopen(address)
data = uh.read()
tree = ET.fromstring(data)



for count in tree.findall('comments/comment'):
    rank = int(count.find('count').text)
    sum=sum+rank

print(sum)