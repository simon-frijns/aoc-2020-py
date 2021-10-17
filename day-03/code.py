def getInput(filename) -> list:
    with open(filename) as input:
        return [line.strip() for line in input.readlines() if line.strip()]

def tobbogan(input: list, slopes: list) -> int:
    answer = 1
    input_len = len(input)
    line_len = len(input[0])
    for slope_x, slope_y in slopes:
        row, col = 0, 0
        counter = 0
        while row < input_len:
            counter += input[row][col] == "#"
            row += slope_y
            col += slope_x
            col %= line_len
        answer *= counter
    return answer

def test():
    test_input = getInput("test_input.txt")
    assert tobbogan(test_input, [(3,1)]) == 7
    assert tobbogan(test_input, slopes) == 336

if __name__ == "__main__":
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    test()
    input = getInput("input.txt")
    print(tobbogan(input, [(3,1)]))
    print(tobbogan(input, slopes))