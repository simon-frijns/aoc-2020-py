from typing import Tuple

def getInput(filename) -> list:
    with open(filename) as input:
         return [str(x) for x in input.readlines()]

def parse_line(line: str) -> Tuple[int, int, str, str]:
    # "1-3 b: cdefg" -> 1, 3, "b", "cdefg"
    line = line.strip().split()
    first, second = map(int, [num for num in line[0].split("-")])
    letter = line[1][0]
    pw = line[2]
    return first, second, letter, pw

def part1(input: list) -> int:
    count = 0
    for line in input:
        lower_bound, upper_bound, letter, pw = parse_line(line)    
        if lower_bound <= pw.count(letter) <= upper_bound:
            count += 1
    return count

def part2(input:list) -> int:
    count = 0
    for line in input:
        first, second, letter, pw = parse_line(line)
        ## XOR -> if letter is present in exactly one of the two positions, increment counter
        if (pw[first - 1] == letter) != (pw[second - 1] == letter):
            count += 1
    return count

def test():
    test_input = getInput("test_input.txt")
    assert part1(test_input) == 2
    assert part2(test_input) == 1

if __name__ == "__main__":
    test()
    input = getInput("input.txt")
    print(part1(input))
    print(part2(input))