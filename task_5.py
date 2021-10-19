
import random
com_score=0
your_score=0
while True:
	print("Enter choice \n 1. rock \n 2. paper \n 3. scissor \n")
	choice = int(input("Your turn: "))
	
	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
	
	if choice == 1:
		choice_made = 'rock'
	elif choice == 2:
		choice_made = 'paper'
	else:
		choice_made = 'scissor'
		
	print("your choice was " + choice_made)
	print("\nNow its computer turn")

	comp_choice = random.randint(1, 3)
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)
	if comp_choice == 1:
		comp_choice_made = 'rock'
	elif comp_choice == 2:
		comp_choice_made= 'paper'
	else:
		comp_choice_made = 'scissor'
		
	print("Computer choice is: " + comp_choice_made)

	print(choice_made + " V/s " + comp_choice_made)
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		print("paper wins ", end = "")
		win = "paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("Rock wins", end = "")
		win = "Rock"
	else:
		print("scissor wins ", end = "")
		win = "scissor"

	if win == choice_made:
		print(" User wins ")
		your_score+=1
	else:
		print(" Computer wins ")
		com_score+=1
	print("you won the game :", your_score )
	print("computers win:", com_score)
	print("Do you want to play again? (Y/N)")
	ans = input()

	if ans == 'n' or ans == 'N':
		break
print("\nThanks!!!!")
