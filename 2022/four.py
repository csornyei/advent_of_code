file = open("../input.txt")


def split_range(r):
    return map(lambda x: int(x), r.split("-"))


def fully_contains(first_range, second_range):
    first_start, first_end = split_range(first_range)
    second_start, second_end = split_range(second_range)
    if first_start >= second_start:
        if first_end <= second_end:
            return True
    return False


def is_overlap(first_range, second_range):
    first_start, first_end = split_range(first_range)
    second_start, second_end = split_range(second_range)
    return first_start <= second_start <= first_end or second_start <= first_start <= second_end


fully_contains_counter = 0
overlap_counter = 0
for line in file:
    line = line.strip()
    first_elf, second_elf = line.split(",")

    if is_overlap(first_elf, second_elf):
        overlap_counter += 1
    if fully_contains(first_elf, second_elf):
        fully_contains_counter += 1
    elif fully_contains(second_elf, first_elf):
        fully_contains_counter += 1

print(fully_contains_counter)
print(overlap_counter)
