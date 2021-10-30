def get_input(filename) -> list:
    with open(filename) as input:
        return input.read().strip().split("\n")

def find_row(input: str) -> int:
    low = 0
    high = 128
    for character in input:
        middle = (low + high) // 2
        if character == 'B':
            low = middle
        elif character == 'F':
            high = middle
    return low

def find_col(input: str) -> int:
    low = 0
    high = 8
    for character in input:
        middle = (low + high) // 2
        if character == 'R':
            low = middle
        elif character == 'L':
            high = middle
    return low

def find_seat_id(row_num: int, col_num: int) -> int:
    return row_num * 8 + col_num

def part1(input: list) -> int:
    ans = 0
    for bsp in input:
        seat_id = find_seat_id(find_row(bsp[:7]), find_col(bsp[7:]))
        ans = max(ans, seat_id)
    return ans

def part2(input: list) -> int:
    ans = 0
    seat_ids = []
    for bsp in input:
        seat_id = find_seat_id(find_row(bsp[:7]), find_col(bsp[7:]))
        seat_ids.append(seat_id)
    for seat_id in range(128*8):
        if seat_id not in seat_ids and seat_id+1 in seat_ids and seat_id-1 in seat_ids:
            ans = seat_id
    return ans

def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 820
    # no test for part 2

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input))