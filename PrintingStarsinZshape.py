user_input = int(input("Enter size of the alphabet z you want : "))
print(user_input * '*')

for row in range(1, user_input - 1):
    print((user_input - (row + 1)) * ' ' + '*')

print(user_input * '*')
