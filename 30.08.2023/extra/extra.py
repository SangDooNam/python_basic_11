"""Certainly! How about creating a Python program to calculate the factorial of a given number? 
The factorial of a number n is the product of all positive integers from 11 to n. 
It's usually denoted by n!.

For example:

    4!=4×3×2×1=24
    5!=5×4×3×2×1=120

You can start by asking the user for a number, and then you can calculate the factorial 
using either a for loop or a while loop. After that, display the result to the user.

Here are some specific tasks you could consider:

    Prompt the user to enter a positive integer.
    Calculate the factorial of that number.
    Display the result to the user.
    Add error handling to deal with invalid inputs (like negative numbers or non-numeric inputs).

"""

# def Get_int_abs(prompt):
#     while True:
#         value = input(prompt)
#         try:
#             value = int(value)
#             if value < 0:
#                 print("please enter a positive integer. ")
#                 continue
#         except ValueError:
#             print('Enter a valid integer.')
#             continue
#         return abs(value)
        


# factorial_Calc = Get_int_abs('Enter a positive integer.: ')

# counter = factorial_Calc

# result = 1

# while counter > 0:
    
#     result = result * counter 
    
#     counter -= 1 
# print(f"the result of the factorial calculating the number{factorial_Calc} is :", result)


"""Certainly! How about creating a Python program that reverses a string but keeps the capitalization 
in the same positions?

For example, the string "PyThoN" reversed would become "NoThTyP".

Here are some specific tasks you could consider:

    Prompt the user to enter a string.
    Reverse the string.
    Make sure that the capitalization remains in the same positions after the string is reversed.
    Display the reversed string to the user.

This challenge involves string manipulation and can be a good exercise for understanding Python strings better.
"""

# letters = "abcdefghijklmnop"
# trans = str.maketrans(letters, letters.upper())
# text= input("Enter a any words or text: ")

# print(text.translate(trans))

# reverser = text[::-1]


# print(reverser.translate(trans))

#-------------------------------------------------------------------

# text = input("Enter any words or text: ")

# # Initialize an empty list to hold the reversed characters
# reversed_text_list = [None] * len(text)

# # Loop through the original string to place the reversed characters
# # into their corresponding positions in the reversed_text_list
# for i, char in enumerate(text):
#     reversed_text_list[-(i + 1)] = char.lower() if char.islower() else char.upper()

# # Now apply the original capitalization to the reversed characters
# for i, char in enumerate(text):
#     if char.isupper():
#         reversed_text_list[i] = reversed_text_list[i].upper()
#     else:
#         reversed_text_list[i] = reversed_text_list[i].lower()

# # Join the list back into a string and print it
# reversed_text = ''.join(reversed_text_list)
# print("Reversed text with maintained capitalization:", reversed_text)

#----------------------------------------------------------------------------

text = input("Enter any words or text: ")

# Initialize an empty list to hold the reversed characters
reversed_text_list = [None] * len(text)

# Loop through the original string to place the reversed characters
# into their corresponding positions in the reversed_text_list
for i, char in enumerate(text):
    reversed_text_list[-(i + 1)] = char

# Now apply the original capitalization to the reversed characters
for i, char in enumerate(text):
    if char.isupper():
        reversed_text_list[-(i + 1)] = reversed_text_list[-(i + 1)].upper()
    else:
        reversed_text_list[-(i + 1)] = reversed_text_list[-(i + 1)].lower()

# Join the list back into a string and print it
reversed_text = ''.join(reversed_text_list)
print("Reversed text with maintained capitalization:", reversed_text)

