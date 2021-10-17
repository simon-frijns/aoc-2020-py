import re

def get_input(filename) -> list:
    with open(filename) as input:
        return input.read().strip().split("\n\n")

def parse_input(passport: str) -> dict:
    fields = re.split("[\n ]", passport)
    passport_dict = dict(field.split(":") for field in fields)
    return passport_dict

def part1_check(passport_dict: dict) -> int:
    a = 0 
    valid = True
    if not all(field in passport_dict for field in required_fields):
        valid = False
    a += valid
    return a

def part1(input: list) -> int:
    counter = 0
    for passport in input:
        passport_dict = parse_input(passport)
        counter += part1_check(passport_dict)
    return counter

def part2_check(passport_dict: dict) -> int:
    a = 0
    valid = part1_check(passport_dict)   
    if valid:
        # years - check if within bounds
        for year, low, high in year_bounds:
            valid = (valid and low <= int(passport_dict[year]) <= high)
        # height - check if correct format and within bounds
        valid = valid and bool(re.match("^\d+(cm|in)$", passport_dict['hgt']))
        if passport_dict["hgt"].endswith("cm"):
            valid = (valid and 150 <= int(passport_dict["hgt"][:-2]) <= 193)   
        if passport_dict["hgt"].endswith("in"):
            valid = (valid and 59 <= int(passport_dict["hgt"][:-2]) <= 76)              
        # hair colour - regex
        valid = valid and bool(re.match("^[#][\da-f]{6}$", passport_dict["hcl"]))
        # eye colour
        valid = valid and passport_dict["ecl"] in eye_colour
        # PID
        valid = valid and bool(re.match("^\d{9}$", passport_dict["pid"]))
    a += valid
    return a

def part2(input: list) -> int:
    counter = 0
    for passport in input:
        passport_dict = parse_input(passport)
        counter += part2_check(passport_dict)
    return counter

def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 10
    assert part2(test_input) == 6

if __name__ == "__main__":
    required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    year_bounds = [("byr", 1920, 2002), ("iyr", 2010, 2020), ("eyr", 2020, 2030)]
    eye_colour = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input))