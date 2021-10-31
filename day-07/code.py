import re

def get_input(filename) -> list:
    with open(filename) as input:
        return input.read().strip().split("\n")

def parse_input(input:list) -> dict:
    bags = {}
    for line in input: # parse input to obtain a set of bag and contents
        bag, _ = line.split(' bags contain ') 
        bags[bag] = re.findall('(\d+?) (\w+ \w+) bags?',line) # creates dict in the shape 'bag': [('1', 'bag'), ('4', 'bag')]
    return bags

def part1(input: list) -> int:
    ans = 0
    bags = parse_input(input)
    for bag in bags:
        ans += contains_shiny_gold(bags, bag) # abusing the fact True == 1
    return ans - 1 # -1 to remove shiny gold bag from set
 
# Recursive
# if the colour we encounter is shiny gold, return True. 
# Otherwise, go dig into the bags contained in this bag, etc, until we (potentially) hit a shiny gold and return True, or return False if we have to stop digging.
def contains_shiny_gold(bags: dict, bag: str) -> bool:
    if bag == 'shiny gold':
        a = True
    else:
        return any(contains_shiny_gold(bags, bag) for _, bag in bags[bag]) # we use _, bag to ignore the int in the first spot of every bag
    return a 

# Recursive
# If the list is empty, we return 0
# Otherwise, we sum for each bag encountered along the way
# Need to do +1 because we're multiplying - an empty list means 1 bag
def contains_bags(bags:dict, bag:str) -> int:
    return 1 + sum(int(amount) * contains_bags(bags, b) for amount, b in bags[bag])

def part2(input: list) -> int:
    ans = 0
    bags = parse_input(input)
    ans = contains_bags(bags, 'shiny gold')
    return ans - 1 # -1 to remove shiny gold bag from set

def test():
    test_input = get_input("test_input.txt")
    test_input_2 = get_input("test_input_2.txt")
    assert part1(test_input) == 4
    assert part2(test_input) == 32
    assert part2(test_input_2) == 126

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input))