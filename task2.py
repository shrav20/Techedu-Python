def computer_guess(n):
    l = 1
    h = 100
    guess = (l+h)//2
    while guess != n:
        guess = (l+h)//2
        print("The computer guesses", guess)
        if guess > n:
            h = guess
        elif guess < n:
            l = guess + 1

    print("The computer guessed", guess, "and it is correct!")


def main():
    n = int(input("Enter a number of your choice: "))
    if n < 1 or n > 100:
        print("Must be in range [1, 100]")
    else:
        computer_guess(n)

if __name__ == '__main__':
    main()
