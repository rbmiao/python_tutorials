urls = [
    "/home/anti-depressants/xanax",
    "/home/heart/lipitor",
    "/home/heart/atorvastatin",
    "/home/heart/lipitor",
    "/home/heart/heart",
    "/drugs/nasal/flonase",
    "/drugs/topical",
    "/drugs/routes/oral/tablets",
    "/drugs/routes/nasal/flonase",
]
# { "home": { "anti-depressants" : {"xanax": {}}, "heart": {}}}

# 
# Your previous Plain Text content is preserved below:
# 
# Write code to parse urls into a sitemap tree structure and display it as text. For example, the following urls will result in this printed structure.
# 
# Milestones:
# 1. Parse routes into data structure
# 2. Print data structure as simply as possible to check parsing
# 3. Format text output like shown in below
# 
# Input:
# [
#     "/home/anti-depressants/xanax",
#     "/home/heart/lipitor",
#     "/home/heart/atorvastatin",
#     "/home/heart/lipitor",
#     "/home/heart/heart",
#     "/drugs/nasal/flonase",
#     "/drugs/topical",
#     "/drugs/routes/oral/tablets",
#     "/drugs/routes/nasal/flonase",
# ]
# 
# Output:
# - home
#     - anti-depressants
#         - xanax
#     - heart
#         - lipitor
#         - atorvastatin
#         - heart
# - drugs
#     - nasal
#         - flonase
#     - topical
#     - routes
#         - oral
#             - tablets
#         - nasal
#             - flonase
# 
# 
# { "home": { "anti-depressants" : {"xanax": {}}, "heart": {}}}
# 
# joel@blinkhealth.com

def read_output(urls):
    dict_output = {}
    for line in urls:
        keys = line.split("/")[1:2]
        values = line.split("/")[2:]
        #rec_insert()
        dict_output[keys] = dict_output[values]
        # print(keys, values)
        #print(dict_output)
        #dict_out[keys] = 

        
# {}, ['test', 'test3'] => { "test": {}} ^^ { "test": { "test3": {}}}
#    {}, ['test3'] => { "test3": {}} ^^
def rec_insert(root, keys):
    print("mmmmmmmmmm ")
    print(keys)
    if not keys:  
        return   
    key = keys[0]
    #next(iter(root))
    #root[key] = {}
    root[key] = keys[1:]
    firstKey = next(iter(root))
    print(firstKey, root[key], key, keys[1:])
    #print(firstKey, root(firstKey), keys[0], keys[1:] )
    #print(root)
    #rec_insert(root, keys[1:])

    if (root[key] == keys[0]):
        root[key].append[keys[1:]]
    else:
        rec_insert(root, root[key])
    # print(dict)
    
root = {}
rec_insert( root, ['test', 'test1'])
#rec_insert( root, ['test', 'test3'])
rec_insert( root, ['daniel', 'daniel1' ])
rec_insert( root, ['Miao', "miao1", "miao2"])

print(root)
    