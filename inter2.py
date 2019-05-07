import os
import re
print (os.path.expanduser('~'))


def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = {}".format(list1))
print("list2 = {}".format(list2))
print("list3 = {}".format(list3))


my_tuple = (10, 20, 30, 40)
my_dict = {"name": "daniel", "age": "39", "occupant":"student"}
my_set = {10, 20, 30, 10, 20, 30, 50, 60}

for i in my_tuple:
	print(i)

print("following is set:")
for j in my_set:
	print(j)

for key, value in my_dict.items():
	print("My key is {} and value is {}".format(key, value))

for k,v in my_dict.items():
	print(k,v)

print(re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","micheal.pages@mp.com"))


list = ['a', 'b', 'c', 'd', 'e']
print (list[10:])

#try:
#    fh = open("trytest.txt", r+w)
#
#except:
#
#else: