# def printing(st1):
#   if len(st1)>=3:
#     if st1.endswith('ing'):
#       newstring = st1+'ly'
#     else :
#       newstring = st1+'ing'

#   else:
#     newstring = st1
#   return newstring

# st1 = str(input("enter a string: "))
# print(printing(st1))

# st='ABCDEFGHI'
# print(st[2:7])
# print(st[-7:-2])
# print(st[2:-5])

# divisible_by_7 = [num for num in range(1, 1001) if num % 900 == 0]
# # Print the result
# print(divisible_by_7)


# def is_palindrome(user_input):
#     # Convert to lowercase and check if it's equal to its reverse
#     user_input = user_input.lower()  # Ensure case insensitivity
#     return user_input == user_input[::-1]

# # Input from the user
# user_input = input("Enter a string: ")

# # Check if it's a palindrome
# if is_palindrome(user_input):
#     print(f'"{user_input}" is a palindrome!')
# else:
#     print(f'"{user_input}" is not a palindrome.')

# def swap(l,index1,index2):
#   l[index1],l[index2]=l[index2],l[index1]

# l = [1,68,2,40,55]
# swap(l,0,4)
# print(l)


def fibonacci_5():
    a, b = 0, 1
    for i in range(5):
        print(a, end=" ")
        a, b = b, a + b

# Call the function
fibonacci_5()


