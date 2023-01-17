# TODO: display the correct guesses in their position -> dictionary? look into mapping
# TODO: add ability to guess the entire word
# TODO: guessing the same letter twice breaks it
# TODO: create formatted_display_word once

import os
import requests

# configs

# difficulty setting
max_guess = 10
# init game counter
i = 0

# static answer
answer ='pattern'
# static list of answer characters
list_answer = list(answer)
# list to keep track of letters left to guess
word = list(answer)
# list to keep track of guessed letters
guesses = []
incorrect_guesses = []
# to display list of guessed letters as a string
display_word = []
word_len = len(answer)

# create blank word
for ans in range(len(answer)):
	display_word.append('_')

# init
print('\nWelcome to Hangman.\n')
print('Try guessing the letters (a-z) of a 6 letter word. Use lowercase.\n')
print(f"The word has {word_len} letters and you have {max_guess} guesses.\nYou can input only one letter at a time.")

# start the game
while i < max_guess: # loops through max_guess
	guess_input = input("What's your guess?\n")
	# insert input checking here
	# repeated guess
	if guess_input in guesses or guess_input in incorrect_guesses:
		print('You guessed this, try something new.')
		continue
	# correct guess
	elif guess_input in word:
		for x in range(len(word)):
			if guess_input in word:
				word.remove(guess_input)
				guesses.append(guess_input)
		# winning the game
		if sorted(answer) == sorted(guesses):
			print(f"\nCongrats! You guessed the entire word: {answer}.")

			if i == 1:
				print(f"You used {i} guess.\n")
			else:
				print(f"You used {i} guesses.\n")
			break
		# getting a correct letter
		else:
			for y in range(len(answer)):
				if guess_input == list_answer[y]:
					display_word[y] = guess_input

			formatted_display_word = ''.join(str(y) for y in display_word)
			print(f"\n{formatted_display_word}")
			print('Nice, you got a letter right. Try another.\n')
			continue
	# incorrect guess
	else:
		# getting an incorrect letter
		if i < max_guess-1:
			i += 1
			incorrect_guesses.append(guess_input)
			print(f"\nBad guess. You have {max_guess-i} left.\n")
		# losing the game
		else:
			print(f"\nYou lost the game. {max_guess} guesses have been reached")
			print(f"You guessed the following: {incorrect_guesses}")
			break