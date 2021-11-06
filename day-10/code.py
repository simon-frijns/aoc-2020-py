def get_input(filename) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        input = list(map(int, input)) # input list needs to be ints
        input = add_start_and_end(input)
        return input

def add_start_and_end(input: list) -> list:
    start_and_end = [0, max(input)+3]
    input.extend(start_and_end)
    return sorted(input)

def part1(input: list) -> int:
    ans = 0
    one_diff = 0
    three_diff = 0
    for i in range(len(input)-1):
        diff = input[i+1] - input[i]
        if diff == 1:
            one_diff += 1
        elif diff == 3:
            three_diff += 1
    ans = one_diff * three_diff
    return ans


def part2(input: list) -> int:
    ans = 0
    known_routes = {} # dictionary of known routes for each index in form {index : # of routes}
    def find_routes(index): # for a provided index, find the number of routes to reach the end
        ans = 0
        # 3 options 
        #   1. we're at the end, in which case there's only 1 way
        #   2. we're at a point of which we've already determined the # of routes, so we look back in known_routes and use that
        #   3. we're at a new point, in which case we need to first compute how many routes there are
        # effectively, this approach first goes to the last point, then folds back, each time computing how many routes there are for the current index
        if index == len(input) - 1:
            ans = 1
        elif index in known_routes:
            ans = known_routes[index]
        else:
            # if we're at a new point, loop over all subsequent values from this point, and count how many routes there are
            for j in range(index + 1, len(input)):
                if input[j]-input[index]<=3:
                    ans += find_routes(j)
            known_routes[index] = ans
        return ans
    ans = find_routes(0)
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    test_input_2 = get_input("test_input_2.txt")
    assert part1(test_input) == 35
    assert part1(test_input_2) == 220
    assert part2(test_input) == 8
    assert part2(test_input_2) == 19208
    
if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 