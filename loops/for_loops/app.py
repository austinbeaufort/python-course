# for name in ['Austin', 'April', 'Frank']:
#     print(name)

# for num in [1, 2, 3, 4]:
#     print(num)

# for num in range(10):
#     print(num)

# for num in range(5, 10):
#     print(num)

# for num in range(0, 10, 2):
#     print(num)

# prices = [10, 20, 30]
# total = 0

# for item in prices:
#     total += item
# print(total)


# NESTED LOOPS

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]

for num in numbers:
    printString = ''
    for x in range(num):
        printString += 'x'
    print(printString)