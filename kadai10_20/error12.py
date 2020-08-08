path1 = r"/Users/hide/100knocks/kadai10_20/col1.txt"
path2 = r"/Users/hide/100knocks/kadai10_20/col2.txt"
with open(path1,) as f:
    print(len([r for r in f.read().split("¥n")]))

with open(path2,) as f:
    print(len([r for r in f.read().split("¥n")]))
