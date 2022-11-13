s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
table = s.maketrans({
    ".": "",
    ",": "", })
ss = s.translate(table)
w = ss.split()
print(print([len(i) for i in w]))
