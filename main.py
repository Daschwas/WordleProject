def pick_word():
    words = open("target_words.txt").read().split()
    import random
    target_word = random.choice(words)
    return target_word

def instruction():
    print("A word has been chosen. You have five guesses to guess the word. \n ")
    print("With each guess, you will be informed how many letters you got right.")
    print("If you get the right letter and position, it will state G. Otherwise, the right letter will state Y.")
    print("Finally if the letter is not in the mystery word, it will state R.")

def get_guess():
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
def attempt_tracker():
    if count == 5:
        print("Game over!")
        return
    else:
        count = count+1
        print("Guess number: " + count)
        return count

def wordle_clone():
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