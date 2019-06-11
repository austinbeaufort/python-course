names = ['john', 'bob', 'austin', 'jake', 'mike']

# names[0] = 'Jon'
# print(names)
# print(names)
# print(names[0])
# print(names[2])
# print(names[-1])

# print(names[2:])
# print(names[2:4])


# Exercise Max Number

# numList = [1, 11, 22, 42, 22, 33, 4]
# maxNum = 0
# for num in numList:
#     if num > maxNum:
#         maxNum = num
# print(maxNum)




# 2D Lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for item in row:
#         print(item)

# print(matrix[0][1])





# List Methods

# numbers = [5, 2, 1, 5, 7, 4]

# numbers2 = numbers.copy()
# numbers2.append(10)
# numbers.sort()
# numbers.reverse()
# print(numbers, numbers2)
# print (50 in numbers)
# print(numbers.index(5))
# numbers.insert(index, new_number)
# numbers.pop()
# numbers.append(11)
# numbers.remove(7)
# numbers.clear()

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
