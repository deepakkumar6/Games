
import random

from words import word_list


def get_word():

    word = random.choice(word_list) # choose any random word

    # idx = random.randint(0,n-1)# index are from 0-n-1
    # word = word_list[idx]

    word = word.upper() # lowercase to upper case

    return word

def play(word):

    word_completion = '*'*len(word) # this is the things will show at each stage

    guessed = False # flag for guessed or not

    guessed_letter = [] # to store the guessed letter till now

    guessed_word = [] # to store the guessed word till now

    tries = 6 # we have 6 life line

    print('Lets Play The Hangman') # ok Lets start

    print(Hangman(tries)) # just for pring

    print(word_completion)

    print()

    while not guessed and tries>0:

        guess = input('Please guess a letter or word : ').upper()

        if len(guess)==1 and guess.isalpha():

            if guess in guessed_letter:
                print("You already guessed the letter",guess)

            elif guess not in word:
                print(guess,"is not in the word.")
                tries -=1
                guessed_letter.append(guess)

            else:
                print('Wow',guess,'is the word!')

                guessed_letter.append(guess)

                word_as_list = list(word_completion) # spliting the string into list

                indices = [idx for idx,letter in enumerate(word) if letter == guess] # this will show all the occurance

                for index in indices:
                    word_as_list[index] = guess

                word_completion = ''.join(word_as_list)

                if '*' not in word_completion:
                    guessed = True




        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print('You alrady guess the word',guess)
            elif guess != word:
                print(guess,"is not in the word")
                tries -= 1
                guessed_word.append(guess)
            else:
                guess = True
                word_completion = word

        else:

            print('uff.. Not a valid guess')

        print(Hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Congrats , you guessed the word! YOu win!')
    else:
        print('uff , You ran out of tries. The word was',word,'. Maybe next time')


def Hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)

    while  input("play Again ? (Y?N)").upper()=='Y':
        word = get_word()
        play(word)

if __name__=='__main__':
    main()











