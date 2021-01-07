a = "{[]}()"

legend = {
    "[": "]",
    "(": ")",
    "{": "}"
}

def is_balanced(string):
    stack = []
    for character in string:
        if character in legend:
            stack.append(character)
        elif character in legend.values():
            last_caracter = stack.pop()
            if legend[last_caracter] != character:
                return False
    if stack:
        return False
    else:
        return True

print(is_balanced("a(bcd)d"))
print(is_balanced("(kjds(hfkj)sdhf"))
print(is_balanced("(sfdsf)(fsfsf"))
print(is_balanced("{[]}()"))
print(is_balanced("{[}] "))
