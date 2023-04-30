import random
Valid_Words_File = "all_words.txt"
valid_words = open(Valid_Words_File).read().split()

def pick_word():
"""
This function imports and splits the word list in order to randomly pick a word to be guessed each game.

Parameters:     None
Returns: target_word (random word taken from the text file)

Example: target_word = "Refer"
"""
    Target_Words_File = "target_words.txt" 
    words = open(Target_Words_File).read().split()
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
    word_limit = 5
    
    while True:
        guess = input("Enter a five letter word: ")
        if len(guess) != word_limit:
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
def replay():
    response = input("Would you like to play again? (Y/N)")
    response = response.upper()
    if response == "Y":
        print("Let's begin!\n")
    else:
        print("Thanks for playing!")
        exit()
"This allows the user to indicate whether they wish to play again, rather than needing to run the program each time"
    
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
['G', 'Y', 'R', 'R', 'R']
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
        Green_Letter = "G"
        Red_Letter = "R"
        Yellow_Letter = "Y"
        #count = attempt_tracker()
        while count < limit:
            for letter in target_word:
                letter_frequency[letter] = 0
            for letter in target_word:
                letter_frequency[letter] += 1
            """ The above counts how many times a letter appears in the target word, with 0 resetting it for each guess.
            This will be used later in the code"""
            guess = get_guess()
            guess_list = list()
            if guess == target_word:
                print("You win!")
                print("Guesses:")
                print(count)
                replay()
                break
            else:
                clues_guess = list(guess)
                clues_target = list(target_word)
                for index, letter in enumerate(clues_guess):
                    if letter in clues_target:
                        if clues_guess[index] == clues_target[index]:
                            clues_guess[index] = "*"
                            letter_frequency[letter] -= 1
                       """
This first for loop is so that all the correct letters in the correct positions can be captured first before determining whether the other letters are correct or not
"""
                for index, letter in enumerate(clues_guess):
                    if letter == "*":
                        guess_list.append(Green_Letter)
                    elif (letter in clues_target) and (letter_frequency[letter] > 0):
                        guess_list.append(Yellow_Letter)
                    else: guess_list.append(Red_Letter)
"""
The second loop then checks each of the other letters and gives "G" to all the letters marked in the previous loop.
Due to the letter frequency counter decreasing with each instance of a letter, as well as the correct position letters already being removed from the word,
the correct amount of letters is reflected whenever the user guesses.
"""
                print(guess_list)
            #print(clues_guess)
            #print(clues_target)
                count = count+1
                continue
        if count >=limit:
            print("Game over!")
            print("The target word was " + target_word)
            replay()

wordle_clone()
