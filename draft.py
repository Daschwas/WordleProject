import random

valid_words_file = "all_words.txt"
with open(valid_words_file) as text:
    valid_words = text.read().split()
target_words_file = "target_words.txt"
with open(target_words_file) as guess_text:
    words = guess_text.read().split()


def pick_word():
    """This function imports and splits the word list in order to randomly pick a word to be guessed each game.

    Parameters:     None
    Returns: target_word (random word taken from the text file)

    Example: target_word = "Refer"
    """
    target_word = random.choice(words)
    return target_word


def instruction():
    """This function when called merely prints the instructions for the game so the user knows what they need to do.
    As such, it does not return any value or contain any parameters.
    """
    print("A word has been chosen. You have five guesses to guess the word. \n ")
    print("With each guess, you will be informed how many letters you got right.")
    print('If you get the right letter and position, it will state \"+\". ')
    print('Otherwise, having the right letter only will state \"?\".')
    print("Finally if the letter is not in the mystery word, it will state \"-\".")


def get_guess():
    """This function evaluates whether the users guess is a valid word by examining whether it is five letters and a
    word present in the text file. For the purpose of later comparing the individual character strings, it also renders
    the guess in lower case.

    Parameters:     None
    Returns: guess (the current guess as to what the target word is)

    Example:
    Enter a five-letter word: j
    Your guess is not five letters.
    Enter a five-letter word: aaaaa
    Your guess is not a valid word.
    Enter a five-letter word: sails
    word is then accepted
    """
    word_limit = 5
    while True:
        guess = input("Enter a five letter word: ")
        guess = guess.lower()
        if len(guess) != word_limit:
            print("Your guess is not five letters.")
            continue
        elif guess not in valid_words:
            print("Your guess is not a valid word.")
            continue
        else:
            return guess


def replay(total_count, matches):
    """This allows the user to choose to play again, rather than needing to run the program each time
    Additionally, it works out the average amount of guesses from all successful games as per the updated customer
    requirements.
    """
    response = input("Would you like to play again? (Y/N)")
    response = response.upper()
    if response == "Y":
        print("Let's begin!\n")
        return True
    else:
        if matches > 0:
            average = float(total_count/matches)
            print("Average guesses: " + str(average) + " guesses across " + str(matches) + " won games.")
            print("Thanks for playing!")

        else:
            print("No games won today!")
        return False


def history_won(target_word, count):
    """As per the client's request, this function keeps a record of all played games, by writing the secret word
    and the guesses needed to identify it in a separate text file.
    """
    word_document = open("secret_word_history.txt", "a+")
    word_document.write("\n" + '"' + str(target_word) + '" ' + "took " + str(count) + " guesses!")
    word_document.close()


def history_loss(target_word):
    """As per the client's request, this function keeps a record of all played games, by writing the secret word
    and the fact that the user failed to guess it in a separate text file.
    """
    word_document = open("secret_word_history.txt", "a+")
    word_document.write("\n" + 'Failed to guess "' + str(target_word) + '"!')
    word_document.close()


def wordle_clone():
    """This function compiles the other functions to create the Wordle clone.
    In other words, the function prompts for guesses whilst keep track of the current amount of guesses and
    providing feedback via coded symbols ("+", "-", "?"). It checks whether the letters are in the current position by
    splitting the word into individual letters and comparing indexes. If the user either guesses the word, or hits the
    guess limit, the game will end and the target word (and overall score) will be revealed. Two loops are implemented
    with the first ensuring all correct letters in the correct position can be captured before other "types" of letters.

    Parameters:     None
    Returns: None

    Example:
    Enter a five-letter word: sails
    + ? - - -
    s a i l s
    Enter a five-letter word: pears
    ? ? ? ? ?
    p e a r s
    Enter a five-letter word: ghost
    - - - ? -
    g h o s t
    Enter a five-letter word: Paris
    ? ? ? - ?
    p a r i s
    Enter a five-letter word: spear
    You win!
    Guesses:
    5

    Process finished with exit code 0
    """
    total_count = 0
    matches = 0
    flag = True
    while flag:
        target_word = pick_word()
        instruction()
        limit = 6
        count = 1
        correct_position = "+"
        incorrect_letter = "-"
        correct_letter = "?"
        failsafe = "fail"
        letter_frequency = {}

        while count < limit:
            guess = get_guess()
            guess_list = list()

            if guess == target_word:
                print("You win!")
                print("Guesses:")
                print(count)
                history_won(target_word, count)
                matches = matches+1
                failsafe = "safe"
                total_count = total_count+count
                count = (limit + 1)
                flag = replay(total_count, matches)
                continue
            else:
                clues_guess = list(guess)
                print_guess = list(guess)
                clues_target = list(target_word)
                for letter in target_word:
                    letter_frequency[letter] = 0
                for letter in target_word:
                    letter_frequency[letter] += 1
                for index, letter in enumerate(clues_guess):
                    if letter in clues_target:
                        if clues_guess[index] == clues_target[index]:
                            clues_guess[index] = "*"
                            letter_frequency[letter] -= 1
                for index, letter in enumerate(clues_guess):
                    if letter == "*":
                        guess_list.append(correct_position)
                    elif (letter in clues_target) and (letter_frequency[letter] > 0):
                        guess_list.append(correct_letter)
                        letter_frequency[letter] -= 1
                    else:
                        guess_list.append(incorrect_letter)
                print(" ".join(guess_list))
                print(" ".join(print_guess))
                count = count + 1
                if (limit - count) > 1:
                    print("You have " + str(limit - count) + " guesses left!")
                elif (limit - count) == 1:
                    print("You have 1 guess left!")
                continue
        if count >= limit and failsafe == "fail":
            print("Game over!")
            print("The target word was " + target_word + ".")
            history_loss(target_word)
            flag = replay(total_count, matches)


wordle_clone()
