from itertools import combinations

def get_input(filename) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        input = list(map(int, input)) # input list needs to be ints
        return input

def part1(input: list, preamble: int) -> int:
    ans = 0
    for i in range(preamble, len(input)):
        previous_numbers = set(input[i - preamble:i]) # convert to set because we don't want duplicate combinations
        if not any([x + y == input[i] for x, y in combinations(previous_numbers, 2)]): # if we can't find any combination of 2 items in our set that sums to input
            ans = input[i]
    return ans

def part2(input: list, preamble: int) -> int:
    solution_part1 = part1(input, preamble)
    # double for-loop? see if this can be done cleaner
    for i in range(len(input)):
        for j in range(i+2, len(input)): # i+2 because we want at least 2 numbers previous to our own number, so i and i+1 are irrelevant
            contiguous_set = input[i:j]
            if sum(contiguous_set) == solution_part1:
                ans = min(contiguous_set) + max(contiguous_set)
            if sum(contiguous_set) > solution_part1: # no point in summing if we're already past the target number
                break
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input, 5) == 127
    assert part2(test_input, 5) == 62
    
if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input, 25))
    print(part2(input, 25)) 