from itertools import combinations

def getInput(filename) -> list:
    with open(filename) as input:
        return [int(x) for x in input.readlines()]

def part1(input: list) -> int:
    answer = 0
    for a,b in combinations(input, 2):
        if a + b == 2020:
            answer = a * b
    return answer    

def part2(input: list) -> int:
    answer = 0
    for a,b,c in combinations(input, 3):
        if a + b + c == 2020:
            answer = a * b * c
    return answer  

def test():
    test_input = getInput("test_input.txt")
    assert part1(test_input) == 514579
    assert part2(test_input) == 241861950

if __name__ == "__main__":
    test()
    input = getInput("input.txt")
    print(part1(input))
    print(part2(input))
