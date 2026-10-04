#snake water gun game rules
#1 sanke defeats water
#2 water defeats gun
#3 gun defeats snake
import random
print("Let's play Snake Water Gun ")
print("Sanke: s, Water: w, Gun: g")
rounds = int(input("Enter the number of rounds: "))


win_against = {"s": "w", "w": "g", "g": "s"}  #simple stronger ones are keys and which they can defeat is their values like snake > water
characters = ["s","w","g"]

h_score = 0
c_score = 0

for i in range(rounds):
    choice = input("Enter your choice: ").lower()
    if(choice not in characters):
        print("Invalid Input, Please only between 's','w' or 'g' only.") #if any user entered something else apart "s,"wand "g", we should capture it
        choice = input("Enter your choice again: ")

    computer = random.choice(characters) #randomly choosing from character list

    if(choice == computer):
        print(f"{choice} vs {computer}")
        print("It's a draw")
    # elif((choice == "s" and computer == "w") or (choice == "g" and computer == "s") or (choice == "w" and computer == "g") ):
    elif(win_against[choice] == computer):   #to reduce these checks we use our dictionary, choice is "s" then value is "w" and if computer also "w" than defeated 
        h_score+=1
        print(f"{choice} vs {computer}")
        print("You score 1 point")
    else:
        c_score+=1
        print(f"{choice} vs {computer}")

        print("Computer score 1 point")


if(h_score > c_score):
    print("You have won the game \N{grinning face}")
elif(h_score == c_score):
    print("It's a tie")
else: 
    print("Computer have won the game \U0001F614")

print(f"Your score: {h_score}, Computer's Score: {c_score}")  