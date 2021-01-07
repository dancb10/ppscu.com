def palin(n):
    return True if str(n) == str(n)[::-1] else False

def palinString(m):
    return True if m == m[::-1] else False


nr = 1234321
# print(palin(nr))

string = "malayalam"
# print(palinString(string))


def invertNumber(no):
    reminder = no
    new_nr = 0
    while no != 0:
        digit = no % 10
        no = int(no / 10)
        new_nr = new_nr * 10 + digit
    if new_nr == reminder:
        return True
    return False

nr = 1234321
print(invertNumber(nr))
