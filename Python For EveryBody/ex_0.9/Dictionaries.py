file = open('text.txt')
count = dict()
for line in file:
    words = line.split()
    for word  in words:
        count[word] = count.get(word,0) + 1

lst1 = []

for k,v in count.items():
    lst1.append((v,k))

print(lst1)

lst1 = sorted(lst1, reverse=True)

for v, k in lst1[:10]:
    print(k,v)
    
x , y = 3, 4
print(y)    


days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count= dict()
for line in handle:
    
    if not line.startswith('From '):
        continue
    words = line.split()
    hours = words[5].split(':')[0]
    count[hours] = count.get(hours, 0) + 1

lst = []

for k,v in count.items():
    newtup = (k,v)
    lst.append(newtup)

lst = sorted(lst)


for k,v in lst:
    print(k,v)