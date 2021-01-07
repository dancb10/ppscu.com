# Given a integer , return corresponding ASCII char  representation without using language building in feature. ex. input interger 1234, return "1234" in string or characters


def return_acii(number):
    string = ""
    while number > 0:
        last_nr = number % 10
        number = int(number / 10)
        string = string + str(last_nr)
    return string[::-1]

print(return_acii(1234))
