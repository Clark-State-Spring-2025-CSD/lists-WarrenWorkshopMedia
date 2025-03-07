#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

random.seed()
#Used seed 18 to test the scenario of a Tie where Player 1 and Player 2 roll a 12 on Index 0.
#Used seed 13 to test the scenario of a duplicate highest value using the first instance of the Index (44) at Index 2 for Player One.


#Random Number Generator for Player 1 and Player 2
Player_One = [random.randint(1, 50) for _ in range(10)]
Player_Two = [random.randint(1, 50) for _ in range(10)]

#Initialize Win Counts
Player_One_Wins = 0
Player_Two_Wins = 0

#Compare the numbers from the Players and add a win to the player with the higher number.
for i in range(10):
    if Player_One[i] > Player_Two[i]:
        Player_One_Wins += 1
    elif Player_Two[i] > Player_One[i]:
        Player_Two_Wins += 1

#Player One's Highest and Lowest Values and Indexes

Player_One_Highest_Value = max(Player_One)
Player_One_Highest_Index = Player_One.index(Player_One_Highest_Value)

Player_One_Lowest_Value = min(Player_One)
Player_One_Lowest_Index = Player_One.index(Player_One_Lowest_Value)

#Player Two's Highest and Lowest Values and Indexes

Player_Two_Highest_Value = max(Player_Two)
Player_Two_Highest_Index = Player_Two.index(Player_Two_Highest_Value)

Player_Two_Lowest_Value = min(Player_Two)
Player_Two_Lowest_Index = Player_Two.index(Player_Two_Lowest_Value)

#Printed Results
print(f"Player One's Numbers: {Player_One}")
print(f"Player Two's Numbers: {Player_Two}")

print(f"Player One won {Player_One_Wins} times.")
print(f"Player Two won {Player_Two_Wins} times.")

print(f"Player One's highest number is {Player_One_Highest_Value} at index {Player_One_Highest_Index}.")
print(f"Player Two's highest number is {Player_Two_Highest_Value} at index {Player_Two_Highest_Index}.")

print(f"Player One's lowest number is {Player_One_Lowest_Value} at index {Player_One_Lowest_Index}.")
print(f"Player Two's lowest number is {Player_Two_Lowest_Value} at index {Player_Two_Lowest_Index}.")