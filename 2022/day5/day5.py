def build_stacks(stack_file):
    stacks = []
    stack_file = stack_file.split("\n")
    stck_list = list(reversed(stack_file))
    length = len(stck_list[0]) - 1
    for i in range(1, length, 4):
        stack = []
        for line in stck_list:
            stack.append(line[i])
        stack = [x for x in stack if x != " "]
        stacks.append(stack)

    return stacks


def perform_moveset(moves_file, stacks, challenge):
    moves_file = moves_file.split("\n")
    for line in moves_file:
        input = line.split(" ")
        quantity = int(input[1])
        origin_stack_index = int(input[3]) - 1
        destination_stack_index = int(input[5]) - 1

        crate_move = []
        for _ in range(quantity):
            value = stacks[origin_stack_index].pop()
            crate_move.append(value)

        if challenge == 2:
            crate_move = list(reversed(crate_move))

        stacks[destination_stack_index].extend(crate_move)

    return stacks


def challenge(file_name, challenge_num):
    with open(file_name) as f:
        stack_file, moves_file = f.read().split("\n\n")
        stacks = build_stacks(stack_file)
        stacks = perform_moveset(moves_file, stacks, challenge_num)

    answer = ""
    for stack in stacks:
        answer += stack.pop()

    return answer


if __name__ == "__main__":
    ex_file_name = "ex.txt"
    challenge_file_name = "input.txt"

    example_1 = challenge(ex_file_name, 1)
    assert example_1 == "CMZ"
    answer_1 = challenge(challenge_file_name, 1)
    print(answer_1)

    example_2 = challenge(ex_file_name, 2)
    assert example_2 == "MCD"
    answer_2 = challenge(challenge_file_name, 2)
    print(answer_2)
