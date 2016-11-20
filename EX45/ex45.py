# -*- coding: utf-8 -*-
# Basic imports for the game
from sys import exit
from random import randint

# Setting Scenes, the parent class.
class Scene(object):

	def enter(self):
		exit(1)

# Subclass
class Fail(Scene):

# Create a list having various and answers.   
	Antwort = [
	     "life is a box of chocolate, don't be sad.",
	     "You fate to be a general person, don't quit your job.",
	     "Bye, at least you've tried.",
	     "More money you have, more responsibility you take, take it easy~"

	]

	def enter(self):
		# Count the numbers of the answers and print the answers randomly.
		print Fail.Antwort[randint(0, len(self.Antwort)-1)]
		exit(1)

class Mom(Scene):

	def enter(self):

		print "Hello! Welcome to the story : THE ADVENTURE OF BEING A MILLIONARIE"
		print "One day You can't stand to live a normal life anymore, "
		print "you are going to have a bet to become the one of the richest people and win uncountable amount of money"
		print "in Las Vegas..."
		print "------------------------------------------ "
		print "First step to be the legend: Tell your mom about your decision. "
		print "You need to choose which way to tell her about your insane idea... "
		print "------------------------------------------ "
		print "1. 'Mom, can you borrow me $10000 for gambling? I'll pay back 10 times. "
		print "2. 'Mom, I need $10000 to date a girl. "
		print "3. 'Mom, my friend is injured, he needs money for hospital care"

		action = raw_input("input number >  ") 
		
		if action == "1":
			
			print "Mom : Are you crazy? Don't be a daydreamer anymore!"
			
			print "You're fail but your think of another way to get the money"
			
			return 'PIN'

		elif  action == "2":
			
			print "Mom : son...True love can't be bought through money."
			
			return 'Fail'

		elif  action == "3":

			print "What a caring child~ but I only can give you $500."

			print "You're fail but your think of another way to get the money"

			return 'PIN'

		else:
			print "Invalid input!"
			
			quit(1)


class PIN(Scene):

	def enter(self):
		
		print "You're sad and angry, so you plan to crack the Safe deposit box at your home."
		
		print "2 _ 6\n3 5 7\n1 3 5 "
		
		print "Just 1 digit is missing"

		pin = "%d" % (randint(1,9))
		
		guess = raw_input("[keypad]> ")
		
		guesses = 1

		while guess != pin and guesses < 7:
							print "You have tried %d time" % guesses
							guesses += 1
							guess = raw_input("[keypad]> ")

		if guess == pin:
			print "What a genius!"

			print "You open the deposit box and take much more money than you expected."

			return 'Gambling'



		elif guess == "4":

			print "That just proves that you have nice logical mind."

			print "Not bad~ Keep trying!"

			return 'PIN'

		else:

			print "This lesson tells you have no luck to be a millionaire..."

			print "Auto defense system is activated, the box blew up"

			return 'Fail'


class Gambling(Scene):

	def enter(self):
		print "You finally get into the casino in Las Vegas"
		
		print "You just put $10000 cash on the table which is playing the Blackjack(Twenty-one)"
		print "Betting who will holds the bigger card at the end "
		print "Now you know that the dealer has 'J' and 'Six'."
		print "To win, you need to have over 17 points and under 21 points in total"

		# Create two lists to the represent the all the poker cards and refers each other.

		cards = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7:"Seven", 
		8:"Eight", 9: "Nine", 10: "Ten", 11: "J", 12: "Q", 13:"K"}

		cards2 = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five" : 5, "Six" : 6, "Seven" : 7, 
"Eight" : 8, "Nine" : 9, "Ten" : 10, "J" : 11, "Q" : 12, "K" : 13} 


		# Take two cards randomly
		FirstCard = cards[randint(1,13)]
		NextCard = cards[randint(1,13)]

		FirstCardEQ = cards2[FirstCard]
		NextCardEQ = cards2[NextCard]
		total =  FirstCardEQ + NextCardEQ
		NewTotal = total + randint(1,13)

		print "You have %s and %s, total: %d" % (FirstCard, NextCard, total)


		# List all the situations might encounter for the game Twenty-One.
		if total >= 21:
			print "The total is more than  21 points, you lost"
			
			return'Reverse'

		if total > 17 and total <= 21:
			print "You finally win, man !"
			print "Congratulation!"
			quit(1)


		while  total <= 17:
			print " 'Continue' or 'Open' ?"
			action = raw_input(">  ")

			if action == "Continue":
				total = total + randint(1,13)
				print "Add one more card, now you have %d points" % total

				if total > 17 and total < 21:
					print "You finally win, man!!"
					print "Tell us what's the smell of million dollars？"
					quit(1)

				elif total > 21:
					print "The total is more than 21 points, you lost"
					return'Reverse'

			if action == "Open" and total <= 17:
				
				print "Now you have %d points is less than 17" % total
				
				print "Such a loser, Bye"
				
				return 'Reverse'

			elif action == "Open":
				
				print "Are you stupid?"

				return 'Reverse'

			else:
				print "Please input correct instruction"


class Reverse(Scene):

	def enter(self):

		print "No worry! You have a super power to back to history, reverse the result"
		print "Just typing the following strings backwards:"
		print "-" * 15
		print "EMOSDNAH=NIVEK"
		print "-" * 15

		action = raw_input("> ")

		if action == "KEVIN=HANDSOME":
			print "Glad to hear that"
			return 'Gambling'

		else:
			print "No hope"
			return 'Fail'

class Map(object):
# create a Map class connect different scenes with a list of words
	scenes = {
	'Mom':  Mom(),
	'PIN': PIN(),
	'Gambling':Gambling(),
	'Reverse': Reverse(),
	'Fail': Fail(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

class Start(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('Fail')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		

a_map = Map('Mom')
a_game = Start(a_map)
a_game.play()
