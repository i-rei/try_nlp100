def word_bi_gram(text, n):
    word_list = text.split()
    output = [word_list[i:i + n] for i in range(len(word_list) - n + 1)]
    return output


def character_bi_gram(text, n):
    character_list = [tuple(text[i:i + n]) for i in range(len(text) - n + 1)]
    return character_list


input_text = "I am an NLPer"
print(word_bi_gram(input_text, 2))
print(character_bi_gram(input_text, 2))
