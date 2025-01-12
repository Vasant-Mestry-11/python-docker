# print("Program to sum two numbers")
# num1 = int(input("Enter the first no"))
# num2 = int(input("Enter the second no"))
# 
# result = num1 + num2
# 
# print(f'Sum of two numbers {result}')


# ================================= volume

# user_name = input("Enter your name to store in file or enter to proceed: ");
# if user_name:
#     with open("user_info.txt", "a") as file:
#         file.write(user_name + "\n")
#
# show_info = input("Do you want to see all user name? y/n: ")
# if show_info == 'y':
#     try:
#         with open('user_info.txt','r') as file:
#             content = file.readlines()
#     except Exception as e:
#         print(e, type(e))
#     else:
#         for line in content:
#             print(f'{line.rstrip()}')


# ================================= mount bind

try:
    with open('servers.txt', 'r') as file:
        content = file.readlines()
except Exception as e:
    print(e, type(e))
else:
    for line in content:
        print(f'{line.rstrip()}')