#Name :: Bishwo Dallakoti
#Purpose : Mastermind Lab
#Date : Apr 4

import random

def main():
    COLORS = ['B', 'G', 'K', 'P', 'R', 'Y']

    secret = []
    i = 0
    while i < 4:
        index = random.randint(0, 5)
        color = COLORS[index]
        secret.append(color)
        i = i + 1

    turn = 1
    while turn <= 8:
        print("=============")
        print("Turn", turn)

        guess = input("Enter your guess (B, G, K, P, R, Y): ")

        print("Your guess:", end=" ")
        i = 0
        while i < len(guess):
            print(guess[i], end=" ")
            i = i + 1

        black = 0
        i = 0
        while i < 4:
            if i < len(guess) and guess[i] == secret[i]:
                black = black + 1
            i = i + 1

        guess_b = 0
        guess_g = 0
        guess_k = 0
        guess_p = 0
        guess_r = 0
        guess_y = 0

        code_b = 0
        code_g = 0
        code_k = 0
        code_p = 0
        code_r = 0
        code_y = 0

        i = 0
        while i < 4:
            if i < len(guess):
                if guess[i] == 'B':
                    guess_b = guess_b + 1
                elif guess[i] == 'G':
                    guess_g = guess_g + 1
                elif guess[i] == 'K':
                    guess_k = guess_k + 1
                elif guess[i] == 'P':
                    guess_p = guess_p + 1
                elif guess[i] == 'R':
                    guess_r = guess_r + 1
                elif guess[i] == 'Y':
                    guess_y = guess_y + 1

            if secret[i] == 'B':
                code_b = code_b + 1
            elif secret[i] == 'G':
                code_g = code_g + 1
            elif secret[i] == 'K':
                code_k = code_k + 1
            elif secret[i] == 'P':
                code_p = code_p + 1
            elif secret[i] == 'R':
                code_r = code_r + 1
            elif secret[i] == 'Y':
                code_y = code_y + 1

            i = i + 1

        white = 0

        if guess_b < code_b:
            white = white + guess_b
        else:
            white = white + code_b

        if guess_g < code_g:
            white = white + guess_g
        else:
            white = white + code_g

        if guess_k < code_k:
            white = white + guess_k
        else:
            white = white + code_k

        if guess_p < code_p:
            white = white + guess_p
        else:
            white = white + code_p

        if guess_r < code_r:
            white = white + guess_r
        else:
            white = white + code_r

        if guess_y < code_y:
            white = white + guess_y
        else:
            white = white + code_y

        white = white - black

        print("Results: Black", black, "White", white)

        if black == 4:
            print("============")
            print("You Win!  The secret code was ", end="")
            i = 0
            while i < 4:
                print(secret[i], end="")
                i = i + 1
            print(".")
            return "done"

        turn = turn + 1

    print("====================================")
    print("You Lose! The secret code was ", end="")
    i = 0
    while i < 4:
        print(secret[i], end="")
        i = i + 1
    print(".")

main()
