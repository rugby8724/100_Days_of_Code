import random
import hangman_art
import words

word_list = words.word_list
stages = hangman_art.stages
print(hangman_art.logo)

#Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
display = []
for l in range(word_len):
    display += '_'
print(display)
chances= 6
print(stages[chances])

#Ask the user to guess a letter
guessed_letters = []
game_over = False
while not game_over:
    guess = input('Please pick a letter? ').lower()
    if guess in guessed_letters:
        print(f'You have already picked {guess} please pick again')
        guess = input('Please pick a letter? ').lower()
    else:
        guessed_letters += guess
#Check if the letter the user guessed is one_band_name_generator of the letters in the chosen_word.

    if guess not in chosen_word:
        chances -= 1
        print(f'The letter {guess} is not in the word')
        if chances == 0:
            print(f'Sorry you lose, the word was {chosen_word}')
            game_over == True
            break
        else:
            print(display)
            print(stages[chances])
            continue

    for position in range(word_len):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess

    if '_' not in display:
        print(f'Congrats you guessed {chosen_word} correctly')
        game_over = True
    else:
        print(display)






print('Thanks for Playing')
