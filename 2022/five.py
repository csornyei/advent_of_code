file = open("../input.txt")

crate_lines = []
move_lines = []
is_crate_line = True
for line in file:
    if len(line.strip()) == 0:
        is_crate_line = False
        continue
    if is_crate_line:
        crate_lines.append(line)
    else:
        move_lines.append(line.strip())


def lines_to_storage(lines):
    crates = []

    idx = 0
    for line in lines:
        crates.append([])
        for i in range(0, len(line), 4):
            crates[idx].append(line[i:i+4].strip())
        idx += 1

    storage = {}

    titles = crates.pop()

    for title in titles:
        storage[title] = []

    for line in crates[::-1]:
        for idx, crate in enumerate(line):
            crate = crate.strip()
            if len(crate) > 0:
                storage[f"{idx + 1}"].append(crate)

    return storage


def move(storage, f, t):
    crate = storage[f].pop()
    storage[t].append(crate)
    return storage


def get_move_attributes_from_line(line):
    words = line.split(" ")
    return [words[1], words[3], words[5]]


def move_many(storage, line):
    repeat, f, t = get_move_attributes_from_line(line)
    for _ in range(0, int(repeat)):
        storage = move(storage, f, t)
    return storage


def move_many_keep_order(storage, line):
    amount, f, t = get_move_attributes_from_line(line)
    remaining = storage[f][:len(storage[f]) - int(amount)]
    removed = storage[f][len(storage[f]) - int(amount):]
    storage[f] = remaining
    storage[t] += removed


storage = lines_to_storage(crate_lines)
for line in move_lines:
    # storage = move_many(storage, line)
    move_many_keep_order(storage, line)

tops = ""
for k in storage:
    top = storage[k][len(storage[k]) - 1]
    t = top[1]
    tops += t
print(tops)
