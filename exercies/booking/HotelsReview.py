
#Given a set of hotels and its guests reviews, sort the hotels based on a list of words specified by a user.
# The criteria to sort the hotels should be how many times the words specified by the user is mentioned in the hotel reviews.
#The first line contains a space-separated set of words which we want to find mentions in the hotel reviews.
#The second line contains one integer M, which is the number of reviews.
#This is followed by M+M lines, which alternates an hotel ID and a review belonging to that hotel.
#Output
#A list of hotel IDs sorted, in descending order, by how many mentions they have of the words specified in the input.
# If the count is same, sort according to the hotel IDs.
# The first line contains an integer , which indicates the number of hotels that follow. Each hotel is represented by a single line of space-separated values, where the first value is the hotel ID (integer), the second value is its average price (integer) and the other values are the facilities offered by the hotel (space-separated strings). Each hotel has at least one facility. This is followed by another line containing an integer M, that indicates the number of test cases that follows. Each test case is represented by a single line of space-separated values, where the first value is the maximum budget for the guest (integer) and the rest forms a list of the guest’s required facilities (space separated strings). Each test case has at least one facility.
"""
input
4
1 70 wifi pool restaurant bathtub kitchenette
2 80 pool spa restaurant air-conditioning bathtub wifi
3 60 restaurant air-conditioning wifi
4 50 kitchenette
4
65 wifi
50 wifi
100 pool restaurant
80 kitchenette
"""

"""
output
3

2 1
1 4
"""
# hotels = []
# hotels_nr = input()
# print("hotels_nr: " + str(hotels_nr))
# for line in range(int(hotels_nr)):
#     hotels.append(input().split(" "))
# print(hotels)

hotels1 = [['1', '70', 'wifi', 'pool', 'restaurant', 'bathtub', 'kitchenette'], ['2', '80', 'pool', 'spa', 'restaurant', 'air-conditioning', 'bathtub', 'wifi'], ['3', '60', 'restaurant', 'air-conditioning', 'wifi'], ['4', '50', 'kitchenette']]
test_cases = [['65','wifi'], ['50', 'wifi'], ['100', 'pool', 'restaurant'], ['80', 'kitchenette']]





# def process_hotel(hotel, test_case):
#     hotel_id = hotel[0]
#     hotel_price = int(hotel[1])
#     hotel_reviews = hotel[2:]
#     counter = 0
#     test_budget = int(test_case[0])
#
#     if test_budget >= hotel_price:
#         for label in test_case[1:]:
#             if label in hotel_reviews:
#                 counter += 1
#             else:
#                 counter = 0
#     if counter == len(test_case[1:]):
#         return hotel_id, counter, hotel_price
#
#
# def process_hotels(hotels, test_case):
#     matching_hotels = []
#     for hotel in hotels:
#         hotel_tuple = process_hotel(hotel, test_case)
#         if hotel_tuple:
#             matching_hotels.append(hotel_tuple)
#     return matching_hotels
#
#
# def process_test_cases(hotelz, test_cases):
#     final_matching = []
#     for test in test_cases:
#         final_matching.append(process_hotels(hotelz, test))
#     return final_matching
#
#
# def sort_matching(matching_hotels_list):
#     for line in matching_hotels_list:
#         print(line)
#
#
# matching = process_test_cases(hotels1, test_cases)
# print(sort_matching(matching))

# print(process_hotel(['1', '70', 'wifi', 'pool', 'restaurant', 'bathtub', 'kitchenette'], ['100', 'pool', 'restaurant']))

# process_hotels(hotels1, ['65','wifi'])
# process_hotels(hotels1, ['50', 'wifi'])
# process_hotels(hotels1, ['100', 'pool', 'restaurant'])
# process_hotels(hotels1, ['80', 'kitchenette'])
