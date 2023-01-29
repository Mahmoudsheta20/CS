import urllib.request
import json
adress = input('address :')
uh = urllib.request.urlopen(adress)
print(uh)

data = uh.read().decode()




j = json.loads(data)
print(json.dumps(j,indent=4))
count = 0
for x in j['comments']:
    count = count + int(x['count'])

print(count)