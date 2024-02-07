
print('Welcome to the Stone Game!')

stones_in_pile = int(input('Enter the total number of stones in the pile: ' ))

max_number = int(input("Enter the maximaum number of stones that can be taken at once :"))

player1 = input("Enter the name of Player 1 :")
player2 = input("Enter the name of Player 2 :")

currentPlayer = int(input("Enter the player number who will start the game (1, 2) : "))

print('Start !')
print('-------')
    
while stones_in_pile > 0:
    print(f"Current stone count: {stones_in_pile}" )
    
    player_name = ''
    
    if currentPlayer == 1:
        player_name = player1
        
    
    elif currentPlayer == 2:
        player_name = player2
    
    
        
    take_stone = int(input(f"{player_name}'s turn. Enter a number of stones of take (1- {min(max_number, stones_in_pile)}): "))
    
    if take_stone < 0 or take_stone > stones_in_pile or take_stone > max_number:
        print('Enter a valid number. ')
        continue
    
    
    if player_name == player1:
        currentPlayer = 2

    elif player_name == player2:
        currentPlayer = 1
        
    stones_in_pile -= take_stone
    
    

print(player_name,"wins the game!")





    