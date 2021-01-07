#Problem statement
#Given a set of hotels and its guests reviews, sort the hotels based on a list of words specified by a user. The criteria to sort the hotels should be how many times the words specified by the user is mentioned in the hotel reviews.

#Input
#The first line contains a space-separated set of words which we want to find mentions in the hotel reviews.
#The second line contains one integer M, which is the number of reviews.
#This is followed by M+M lines, which alternates an hotel ID and a review belonging to that hotel.

#Output
#A list of hotel IDs sorted, in descending order, by how many mentions they have of the words specified in the input. If the count is same, sort according to the hotel IDs.
"""
bathroom wifi 
5
10 This is a nice hotel with good bathroom
50 Shitty hotel with wifi
20 Good but with a single wifi
30 Bathroom an wifi included
60 Just Bathroom
"""

words = input().rstrip().split(" ")
print(words)
nr_review = int(input().rstrip())
print(nr_review)
reviews = []
for review in range(nr_review):
    reviews.append(input().rstrip().split(" "))
print(str(reviews))

words = ['bathroom', 'wifi']
reviews = [['10', 'This', 'is', 'a', 'nice', 'hotel', 'with', 'good', 'bathroom'], ['50', 'Shitty', 'hotel', 'with', 'wifi', 'bathroom'], ['20', 'Good', 'but', 'with', 'a', 'single', 'wifi'], ['30', 'Bathroom', 'an', 'wifi', 'included'], ['60', 'Just', 'Bathroom']]
from collections import Counter


def search_keyword(hotel_review, to_search):
    counter = 0
    word_counts = Counter(hotel_review)
    for key, value in word_counts.items():
        if key in to_search and value > 0:
            counter += value
    return counter


def get_results(reviews, to_search):
    hotel_results = []
    for review in reviews:
        counter = search_keyword(review, to_search)
        if counter:
            hotel_results.append([review[0], counter])
    return sorted(hotel_results, key=lambda sl: (sl[1], sl[0]), reverse=True)


# print(search_keyword(['10', 'This', 'is', 'a', 'nice', 'hotel', 'with', 'good', 'bathroom'], ['bathroom', 'wifi']))
print(get_results(reviews, words))

