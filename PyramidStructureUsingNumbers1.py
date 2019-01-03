user_input = int(input("Enter number of rows you want to see in Pyramid : "))
for num in range(1, user_input + 1):
    for num1 in range(1, num + 1):
        print(num1, end = '')
    print()
