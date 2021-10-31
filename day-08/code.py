from typing import Tuple

def get_input(filename) -> list:
    with open(filename) as input:
        return input.read().strip().split("\n")

# 4 variables -> Accumulator, Pointer, Operation, Argument
def read_instruction(acc: int, pointer: int, op: str, arg: int) -> Tuple[int,int]:
    #print(acc, pointer, op, arg)
    if op == "acc":
        acc += arg
    if op == "nop":
        pass
    if op == "jmp":
        pointer += arg - 1
    pointer += 1
    return acc, pointer

def part1(input: list) -> int:
    acc = 0
    pointer = 0
    instructions = []
    for instruction in input:
        op, arg = instruction.split(' ')
        instructions.append((op, int(arg)))
    visited_instructions = set()
    while pointer not in visited_instructions:
        visited_instructions.add(pointer)
        op, arg = instructions[pointer]
        acc, pointer = read_instruction(acc, pointer, op, arg)
    return acc

def part2(input: list) -> int:
    ans = 0
    return ans 

def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 5
    #assert part2(test_input) == 32

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    #print(part2(input))