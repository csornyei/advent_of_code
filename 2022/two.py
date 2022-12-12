file = open("../input.txt")

codes = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

result_codes = {
    "X": "lost",
    "Y": "draw",
    "Z": "win",
}

points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "lost": 0,
    "draw": 3,
    "win": 6
}


def rps(opponent, mine):
    if opponent == "Rock":
        if mine == "Paper":
            return "win"
        elif mine == "Scissors":
            return "lost"
        else:
            return "draw"
    elif opponent == "Paper":
        if mine == "Paper":
            return "draw"
        elif mine == "Scissors":
            return "win"
        else:
            return "lost"
    else:
        if mine == "Paper":
            return "lost"
        elif mine == "Scissors":
            return "draw"
        else:
            return "win"


def get_rps_from_result(result, opponent):
    if result == "lost":
        if opponent == "Rock":
            return "Scissors"
        elif opponent == "Paper":
            return "Rock"
        else:
            return "Paper"
    elif result == "win":
        if opponent == "Rock":
            return "Paper"
        elif opponent == "Paper":
            return "Scissors"
        else:
            return "Rock"
    else:
        return opponent


my_points = 0
for line in file:
    # opponent, mine = line.strip().split(" ")
    # opponent = codes[opponent]
    # mine = codes[mine]
    # result = rps(opponent, mine)
    # my_points += points[mine] + points[result]
    opponent, result = line.strip().split(" ")
    opponent = codes[opponent]
    result = result_codes[result]
    mine = get_rps_from_result(result, opponent)
    my_points += points[mine] + points[result]


print(my_points)
