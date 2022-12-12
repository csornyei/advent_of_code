
f = open("../input.txt")
calories = 0
max_calories = 0
elves_calories = []

for line in f:
    line = line.strip()
    if len(line) == 0:
        elves_calories.append(calories)
        if calories > max_calories:
            max_calories = calories
        calories = 0
    else:
        calories = calories + int(line)

elves_calories.sort(reverse=True)


print(elves_calories[0])
print(elves_calories[1])
print(elves_calories[2])

print(sum([elves_calories[0], elves_calories[1], elves_calories[2]]))
