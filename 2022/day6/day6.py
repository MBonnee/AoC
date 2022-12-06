def challenge(file_name, window_size):
    with open(file_name) as f:
        input = f.readline()

        for i in range(len(input) - window_size + 1):
            window = input[i: i + window_size]

            window = list(window)
            if len(window) == len(list(set(window))):
                return i + window_size


if __name__ == "__main__":
    ex_file_name = "ex.txt"
    challenge_file_name = "input.txt"

    example_1 = challenge(ex_file_name, 4)
    assert example_1 == 7
    answer_1 = challenge(challenge_file_name, 4)
    print(answer_1)

    example_2 = challenge(ex_file_name, 14)
    assert example_2 == 19
    answer_2 = challenge(challenge_file_name, 14)
    print(answer_2)
