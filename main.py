import random

running = True

while running:
    randInput = random.randint(1,3)
    userInput = int(input("ROCK(1) PAPER(2) SCISSORS(3): "))
    if userInput==randInput:
        print("DRAW")
    elif (userInput==1 and randInput==3) or (userInput==2 and randInput==1) or (userInput==3 and randInput==2):
        print("WELL DONE YOU WON")
        running=False
    else:
        print("SORRY, YOU LOST")
