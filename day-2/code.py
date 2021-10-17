def getInput(filename) -> list:
    with open(filename) as input:
         return [str(x) for x in input.readlines()]

def test():
    test_input = getInput("test_input.txt")
    assert part1(test_input) == 2

def part1(input: list) -> int:
    count = 0
    for line in input:
        line = line.strip().split()
        lower_bound, upper_bound = map(int, [num for num in line[0].split("-")])
        letter = line[1][0]
        pw = line[2]
    
        if lower_bound <= pw.count(letter) <= upper_bound:
            count = count + 1

    return count

if __name__ == "__main__":
    test()
    input = getInput("input.txt")
    print(part1(input))