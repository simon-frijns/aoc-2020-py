from copy import deepcopy

def get_input(filename) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        input = list(map(list, input))
        return input

def decide_character(character: str, count: int, tolerance: int) -> str:
    c = ''
    if character == 'L' and count == 0:
        c = '#'
    elif character == '#' and count >= tolerance:
        c = 'L'
    else:
        c = character
    return c

def check_adjacent(seats: list, row: int, seat: int) -> str:
    count = 0
    for r_diff in range(-1, 2):
        r = row + r_diff
        for s_diff in range(-1, 2):
            s = seat + s_diff
            if r in range(len(seats)) and s in range(len(seats[0])) and (s_diff, r_diff) != (0,0):
                if seats[r][s] == '#':
                    count += 1
            else:
                continue
    character = decide_character(seats[row][seat], count, 4)
    return character

def check_sight(seats:list, row: int, seat: int) -> str:
    count = 0
    directions = [   [-1,-1],[-1, 0],[-1, 1]
                    ,[ 0,-1],        [ 0, 1]
                    ,[ 1,-1],[ 1, 0],[ 1, 1]]
    for direction in directions:
        keep_looking = True
        r = row
        s = seat
        dy = direction[0]
        dx = direction[1]
        while keep_looking:
            r += dy
            s += dx
            if r in range(len(seats)) and s in range(len(seats[0])):
                if seats[r][s] == '.':
                    continue
                elif seats[r][s] == '#':
                    count += 1
                    keep_looking = False
                elif seats[r][s] == 'L':
                    keep_looking = False
            else:
                keep_looking = False
    character = decide_character(seats[row][seat], count, 5)
    return character

def play_round(seats:list, method: str) -> list:
    # method: 'adjacent' or 'sight'
    new_seats = deepcopy(seats)
    for row in range(len(seats)):
        for seat in range(len(seats[0])):
            if method == 'adjacent':
                character = check_adjacent(seats, row, seat)
            elif method == 'sight':
                character = check_sight(seats, row, seat)
            new_seats[row][seat] = character
    return new_seats

def play_game(seats: list, method: str) -> int:
    ans = 0
    iter_count = 0
    game_running = True
    old_input = seats.copy()  
    new_input = play_round(old_input, method)
    while game_running: # dirty while true, can we make this cleaner?
        old_input = new_input.copy()
        new_input = play_round(old_input, method)
        iter_count += 1
        if old_input == new_input or iter_count >= 200:
            print('terminated with iter_count',iter_count)
            game_running = False
    ans = sum(row.count('#') for row in new_input)
    return ans

def part1(input: list) -> int:
    ans = play_game(input, 'adjacent')
    return ans

def part2(input: list) -> int:
    ans = play_game(input, 'sight')
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 37
    assert part2(test_input) == 26
    
if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 