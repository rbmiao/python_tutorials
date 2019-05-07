#!/usr/bin/python


class Employee:
    '所有员工的基类'
    employeeCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount += 1

    def printEmployee(self):
        print("Name is {}, Salary is {}".format(self.name, self.salary))



#if __name__ == "__main()__":
    

e1 = Employee("Daniel", "1000")
e2 = Employee("Miao", "9000")
    
e1.printEmployee()
e2.printEmployee()


 
#print(("\nEmployee.__doc__: {}").format(Employee.__doc__ ))
#print(("\nEmployee.__name__: {}").format( Employee.__name__ ))
#print(("\nEmployee.__module__: {}").format( Employee.__module__))
#print(("\nEmployee.__bases__: {}").format( Employee.__bases__))
#print(("\nEmployee.__dict__: {}").format( Employee.__dict__))

print("\nIn main method:\n")

# Program to count the number of each vowel in a string

# string of vowels
vowels = 'aeiou'

# change this value for a different result
ip_str = 'Hello, have you tried our turorial section yet?'

# uncomment to take input from the user
#ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

count = {}
print(count)
# make a dictionary with each vowel a key and value 0
# count = {}.fromkeys(vowels,0)
count = {"a":0, "e":0, "i":0, "o":0, "u":0}


print(ip_str)
print(count)
#print(count.__dict__)
# count the vowels
#for char in ip_str:
#    print(char)
#    if char in count:
#        print(char, count)	
#        count[char] += 1
#        print(char, count)



for letter in ip_str:
    print(letter)
    if letter in count:
        print(letter, count[letter], count)	
        count[letter] += 1
        print(letter, count[letter], count)
    else:
    	continue

print("DAniel")
# Program to sort alphabetically the words form a string provided by the user

# change this value for a different result
my_str = "Hello this Is an Example With cased letters"

# uncomment to take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
print(count)