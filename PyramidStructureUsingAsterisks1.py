user_input = int(input("Enter number of rows you want to see in a pyramid : "))

for row in range(1, int((user_input + 1) / 2) + 1):
    for num in range(1, row + 1):
        print('*', end = ' ')
    print()

for row1 in range(1, int((user_input + 1) / 2)):
    for num in range(int((user_input + 1) / 2) - row1, 0, -1):
        print('*', end = ' ')
    print()
