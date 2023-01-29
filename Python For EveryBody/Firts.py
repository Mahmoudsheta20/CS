x = 5
print(x)

while x > 0:
    print(x)
    x = x - 1
print('end')
# try / except
astr = 'Hello World'
try:
    istr = int(astr)
except:
    istr = -1
print('first', istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('first', istr)
x = 'banana'
y = max(x)
print(y)


def stuff():
    print('Hello')
    return
    print('World')


stuff()

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)

# print('done')
# Definit Loop

for i in [1, 3, 6, 54, 5, 8]:
    print(i)

largest_so_far = -1
print('aftre', largest_so_far)
for num in [1, 36, 5, 44, 123, 69]:
    if num > largest_so_far:
        largest_so_far = num
    print('loop', largest_so_far, num)
print(largest_so_far)

total = 0
for i in [55, 1, 3, 6, 4, 8, 7, 9, 5]:
    total = total + i

print('total', total)

find = False

for i in [1, 3, 6, 9, 7, 8]:
    if i == 3:
        find = True
        break
    print(i)

print(find)

smalest = None

for value in [15, 13, 6, 9, 8, 92, 21]:
    if smalest is None:
        smalest = value
    elif value < smalest:
        smalest = value
    print(smalest)
print(smalest)
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)
x = 'From marquard@uct.ac.za'   


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])


