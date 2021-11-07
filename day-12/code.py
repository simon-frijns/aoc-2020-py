from typing import Tuple

def get_input(filename) -> list:
    with open(filename) as input:
        return input.read().strip().split("\n")

def process_action(order: str, xy: list, direction: int) -> Tuple[list, int]:
    action = order[0]
    value = int(order[1:])
    directions = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    if action == 'F':
        order = directions[direction] + str(value)
        process_action(order, xy, direction)
    match action:
        case 'N':
            xy[1] += value
        case 'S':
            xy[1] -= value
        case 'W':
            xy[0] -= value
        case 'E':
            xy[0] += value
        case 'L':
            direction = (direction - value) % 360
        case 'R':
            direction = (direction + value) % 360            
    return xy, direction

def process_action_p2(order: str, ship_xy: list, waypoint_xy: list) -> Tuple[list, list]:
    action = order[0]
    value = int(order[1:])
    if action in 'LR':
        turns = value // 90 
        if action == 'L':
            turns = 4 - turns
        for _ in range(turns): # clockwise turn 
            waypoint_xy = [waypoint_xy[1],-waypoint_xy[0]] 
    match action:
        case 'N':
            waypoint_xy[1] += value
        case 'S':
            waypoint_xy[1] -= value
        case 'W':
            waypoint_xy[0] -= value
        case 'E':
            waypoint_xy[0] += value
        case 'F':
            ship_xy[0] += waypoint_xy[0] * value
            ship_xy[1] += waypoint_xy[1] * value
    return ship_xy, waypoint_xy

def part1(input: list) -> int:
    ans = 0
    direction = 90 # starting facing east
    xy = [0, 0]
    for order in input:
        xy, direction = process_action(order, xy, direction)
    ans = sum(map(abs, xy))
    return ans   

def part2(input: list) -> int:
    ans = 0
    ship_xy = [0, 0]
    waypoint_xy = [10, 1] 
    for order in input:           
        ship_xy, waypoint_xy = process_action_p2(order, ship_xy, waypoint_xy)
    ans = sum(map(abs, ship_xy))
    return ans

def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 25
    assert part2(test_input) == 286

if __name__ == "__main__":  
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input))