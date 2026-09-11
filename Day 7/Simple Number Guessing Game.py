secret = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
