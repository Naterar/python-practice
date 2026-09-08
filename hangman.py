from random_word import RandomWords  # type: ignore

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

r = RandomWords()
word = r.get_random_word()

lives = 6
display = []
for letter in word:
    display.append("_")

while lives > 0:
    guess = input("Guess a letter: ").lower()

    for position in range(len(word)):
        if word[position] == guess:
            display[position] = guess

    print(" ".join(display))

    if guess not in word:
        lives -= 1
        print(stages[lives])

    if "_" not in display:
        print(f"YOU WIN! The word was {word}")
        break

# FIX 2: removed the else: pass

if lives == 0:
    print(f"YOU GOT HANGED! The right word was {word}")
