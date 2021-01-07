a='The cat is in the house andcat 3 da.'
b='The mother,is 3 doors.'

def displaywords(sentence):
    slice=''
    wordstodisplay=''
    for character in sentence:
        if character.isalpha():
            slice=slice+character
        else:
            wordstodisplay=wordstodisplay+slice[::-1]+character
            slice=''
    return wordstodisplay+slice[::-1]

print(displaywords(a))
print(displaywords(b))
