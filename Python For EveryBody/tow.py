# # import urllib.request
# # import socket
# # from bs4 import BeautifulSoup

# # mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # mysock.connect(('data.pr4e.org', 80))
# # cmd ='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# # mysock.send(cmd)
# # print( cmd)
# # while True:
# #     data = mysock.recv(512)
# #     if len(data) < 1:
# #         break

# # mysock.close()



# # fhad = urllib.request.urlopen('https://sheta.netlify.app/')
# # for x in fhad:
# #     print(x.decode().strip())
    

# # # url = input('Enter: \n')
# # html = urllib.request.urlopen('https://www.coursera.org/learn/python-network-data/lecture/S4FIR/worked-example-beautifulsoup-chapter-12').read()
# # soup = BeautifulSoup(html,'html.parser')

# # tags = soup('a')

# # for tag in tags:
# #     print(tag.get('href',None))
    
# print(ord('G'))   
    
    
    
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# tags = soup('span')
# sum = 0
# for tag in tags:
#     # Look at the parts of a tag
#     span = tag.contents[0]
#     print('TAG:',span)
#     sum = sum + int(span)
 

# print(sum)


# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# x = []
# y = []

# url = input('Enter - ')

# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # count = int(input('count: ')) 
# postion = int(input('postion :')) - 1

# # Retrieve all of the anchor tags
# tags = soup('a')
# arr = []
# for tag in tags:
#     s = tag.get('href', None)
#     x = tag.text
#     arr.append(x)
 
# print(arr.index('Alannah'))


# import urllib.request
# from bs4 import BeautifulSoup
# url = input('Enter Url: ')
# count = int(input("Enter count: "))
# position = int(input("Enter position:"))
# for i in range(count):
#     html = urllib.request.urlopen(url).read()
#     soup = BeautifulSoup(html)

#     tags = soup('a')
#     s = []
#     t = []
#     for tag in tags:
#         x = tag.get('href', None)
#         s.append(x)
#         y = tag.text
#         t.append(y)
    
#     print(s[position-1]) 
#     print(t[position-1])
#     url = s[position-1]
    
# /
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)