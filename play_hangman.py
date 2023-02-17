# TODO: import Hangman as a module
# TODO: add __name__ main logic to file executing the game

class Hangman:
	def __init__(self, max_guess):
		self.max_guess = max_guess
		self.correct_guess = []
		self.incorrect_guess = set([])
		self.answer = 'pattern'
		self.state = 'playing'

	def guess(self, player_input):
		if player_input in self.answer:
			self.correct_guess.append(player_input)
			if set(self.correct_guess) == set(self.answer):
				self.state = 'win'
		else:
			self.incorrect_guess.add(player_input)
			print('Wrong guess.')

			if len(self.incorrect_guess) == self.max_guess:
				self.state = 'lose'
				# return self.incorrect_guess


# playing the game
print('\nWelcome to Hangman.\n')
print('Try guessing the letters (a-z) of a 6 letter word. Use lowercase.\n')

play_hangman = Hangman(3)

while play_hangman.state == 'playing':
	player_input = input('Try guessing a letter.\n')
	play_hangman.guess(player_input)
if play_hangman.state == 'win':
	print(f'You won! You guessed the word {play_hangman.answer}')
else:
	print('You lost!\n')
	print(f'You used {play_hangman.max_guess} guesses. Here were your guesses: {play_hangman.incorrect_guess}')