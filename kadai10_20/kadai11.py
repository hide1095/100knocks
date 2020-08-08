path = r"/Users/hide/100knocks/popular-names.txt"
with open(path,) as f:
    print([r.replace("\t", " ") for r in f.read().split("\n") if r is not " "])
