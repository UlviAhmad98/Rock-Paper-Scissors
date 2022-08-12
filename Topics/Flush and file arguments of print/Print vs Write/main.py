# numbers = [1234, 5678, 90]
# f = open("file_with_list.txt", "w")
# # save this list in `file_with_list.txt`
# print(str(numbers), file=f, end='')
# f.close()

walks = [
    {"day": "Monday", "distance": 2000},
    {"day": "Tuesday", "distance": 3000},
    {"day": "Wednesday", "distance": 3500},
    {"day": "Thursday", "distance": 2500},
    {"day": "Friday", "distance": 2500},
    {"day": "Saturday", "distance": 1000},
    {"day": "Sunday", "distance": 5600}]

walks_num = [x['distance'] for x in walks]
avr = sum(walks_num) // len(walks_num)
print(avr)
