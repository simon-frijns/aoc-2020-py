from typing import Tuple

def get_input(filename) -> list:
    with open(filename) as input:
        return input.read().strip().split("\n")

# 4 variables -> Accumulator, Pointer, Operation, Argument
def run_instruction(acc: int, pointer: int, op: str, arg: int) -> Tuple[int,int]:
    if op == "acc":
        acc += arg
    if op == "nop":
        pass
    if op == "jmp":
        pointer += arg - 1
    pointer += 1
    return acc, pointer

def run_instructions(instructions: list) -> int or None:
    visited_instructions = set()
    acc = 0
    pointer = 0
    while pointer not in visited_instructions and pointer < len(instructions):
        visited_instructions.add(pointer)
        op, arg = instructions[pointer]
        acc, pointer = run_instruction(acc, pointer, op, arg)
    if pointer == len(instructions):
        # ew, can we not print when asserting please?
        print('part 2: ', acc)
    return acc

def create_instructions(input: list) -> list:
    instructions = []
    for instruction in input:
        op, arg = instruction.split(' ')
        instructions.append([op, int(arg)])
    return instructions

def part1(input: list) -> int:
    instructions = create_instructions(input)
    acc = run_instructions(instructions)
    return acc

def part2(input: list) -> int:
    acc = 0
    instructions = create_instructions(input)
    # Is bruteforce best option here?
    for i in range(len(instructions)):
        if instructions[i][0] == 'acc':
            continue
        elif instructions[i][0] == 'jmp':
            possible_fix = 'nop'
        elif instructions[i][0] == 'nop':
            possible_fix = 'jmp'
        # create new set of instructions with possible fix replacing old operation
        # doesn't deep copy so we need to build it up like this
        fixed_instructions = instructions[:i] + [[possible_fix, instructions[i][1]]] + instructions[i+1:]
        acc = run_instructions(fixed_instructions)
    return acc

def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 5
    assert part2(test_input) == 8

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    part2(input)