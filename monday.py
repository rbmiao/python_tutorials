X = [['A', 'B', 'C'], ['A', 'B', 'D'],['W','X', 'M'], ['W', 'X', 'N'], ['W','Y','Z']]
d = {}

for element in X:
    root = d
    print(element, d)
    for part in element:
        print("for path {} in element {}".format(part, root))
        if part not in root:
            root[part] = {}
        root = root[part]

print(d)


def print_nested(ident, root):
    print(root)
    print("Miao")
    #if not root[]:
    #    return
    #for key in root:
    #key = root[key][0]
    key0 = next(iter(root))
    print(key0)
    print(ident+"- "+key0)
    #root = root[key][1:]
    root = root[key0]
    ident += " "*4
    print(root)
    print_nested(ident, root) 


ident = ' '
print_nested(ident, d)

