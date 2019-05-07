import os
import re
#print (os.path.expanduser('~'))
    
    
## OUTPUT_PATH = environment variables:    
if __name__ == '__main__':
#    str1 = input("Please input:")
#    print("what you input is: {}".format(str1))
    fh = open('trytest.txt', "w")
    fh.write("1, Here we\n2, go!\n")
    fh.write("3, Another line is here\n")
    fh.write("4, Third lines\n")
    fh.close()

    print("reading")
    
    try: 
        fo = open('trytest1.txt', "r")
        str2 = fo.readlines()
        print(str2)
        fo.close()
    except IOError:
        print("There is no such file:")
        #sys.exit()
    
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    
#    print(fptr)
#    arr_count = int(input().strip())
#    arr = []
#    for _ in range(arr_count):
#        arr_item = int(input().strip())
#        arr.append(arr_item)
#    k = int(input().strip())
#    ##res = findNumber(arr, k )
#    ##fptr.write(str(result) + '\n')
#    fptr.write(arr)
#    fptr.close()
#
#  [x*5 for x in xrange(2,10,2)]

