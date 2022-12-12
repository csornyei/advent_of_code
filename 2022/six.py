file = open("../input.txt")

content = file.read()


def get_code(text):
    for idx, char in enumerate(text):
        if idx < 14:
            continue
        textChars = text[idx-14:idx + 1]
        s = set(textChars)
        if len(s) == 14:
            text = "".join(s)
            print(idx+1)
            print(text)
            break


get_code("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
get_code("bvwbjplbgvbhsrlpgdmjqwftvncz")
get_code("nppdvjthqldpwncqszvftbrmjlhg")
get_code("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
get_code("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")

get_code(content)
