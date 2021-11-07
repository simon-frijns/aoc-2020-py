import math # for LCM

def get_input(filename) -> list:
    with open(filename) as input:
        return input.read().strip().split("\n")

def part1(input: list) -> int:
    ans = 0
    earliest_time = int(input[0])
    busses = input[1].split(",")
    filtered_busses = list(map(int, [bus for bus in busses if bus != 'x']))
    mods = {bus: (bus - (earliest_time % bus)) for bus in filtered_busses}
    key = min(mods, key=mods.get)
    value = min(mods.values())
    ans = key * value
    return ans   

def part2(input: list) -> int:
    ans = 0
    busses = input[1].split(",")
    bus_intervals = [(int(bus), interval) for interval, bus in enumerate(busses) if bus != 'x']
    timestamp = 0
    step = bus_intervals[0][0]
    for bus, interval in bus_intervals[1:]:
        no_match_found = True
        while no_match_found:
            if (timestamp + interval) % bus == 0:
                no_match_found = False
                break # need to break to prevent adding another step
            timestamp += step
        step = math.lcm(step, bus) # step should be whatever is least common multiple between all numbers until now and current bus
    ans = timestamp
    return ans

def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 295
    assert part2(test_input) == 1068781

if __name__ == "__main__":  
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input))