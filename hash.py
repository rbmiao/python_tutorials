#Initialize a table of zeros. 10 is the table size.
# table = [0] * 10
table = [[] for x in range(10)]    
    
def hash_function(x): 
    return x % 10 


#def insert(table,input,value): 
#    table[hash_function(input)] = value
def insert(table,input,value): 
    table[hash_function(input)].append((input,value))

insert(table,41,'apple')
insert(table,93,'banana')
insert(table,13,'tangerine')
insert(table,54,'apple')
insert(table,103,'banana')
insert(table,13,'tangerine')

print(table)


############
tree_list = ['Parents', 'Children', 'GrandChildren']
def build_tree(tree_list):
    if tree_list:
        return {tree_list[0]: build_tree(tree_list[1:])}
    return {}

build_tree(tree_list)
print(tree_list)


############
	
import hashlib
mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())


