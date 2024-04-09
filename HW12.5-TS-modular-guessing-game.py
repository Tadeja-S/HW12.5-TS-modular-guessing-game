# HW12.5-TS-modular-guessing-game
# Igra ugibanja števila, ki najprej pozdravi igralca in ga prosi za ime. 
# Nato igralcu ponudi 3 možnosti: igranje, ogled najboljših treh rezultatov ali izhod.
# Če igralec izbere igranje, mu ponudi lažjo in težjo raven igre. 
# Igralec izbere raven igre ter začne ugibati.
# Pri lažji ravni mu ponudi namige, pri težji ne.
# Ko igralec pravilno ugane, se razultati zapišejo v slovar.
# Igralcu ponudi ponovno izbiro: igranje, ogled najboljših rezultatov ali izhod.

import datetime
import random
import json
import operator

with open("scores.json", "r") as scores_file:
    scores_list = json.loads(scores_file.read())

name = 0
name = input("Hello! What is your name? ")
print(f"Welcome, {name}!")

def play_game():
    secret = random.randint(1, 20)
    attempts = 0
    guess = 0
        
    while True:
        guess = int(input("Guess the secret number (between 1 and 20): "))
        attempts += 1

        if guess == secret:
            scores_list.append({"player": name, "secret_number": guess, "attempts": attempts, "date": str(datetime.datetime.now())})
            with open("scores.json", "w") as scores_file:
                scores_file.write(json.dumps(scores_list))     
            print("Congratulations!") 
            break
        elif guess > secret and level.lower() == easy:
            print("Try a smaller number.")
        elif guess < secret and level.lower() == easy:      
            print("Try a bigger number.")
        else:
            print("Wrong!")

def get_top_scores():
    with open("scores.json", "r") as scores_file:
        scores_list = json.loads(scores_file.read())
        sorted_list = sorted(scores_list, key=operator.itemgetter("attempts"))[:3]
        for scores_dict in sorted_list:
            print(scores_dict["player"] + " guessed the secret number " + str(scores_dict["secret_number"]) + " in " + str(scores_dict["attempts"]) + " attempts, date: " + scores_dict["date"])

while True:
    print("Would you like to: A) Play a new game? B) See the top scores? C) Exit.")
    selection = input("Answer: ")

    if selection.upper() == "A":
        level = input("Choose level (easy / hard): ")
        easy = "easy"
        play_game()
    elif selection.upper() == "B":
        get_top_scores()
    else:
        break