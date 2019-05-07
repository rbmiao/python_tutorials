#!/usr/bin/python

def two_sum(nums, target):
    lookup = {}
    for cnt, num in enumerate(nums):
        #print(cnt, num, nums, target, lookup)
        if (target - num) in lookup:
            #print("got the answer!")
            #print(cnt, num, nums, target, lookup, lookup[target-num]) 
            return lookup[target-num], cnt
        lookup[num] = cnt
    print(lookup)            


a = (2,7,1,8,12,13,15)
t = 16
print(two_sum(a,t))  # (1,2)

print("daniel")
a = (-3,4,3,90)
t = 7
print(two_sum(a,t))  # (1,3)





#animals = [
#    {
#        "animal" : {
#            "type" : "bunny"
#        }
#    },
#    {
#        "animal" : {}
#    },
#    {}
#]
#
#for item in animals:
#    if "animal" in item:
#        print(item.get("animal").get("type"))
#
#for item in animals:
#    print(item.get("animal/type"))
#
#
#class DictQuery(dict):
#    def get(self, path, default = None):
#        keys = path.split("/")
#        val = None
#
#        for key in keys:
#            if val:
#                if isinstance(val, list):
#                    val = [ v.get(key, default) if v else None for v in val]
#                else:
#                    val = val.get(key, default)
#            else:
#                val = dict.get(self, key, default)
#
#            if not val:
#                break;
#
#        return val
#
#for item in animals:
#    print(DictQuery(item).get("animal/type"))





#print("NNEEEWWWW")
#def twosum_indices_linear(nums, target):
#    numtoindexmap = {}
#    for num1_index, num1 in enumerate(nums):
#        num2 = target - num1
#        try:
#            num2_index = numtoindexmap[num2]
#            print(nums, num1_index, num1, num2, num2_index, numtoindexmap[num2])
#        except KeyError:
#            numtoindexmap[num1] = num1_index
#            #print(nums, num1_index, num1, num2, num2_index, numtoindexmap[num2])
#        else:
#            print(nums, num1_index, num1, num2, num2_index, numtoindexmap[num2])	
#            return num1_index, num2_index

#print(sorted(twosum_indices_linear([2, 11, 15, 13, 7,], 9)))
#print(sorted(twosum_indices_linear([3, 9, 12, 5, 3], 6)))
#print(sorted(twosum_indices_linear([6, 7, 11, 15, 3, 6, 5, 3], 6)))



