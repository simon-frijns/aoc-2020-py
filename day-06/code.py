import re

def get_input(filename) -> list:
    with open(filename) as input:
        return input.read().strip().split("\n\n")

def part1(groups: list) -> int:
    ans = 0
    for group in groups:
        sets_union = set.union(*map(set, group.split())) # from https://stackoverflow.com/a/3852806 - map set function to every element of group, then compute union of all sets in group
        ans += len(sets_union) 
    return ans

def part2(groups: list) -> int:
    ans = 0
    for group in groups:
        sets_intersect = set.intersection(*map(set, group.split())) # exact same approach as above but with intersection instead of union
        ans += len(sets_intersect)
    return ans

def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 11
    assert part2(test_input) == 6

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input))