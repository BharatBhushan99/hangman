import random
import hangman_ascii
import hangman_words

print(hangman_ascii.logo)

word_display = []
lives = 6

chosen_word = random.choice(hangman_words.word_list)

for _ in range(0,len(chosen_word)):
  word_display.append("_")

while "_" in word_display and lives > 0:
  
  user_guess = input("Guess a letter: ").lower()

  if user_guess in word_display:
    print("You already guessed this letter.")

  elif user_guess in chosen_word:
    
    for index, letter in enumerate(chosen_word):
      if letter == user_guess:
        word_display[index] = user_guess
  else:
    print("You guessed " + user_guess + ", which is not in the word. You lose a life.")
    print(hangman_ascii.stages[lives])
    lives -= 1
  
  print(" ".join(word_display) + "\n")

if lives == 0:
  print(hangman_ascii.stages[lives])
  print("You lost.")
  print("The word was "+ chosen_word + ".")
else:
  print("You won.")