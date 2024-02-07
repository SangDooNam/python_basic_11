
# print("Welcome to the Stone Game!")

# stone_in_pile = int(input("Enter the total number of stone in the pile: "))

# Max = int(input("Enter the maximum number of stones that can be taken at once: "))

# p1 = input("Enter the name of Player 1: ")
# p2 = input("Enter the name of Player 2: ")

# start_p = input("Enter the player number who will start the game (1 / 2): ")

# print("Game start!")

# print('-------------------')


# while stone_in_pile > 0:
    
#     reminding_stone = stone_in_pile
    
#     print('Curremt stone count :',reminding_stone )
    
#     current_p = None
    
#     if start_p == '1':
#         current_p = p1
#     elif start_p == '2':
#         current_p = p2
        
#     turn = int(input(f"{current_p}'s turn. Enter a number of stones to take (1- {min(stone_in_pile, Max)}): "))
    
#     if turn < 0 or turn > stone_in_pile or turn > Max:
#         print("Enter a valid number : ")
#         continue
    
#     if p1 == current_p:
#         start_p = '2'
#     elif p2 == current_p:
#         start_p = '1'
        
    
#     stone_in_pile -= min(turn, reminding_stone)
    
# print("the winner is", current_p)
    


text = input("Enter any words or text: ")

reverse_text = [None] * len(text)

for i, e in enumerate(text):
    reverse_text[-(i + 1)] = e
    
for i, e in enumerate(text):
    if e.isupper():
        reverse_text[-(i + 1)] = reverse_text[-(i + 1)].upper()
    else:
        reverse_text[-(i + 1)] = reverse_text[-(i + 1)].lower()

reverse_text = "".join(reverse_text)

print("The reseult is: ", reverse_text)