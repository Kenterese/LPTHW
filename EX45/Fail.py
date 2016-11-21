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