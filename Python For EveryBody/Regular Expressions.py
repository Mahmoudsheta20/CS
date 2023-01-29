import re
file = open('text.txt')

# p = file.read()
# print(p)
# dic = dict()
# for word in file:
#     word = word.rsplit()

#     print(word)
# print(dic)

# x =[1,2,3,6,45,655,]

# for l in x:
#     print(l)



# x = 0
# if x < 2 :
#     print('Small')
# elif x < 10 :
#     print('Medium')
# else :
#     print('LARGE')
# print('All done')



# stuff = dict()
# stuff['candys'] = 1
# stuff['candy'] = 1
# stuff['cand'] = 1
# stuff['can'] = 1

# for y in stuff:
#     print(y)

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# dic = dict()
# item = None
# for lis in handle:
    
#     if not lis.startswith('From '):
#         continue
        
#     lis = lis.split()
#     lis = lis[1]
#     dic[lis] = dic.get(lis,0)+1
    

# bigcount = 0
# bigword = None

# for word , count in dic.items():
#     if count > bigcount:
#         bigcount = count
#         bigword  = word
# print(bigword, bigcount)
# x= list()

# for line in file:
#     line = line.rstrip()
#     y = re.findall('[0-9]+',line)
#     x = x + y
    


c = file.read()
print(c)

y = re.findall('[0-9]+',c)
print(y)
sum = 0

for z in y:
    sum = sum + int(z)
print(sum)    
