file = open("../input.txt")


def char_to_num(c):
    if ord(c) >= ord("A") and ord(c) <= ord("Z"):
        return (ord(c) - ord("A") + 27)
    else:
        return (ord(c) - ord("a") + 1)


lines = []
for line in file:
    lines.append(line.strip())

file.close()

badges = []
for idx, line in enumerate(lines):
    if idx % 3 != 0:
        continue
    items = {}
    first_line = lines[idx]
    for c in first_line:
        items[c] = True
    second_line = lines[idx + 1]
    keys = list(items.keys())
    for item in keys:
        if second_line.find(item) == -1:
            del items[item]
    third_line = lines[idx + 2]
    for item in items.keys():
        if third_line.find(item) != -1:
            badges.append(char_to_num(item))

print(sum(badges))

# in_both = []
# for line in file:
#   line = line.strip()
#   chars = {}
#   first_part = line[:len(line)//2]
#   second_part = line[len(line)//2:]
#   for c in first_part:
#     chars[c] = True

#   local_in_both = set()
#   for c in second_part:
#     if c in chars:
#       local_in_both.add(c)
#   for c in local_in_both:
#     in_both.append(char_to_num(c))

# print(sum(in_both))
