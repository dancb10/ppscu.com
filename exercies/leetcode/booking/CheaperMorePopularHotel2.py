# We want to implement a feature to suggest to users the cheapest hotel that is more popular than the one they are looking at.
#Write a function that given an array of hotels, sorted by their popularity returns a map from the hotel ids that associates
# each hotel with the cheapest hotel that is more popular than the one in question.
# if there is no hotel that is cheaper and more popular than the one with that id, then it shouldn't be put in the map.
"""
input = [
    { id => 123, price => 200 }, # Most popular
    { id => 55, price => 150 }, # Second most popular
    { id => 17, price => 70 }, # Third most popular
    { id => 18, price => 500 }, # ...
    { id => 27, price => 270 },
    { id => 101, price => 230 } # Least popular
]

output = {
    18 : 17,
    27 : 17,
    101 : 17
}
"""

def get_hotels(hotels):
    results = {}
    cheapest_so_far = hotels[0]
    for hotel in hotels[1:]:
        if hotel["price"] < cheapest_so_far["price"]:
            cheapest_so_far = hotel
        else:
            results[hotel["id"]] = cheapest_so_far["id"]
    print(results)

input = [
    {"id": 123, "price": 200},  # Most popular
    {"id": 55, "price": 150},  # Second most popular
    {"id": 17, "price": 70},  # Third most popular
    {"id": 18, "price": 500},  # ...
    {"id": 27, "price": 270},
    {"id": 101, "price": 230}  # Least popular
]

get_hotels(input)
