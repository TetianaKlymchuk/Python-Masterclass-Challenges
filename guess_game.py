# for i in range(10):
#     print("i is now {}".format(i))
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
# available_exits = ["east", "north east", "south"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
#
# else:
#     print("aren't you glad you got out of there!")
import random

HIGHEST = 1000
answer = random.randint(1, HIGHEST)
print("=================================================")
print("TRY TO  GUESS THE NUMBER IN 10 ATTEMPTS! LETS GO!")
print("=================================================")
print("Please enter a number between 1 and {}: ".format(HIGHEST))

guess = 0
attempt = 0

while guess != answer:
	guess = int(input())

	if attempt == 8:
		print('It is your last attempt! Be careful!')

	if attempt == 9:
		print('You exceeded possible number of attempts... Try again')
		break

	if guess == 0:
		print('See you next time...')
		break

	if guess > answer:
		print("Please guess lower")
	elif guess < answer:
		print("Please guess higher")
	else:
		print("You got it!")

	attempt += 1
