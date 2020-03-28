import random

def play_again():
    answer = input('DO YOU WANT TO PLAY AGAIN??? YES OR NO').lower()
    if answer == "y" or answer == "yes":
        play_game()
    else:
        pass

def get_word():
    words = ['cat', 'act', 'dog', 'python', ' monkey', 'snake']
    return random.choice(words)

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    letters_guessed = []
    tries = 10
    guessed = False

    print('The word contains', len(word), 'letters.')
    print(len(word) * '*')
    while guessed == False  and tries > 0:
        print("You have :" + str(tries) + 'tries')
        guess = input('Please enter onle letter or the full word.').lower()

        if len(guess) == 1:
            if guess not in alphabet:
                print('You have not entered a letter.')
            elif guess in letters_guessed:
                print('You have already gussed that letter before.')
            elif guess not in word:
                print("Sorry, that letter is not part of the word :( ")
                letters_guessed.append(guess)
                tries -=1
            elif guess in word:
                print('Well Done, That letter is in the word')
                letters_guessed.append(guess)
            else:
                print("ERROR ERROR ERROR xDDDDDD")

        elif len(guess) == len(word):
            if guess == word:
                print('Well done , You have guessed  the word' )
                guessed = True
            else:
                print("Sorry, That was not the correct word")
                tries -= 1

        else:
            print("The Length of the word is not the same as the length of the word : " )

        status = ''

        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == word:
            print('Well done , you have gussed the word')
            guessed = True
        elif tries == 0:
            print('You Have run out of tries !! Sorry')

    play_again()

play_again()
            
