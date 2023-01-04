def cipher(input_text):
    sentense = [chr(219 - ord(i)) if i.islower() else i for i in input_text]
    return ''.join(sentense)


text = "I am a bookwarm"
text = cipher(text)
print(text)
text = cipher(text)
print(text)
