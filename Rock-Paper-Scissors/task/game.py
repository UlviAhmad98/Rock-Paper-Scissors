import random

n_file = open("rating.txt", "r")
n_list = [line.split() for line in n_file]
n_dict = {line[0]: int(line[1]) for line in n_list}

loss_dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
win_dict = {"paper": "rock", "scissors": "paper", "rock": "scissors"}
game_tools = ["rock", "paper", "scissors"]

user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

if user_name in n_dict:
    score = n_dict[user_name]
else:
    score = 0

rules = input()
print("Okay, let's start")

while True:
    main_list = list()
    beaten_by = list()
    defeat = list()
    user_input = input()
    computer_random = random.choice(game_tools)
    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(f"Your rating is: {score}")
    elif user_input not in game_tools:
        print("invalid input")
    else:
        if rules == "":
            if win_dict[user_input] == computer_random:
                print(f"Well done. The computer chose {computer_random} and failed")
                score += 100
            elif loss_dict[user_input] == computer_random:
                print(f"Sorry, but the computer chose {computer_random}")
            elif user_input == computer_random:
                print(f"There is a draw ({computer_random})")
                score += 50
        else:
            main_list = rules.split(",")

            threshold = (len(main_list) - 1) // 2

            start = main_list.index(user_input) + 1
            end = main_list.index(user_input) + threshold + 1
            finish = main_list.index(user_input)

            if (len(main_list) - start) < threshold:
                beginning_index = threshold - (len(main_list) - start)
                beaten_by = main_list[start: end]
                for x in range(beginning_index):
                    beaten_by.append(main_list[x])
                begin = main_list.index(beaten_by[-1]) + 1

            else:
                beaten_by = main_list[start : end]

            for x in beaten_by:
                main_list.remove(x)
            main_list.remove(user_choice)
            defeat = main_list
            if computer_random in defeat:
                print(f"Well done. The computer chose {computer_random} and failed")
                score += 100
            elif computer_random in beaten_by:
                print(f"Sorry, but the computer chose {computer_random}")
            elif user_input == computer_random:
                print(f"There is a draw ({computer_random})")
                score += 50

n_file.close()
