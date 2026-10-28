# Task4
def make_hangman(secret_word):
    guesses = []                        # remembered between calls

    def hangman_closure(letter):
        
        guesses.append(letter)                         # add letter to guesses

        display = secret_word           # fresh copy each guess
        for ch in secret_word:          # same loop from assignment1
            if ch not in guesses:
                display = display.replace(ch, "_")
        print(display)

        return "_" not in display                   # 2. True if no "_" left in display

    return hangman_closure

if __name__ == "__main__":
    game = make_hangman(input("Enter a word: ").lower())   # once

    solved = False
    while not solved:
        solved = game(input("Guess a letter: ").lower())   # every turn until solved

    print("You got it!")