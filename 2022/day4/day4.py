
def challenge(file_name):
    score_challenge_1 = 0
    score_challenge_2 = 0
    with open(file_name) as f:
        for line in f:
            section_1, section_2 = line.split(",")
            min_section_1, max_section_1 = section_1.split("-")
            min_section_2, max_section_2 = section_2.split("-")

            section_1 = range(int(min_section_1), int(max_section_1) + 1)
            section_2 = range(int(min_section_2), int(max_section_2) + 1)

            if all(value in section_1 for value in section_2) or all(value in section_2 for value in section_1):
                score_challenge_1 += 1

            if any(value in section_1 for value in section_2) or any(value in section_2 for value in section_1):
                score_challenge_2 += 1

    return score_challenge_1, score_challenge_2


if __name__ == "__main__":
    ex_file_name = "ex.txt"
    challenge_file_name = "input.txt"

    example_1, example_2 = challenge(ex_file_name)
    answer_1, answer_2 = challenge(challenge_file_name)

    assert example_1 == 2
    assert example_2 == 4
    print(answer_1)
    print(answer_2)
