
def scan(sentence):

	words = sentence.split( )
	result = []

	for word in words:
		get = clasify(word)
		result.append(get)
	return result


def clasify(word):

		if word in ['north', 'south', 'east']:
			return ('direction', word)

		elif word in ['go', 'kill', 'eat']:
			return ('verb', word)

		elif word in ['the', 'in', 'of']:
			return ('stop', word)

		elif word in ['bear', 'princess']:
			return ('noun', word)

		try:	

			thenumber = int(word)
			return ('number', thenumber)

		except ValueError:
			return ('error', word)