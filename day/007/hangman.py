import random
import hangman_arts  
import hangman_words 

chosen_word = random.choice(hangman_words.word_list)
lives = 6

print(hangman_arts.logo)
print(f'Pssst, the solution is {chosen_word}.') 

display = []
word_length = len(chosen_word)
for i in range(word_length):
	display.append('-')
print(f"{' '.join(display)}")

while '-' in display:
	if lives == 0:
		print("You lose")
		exit()

	guess = input("Guess a letter: ").lower()

	if guess in display:
		print(f"You've already guessed {guess}")

	for i in range(word_length):
		if chosen_word[i] == guess:
			display[i] = guess

	if  guess not in chosen_word:
		lives -= 1
		print(f"You guesses {guess}, that's not in the word. You lose a life.")
		print(hangman_arts.stages[lives])

	print(f"{' '.join(display)}")

print("You win")
