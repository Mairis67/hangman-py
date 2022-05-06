import random
import hangman_art
import hangman_words

random_word = random.choice(hangman_words.word_list)

display = []
word_length = len(random_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

for letter in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess letter!\n").lower()

    if guess in display:
        print(f"You've already guessed that letter {guess}")

    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose! The word was {random_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])



