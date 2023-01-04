def character_bi_gram(text, n):
    character_list = [tuple(text[i:i + n]) for i in range(len(text) - n + 1)]
    return set(character_list)


x = character_bi_gram("paraparaparadise", 2)
y = character_bi_gram("paragraph", 2)

print("X:{}".format(x))
print("Y:{}".format(y))
print("XとYの和集合：{}".format(x | y))
print("XとYの積集合：{}".format(x & y))
print("XとYの差集合:{}".format(x - y))
print("Xにseがあるか：{}".format(('s', 'e') in x))
print("Yにseがあるか：{}".format(('s', 'e') in y))

