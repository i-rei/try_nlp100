text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
word_list = text.split()
print(word_list)
a = [1, 5, 6, 7, 8, 9, 15, 16, 19]
output = dict()
# enumerateが使える
for i in range(len(word_list)):
    if i + 1 in a:
        output[word_list[i][:1]] = i + 1
    else:
        output[word_list[i][:2]] = i + 1
print(output)
