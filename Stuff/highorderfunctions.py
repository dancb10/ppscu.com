
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
# for fruit in sorted(fruits, key=len):
#     print(fruit)

for fruit in sorted(fruits, key=lambda x: x[::-1]):
    print(fruit[::-1])

