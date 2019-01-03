# Works good for single digit numbers
user_input = int(input("Enter number of rows you want to see in Pyramid :"))
initial_space_count = user_input - 1
for num in range(1, user_input + 1):
    print(initial_space_count * ' ', end = '')
    for num1 in range(num, 0, -1):
        print(num1, end = '')
    for num2 in range(2, num + 1):
        print(num2, end = '')
    print()
    initial_space_count -= 1
    
