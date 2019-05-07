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

def output_url(root, indent=0):
  for key, value in root.items():
    print('    ' * indent + ' - ' + str(key))

    if type(value) is dict:
      output_url(value, indent + 1)
    else:
      print('    ' * (indent + 1) + ' - ' + str(value))

def read_url():
  for url in urls:
    depth_url = root
  
    for element in url.split('/')[1:]:
      if element not in depth_url:
        depth_url[element] = {}
      depth_url = depth_url[element]


if __name__ == '__main__':

    root = {}
    read_url()
    output_url(root, 0)