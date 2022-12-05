ALPHA_NUM = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def challenge_1(file_name):
    total_priority = 0

    with open(file_name) as f:
        for line in f:
            items = list(line)[:-1]
            comp_size = int(len(items) / 2)
            compartment_1 = set(items[:comp_size])
            compartment_2 = set(items[-comp_size:])

            error = compartment_1.intersection(compartment_2)
            error = list(error)[0]

            priority = ALPHA_NUM.index(error) + 1
            total_priority += priority

    return total_priority


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def challenge_2(file_name):
    total_priority = 0
    with open(file_name) as f:
        lines = f.readlines()
        line_groups = chunks(lines, 3)

        for line_group in line_groups:
            elf1 = set(list(line_group[0])[:-1])
            elf2 = set(list(line_group[1])[:-1])
            elf3 = set(list(line_group[2])[:-1])

            common = elf1.intersection(elf2.intersection(elf3))
            common = list(common)[0]
            priority = ALPHA_NUM.index(common) + 1
            total_priority += priority

    return total_priority


if __name__ == "__main__":
    ex_file_name = "ex.txt"
    challenge_file_name = "input.txt"

    example_1 = challenge_1(ex_file_name)
    assert example_1 == 157
    answer_1 = challenge_1(challenge_file_name)
    print(answer_1)

    example_2 = challenge_2(ex_file_name)
    assert example_2 == 70
    answer_2 = challenge_2(challenge_file_name)
    print(answer_2)
