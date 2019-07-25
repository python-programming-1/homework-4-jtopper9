import random

# dictionaries to convert human input, and randint into meaningful values for the program
accepted_human_values = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
machine_values = {0: 'rock', 1: 'paper', 2: 'scissors'}
winner_values = {0: 'Lose', 1: 'Win', 2: 'Draw'}
machine_score = 0
human_score = 0


def play_game(human_move, machine_move):
    # winner variable to log score in global scope
    winner = 0
    if human_move == "r" and machine_move == 1:
        return winner
    elif human_move == "r" and machine_move == 2:
        winner += 1
        return winner
    elif human_move == "r" and machine_move == 0:
        winner += 2
        return winner
    elif human_move == "p" and machine_move == 0:
        winner += 1
        return winner
    elif human_move == "p" and machine_move == 2:
        return winner
    elif human_move == "p" and machine_move == 1:
        winner += 2
        return winner
    elif human_move == "s" and machine_move == 0:
        return winner
    elif human_move == "s" and machine_move == 1:
        winner += 1
        return winner
    elif human_move == "s" and machine_move == 2:
        winner += 2
        return winner


x = random.randint(1, 99)
rock_variable = 33
paper_variable = 66
machine_move = 0

if x <= rock_variable:
    machine_move = 0
elif x > rock_variable and x <= paper_variable:
    machine_move = 1
else:
    machine_move = 2

print("make a move! (r/s/p):")
human_move = input()

if human_move == "sc":
    print("Human: " + str(human_score) + ", Computer: " + str(machine_score))
else:
    game_winner = play_game(human_move, machine_move)
    if game_winner == 0:
        machine_score += 1
    elif game_winner == 1:
        human_score += 1
    print("You chose " + accepted_human_values[human_move] + " and the computer chose " + machine_values[machine_move]
          + ". You " + winner_values[game_winner] + "!")

# adjust weighted variables for random int assignment
if human_move == "r":
    paper_variable += 1
elif human_move == "p":
    paper_variable -= 1
elif human_move == "s":
    rock_variable += 1

# loop to continue providing the option to play while player wants to
while True:
    print("Do you want to play again? (y/n)")
    play_again = input()
    if play_again == "y":
        print("make a move! (r/s/p):")
        x = random.randint(1, 99)
        if x <= rock_variable:
            machine_move = 0
        elif x > rock_variable and x <= paper_variable:
            machine_move = 1
        else:
            machine_move = 2
        human_move = input()
        if human_move == "r":
            paper_variable += 1
        elif human_move == "p":
            paper_variable -= 1
        elif human_move == "s":
            rock_variable += 1
        game_winner = play_game(human_move, machine_move)
        if game_winner == 0:
            machine_score += 1
        elif game_winner == 1:
            human_score += 1
        print("You chose " + accepted_human_values[human_move] + " and the computer chose " + machine_values[
            machine_move] +
              ". You " + winner_values[game_winner] + "!")
    elif play_again == "sc":
        print("Human: " + str(human_score) + ", Computer: " + str(machine_score))
    elif play_again == "n":
        print("Thanks bye!")
        break
