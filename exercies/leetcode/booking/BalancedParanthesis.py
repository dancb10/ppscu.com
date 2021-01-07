#
#Balanced parenthesis
#Create function that will determine are the parenthesis balanced in a given string
"""
boolean isBalanced(string)
a(bcd)d => true
(kjds(hfkj)sdhf => false
(sfdsf)(fsfsf => false
{[]}() => true
{[}] => false
"""


def isBalanced(string, legend):
    stack = []
    for character in string:
        if character in legend:
            stack.append(character)
        if character in legend.values():
            last_char = stack.pop()
            if legend[last_char] != character:
                return False

    if stack:
        return False
    else:
        return True


# phrase = "{[}]"
# phrase = "a(bcd)d"
# phrase = "(kjds(hfkj)sdh)f"
legend = dict()
legend["["] = "]"
legend["("] = ")"
legend["{"] = "}"

print(isBalanced("a(bcd)d", legend))
print(isBalanced("(kjds(hfkj)sdhf", legend))
print(isBalanced("(sfdsf)(fsfsf", legend))
print(isBalanced("{[]}()", legend))
print(isBalanced("{[}] ", legend))
