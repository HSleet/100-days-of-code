import random
import urllib.request as request

# Constants
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
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

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                   
print(logo)
wordlist_url = "https://www.mit.edu/~ecprice/wordlist.10000"
words = request.urlopen(wordlist_url).read().decode("utf-8").splitlines()
word_list = list(filter(lambda word: len(word) > 5, words))
chosen_word = random.choice(word_list)

# console testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for letter in chosen_word]
wrong_guess_count = 0
lives = 6
letters_tried = []

while "_" in display:
    print(stages[lives])
    print("".join(display))
    print("\nLetters tried: " + ", ".join(letters_tried))
    print(f"\nYou have {lives} lives left.")
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha():
        print("\nPlease enter a letter from a-z")
        continue
    
    if len(guess) > 1:
        print("\nPlease enter only one letter")
        continue
    
    if guess in letters_tried:
        print(f"\nYou've already guessed {guess}")
        continue
    
    letters_tried.append(guess)
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        lives -= 1
        if lives == 0:
            print("You lose!")
            break
        continue   
    else:
        
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter


else:
    print("You win!")