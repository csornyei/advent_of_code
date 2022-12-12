from functools import reduce
import operator
import re

f = open("../input.txt")


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)


def set_in_dict(data_dict, map_list, value):
    get_from_dict(data_dict, map_list[:-1])[map_list[-1]] = value


directories = {"/": {}}
current_dir = []
for line in f:
    line = line.strip()
    if line.startswith("$ cd"):
        dir_name = line.split(" ")[2]
        if dir_name == "..":
            current_dir.pop()
        else:
            current_dir.append(dir_name)
    elif line.startswith("dir "):
        dir_name = line.split(" ")[1]
        set_in_dict(directories, current_dir + [dir_name], {})
    elif re.match(r"^\d", line):
        size, file_name = line.split(" ")
        set_in_dict(directories, current_dir + [file_name], int(size))

dir_sizes = []


def get_dir_size(dir_path):
    dir_size = 0
    for key, value in get_from_dict(directories, dir_path).items():
        if type(value) == int:
            dir_size += value
        else:
            dir_size += get_dir_size(dir_path + [key])
    dir_sizes.append(("/".join(dir_path).replace("//", "/"), dir_size))
    return dir_size


total_used_space = get_dir_size(["/"])

s = 0
for path, size in dir_sizes:
    if size <= 100000:
        s += size
# print(s)

ALL_DISK_SPACE = 70000000
UPDATE_SIZE = 30000000

goal = UPDATE_SIZE - (ALL_DISK_SPACE - total_used_space)
print(goal)
huge_enough = []
for path, size in dir_sizes:
    if size >= goal:
        huge_enough.append((path, size))

print(min(huge_enough, key=lambda x: x[1]))
