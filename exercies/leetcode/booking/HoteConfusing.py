from collections import Counter
import json

#To avoid this, we want to create a tool to identify "confusing" cities: cities with at least 3 hotels with the same name. Given a list of tuples (hotel_id, hotel_name, city)

from pprint import pprint

hotels = [
    ("hotel_1234", "Sheraton", "Amsterdam"),
    ("hotel_1000", "Sheraton", "Buenos Aires"),
    ("hotel_1001", "Hilton", "Amsterdam"),
    ("hotel_1002", "Royal Palace", "Bogota"),
    ("hotel_1003", "Hilton", "Amsterdam"),
    ("hotel_1004", "Sheraton", "Buenos Aires"),
    ("hotel_1005", "Sheraton", "Buenos Aires")
]

counter = Counter()

for hotel in hotels:
    hotel_name = hotel[1]
    hotel_city = hotel[2]
    if (hotel_name, hotel_city) not in counter:
        counter[(hotel_name, hotel_city)] = 1
    else:
        counter[(hotel_name, hotel_city)] += 1

a = [i[1] for i in counter if counter[i] >= 3]
print(a)
