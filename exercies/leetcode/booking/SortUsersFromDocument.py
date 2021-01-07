# Sort a document of users by age.
"""
dan 30
bla 20
rut 45
plamam 32
duah 23
ojfah 2
danka 80
mkdana 25
"""
def generate_entries(document):
    lines = []
    with open(document, 'r') as f:
        for line in f:
            lines.append(line.rstrip().split(" "))
    return lines


def sort(entries):
    if len(entries) > 1:

        mid = len(entries) // 2
        left = entries[:mid]
        right = entries[mid:]

        sort(left)
        sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                entries[k] = left[i]
                i += 1
            else:
                entries[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            entries[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            entries[k] = right[j]
            j += 1
            k += 1
    return entries


ent = generate_entries("users.txt")
print(ent)
print(sort(ent))
