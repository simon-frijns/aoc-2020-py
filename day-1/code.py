from itertools import combinations
from math import prod 

def getInput(filename) -> list:
    with open(filename) as input:
        return [int(x) for x in input.readlines()]

def solution(input: list, nmb_of_inputs: int) -> int:
    # look for combinations of nmb_of_inputs that sum to 2020, then return their product
    return [prod(combination) for combination in combinations(input, nmb_of_inputs) if sum(combination) == 2020][0]

def test():
    test_input = getInput("test_input.txt")
    assert solution(test_input, 2) == 514579
    assert solution(test_input, 3) == 241861950

if __name__ == "__main__":
    test()
    input = getInput("input.txt")
    print(solution(input, 2))
    print(solution(input, 3))
