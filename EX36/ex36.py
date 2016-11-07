from sys import exit

def cave():
	print "You're in a cave, a dragon is living inside to safeguard the magic sword"
	print "You need to take the sword as a weapon to kill the evil king to safe the country"
	print "You can choose 'sing' to make the dragon fall alseep or 'fight' with the dragon"

	action = raw_input("> ")
	
	if action == 'sing':
		print "The dragon fell asleep, you stole the sword and leave!"
		secret_maze()
	elif action == 'fight':
		print "The dragon cuts you into pieces, you're fail..."
		dead()
	else:
		print "Please choose 'sing' or 'fight'"






def secret_maze():
	print "Welcome to the secret maze!"
	print "You have to go in right direction to walk through the maze then enter the king's castle "
	print "There's a crossroad in front of you, you will turn 'left', 'right' or 'say WTF' "
	loop = False

	while True:
		action = raw_input("> ")
		if action == 'left':
			print "Wow! The dragon woke up and robbed the sword back to the cave, You go back to cave!!!"
			cave()

		elif action == 'right':
			print "OH! NO! You were caught up and killed by the soiders "
			dead()
		elif action == 'say WTF':
			print "Thant's the magic word for oppeing the entrence of the castle, you directly skip the maze!"
			castle()
		else:
			print "Please choose 'left', 'right' and 'say WTF'. "
			loop = True

def castle():
	print "Welcome to the castle, the evil king has been waiting you for a loooooog time."
	print "The king has a gun and he's going to shoot you ..."
	print "Input 'skip' to escape the bullets or 'grasp' to catch all the bullets. "
	catch_bullet = False

	while True:
		action = raw_input("> ")
		if action == 'skip':
			print " That's cool ~"
			print " You used your sword to take down the head of evil king. Congratulation!"
			exit(0)
		elif action == 'grasp' and not catch_bullet:
			print "Too many bullets, you can't catch them all, you are dead."
			dead()
		elif action == 'grasp' and catch_bullet:
			print "Fantastic ! You just killed the King with your sword. Congratulation!"
			catch_bullet = True
			exit(0)
		else:
			print "I got no idea what that means."


def dead():
	count()
	print "You're dead. Donate $10 to UNICEF to play again."
	print "'Yes' or 'No' for donation"
	donation = False
	

	while True:
		action = raw_input ("> ")
		if action == 'Yes':
				start()


		elif action =='No':
			print "Bye~"
			exit(0)
		else:
			print "I got no idea what that means."
			donation = True


def start():
	
	print "Please pick a name for your character: 'Lucy' or 'Kevin'."

	action = raw_input("> ")

	if action == 'Lucy':
		print "In fact I think Kevin sounds better, Please restart from Kevin XD"
		start()

	elif action == 'Kevin':
			cave()

def count():
	i = 0
	numbers = []
	while i < 101:
		numbers.append(i)
		i = i + 10
		print numbers, " percent of HP has recovered. "


start()


