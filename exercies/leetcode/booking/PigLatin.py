# Given a sentence convert the sentence to the modified  pig-latin language:
# Words beginning with a vowel, remove the vowel letter and append the letter to the end.
# All words append the letters 'ni' to the end.
# All words incrementally append the letter 'j'. i.e. 'j','jj','jjj
# input: This is just an example
# output: Thisnij sinijj justnijjj nanijjjj xampleenijjjjj

sentence = "This is just an example"


def pig_latin(sentence):
    words = sentence.rstrip().split(" ")
    vowels = ["a", "e", "i", "o", "u"]
    new_sentence = []
    for index in range(len(words)):
        word = words[index]
        j_multiplier = "j" * (index+1)
        if word[0] in vowels:
            word = words[index][1:] + words[index][0]
        word = word + "ni" + j_multiplier
        new_sentence.append(word)
    return " ".join(new_sentence)


print(pig_latin(sentence))

