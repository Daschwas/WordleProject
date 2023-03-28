def pick_word():
"""
This function imports and splits the word list in order to randomly pick a word to be guessed each game.

Parameters:     None
Returns: target_word (random word taken from the text file)

Example: target_word = "Refer"
"""
    words = open("target_words.txt").read().split()
    import random
    target_word = random.choice(words)
    return target_word

def instruction():
"""
This function when called merely prints the instructions for the game so the user is aware of what they need to do.
As such, it does not return any value or contain any parameters.
"""
    print("A word has been chosen. You have five guesses to guess the word. \n ")
    print("With each guess, you will be informed how many letters you got right.")
    print("If you get the right letter and position, it will state G. Otherwise, the right letter will state Y.")
    print("Finally if the letter is not in the mystery word, it will state R.")

def get_guess():
"""
This function evaluates whether the users guess is a valid word by examining whether it is five letters and a word present in the text file.
For the purpose of later comparing the individual character strings, it also renders the guess in lower case.

Parameters:     None
Returns: guess (the current guess as to what the target word is)

Example: 
Enter a five letter word: j
Your guess is not five letters.
Enter a five letter word: aaaaa
Your guess is not a valid word.
Enter a five letter word: sails
#word is then accepted
"""
    valid_words = open("all_words.txt").read().split()
    while True:
        guess = input("Enter a five letter word: ")
        if len(guess) != 5:
            print("Your guess is not five letters.")
            continue
        elif guess not in valid_words:
            print("Your guess is not a valid word.")
            continue
        else:
            guess = guess.lower()
            return guess
#def attempt_tracker():
   # if count == 5:
     #   print("Game over!")
     #   return
   # else:
      #  count = count+1
      #  print("Guess number: " + count)
     #   return count

def wordle_clone():
"""
This function compiles the other functions to create the Wordle clone.
In other words, the function prompts for guesses whilst keep track of the current amount of guesses and providing feedback via coded letters ("G", "Y", "R").
It checks whether the letters are in the current position by splitting the word into individual letters and comparing indexes.
If the user either guesses the word, or hits the guess limit, the game will end and the target word (and overall score) will be revealed.

Parameters:     None
Returns: None

Example:
Enter a five letter word: sails
['G', 'Y', 'R', 'R', 'G']
['s', 'a', 'i', 'l', 's']
['s', 'p', 'e', 'a', 'r']
Enter a five letter word: pears
['Y', 'Y', 'Y', 'Y', 'Y']
['p', 'e', 'a', 'r', 's']
['s', 'p', 'e', 'a', 'r']
Enter a five letter word: ghost
['R', 'R', 'R', 'Y', 'R']
['g', 'h', 'o', 's', 't']
['s', 'p', 'e', 'a', 'r']
Enter a five letter word: paris
['Y', 'Y', 'Y', 'R', 'Y']
['p', 'a', 'r', 'i', 's']
['s', 'p', 'e', 'a', 'r']
Enter a five letter word: spear
You win!
Guesses:
5

Process finished with exit code 0

"""
    target_word = pick_word()
    instruction()
    limit = 6
    count = 1
    #count = attempt_tracker()
    while count < limit:
        guess = get_guess()
        guess_list = list()
        if guess == target_word:
            print("You win!")
            print("Guesses:")
            print(count)
            return
        else:
            cluesguess = [ch for ch in guess]
            cluestarget = [ch for ch in target_word]
            for letter in cluesguess:
                if letter in cluestarget:
                    guess_index = cluesguess.index(letter)
                    target_index = cluestarget.index(letter)
                    if guess_index == target_index:
                        guess_list.append("G")
                    else:
                        guess_list.append("Y")
                else:
                    guess_list.append("R")
            print(guess_list)
            print(cluesguess)
            print(cluestarget)
            count = count+1
            continue
    while count >=limit:
        print("Game over!")
        print("The target word was " + target_word)
        return

wordle_clone()
#to do: remove the word being revealed after each guess (have currently put this in place to more easily debug
#to do: adjust function so it captures correct amount/position when dealing with words containing multiple of the same letter
