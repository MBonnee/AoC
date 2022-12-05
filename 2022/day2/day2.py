SCORE_CARD = {
	"A - X": [3+1, 3+0],
	"A - Y": [6+2, 1+3],
	"A - Z": [0+3, 2+6],
	"B - X": [0+1, 1+0],
	"B - Y": [3+2, 2+3],
	"B - Z": [6+3, 3+6],
	"C - X": [6+1, 2+0],
	"C - Y": [0+2, 3+3],
	"C - Z": [3+3, 1+6]
}


def challenge(file_name, score_card_version):
	with open(file_name) as f:
		total_score = 0
		for line in f:
			opponent = line[0]
			me = line[2]
			match_pattern = f"{opponent} - {me}"
			score = SCORE_CARD[match_pattern][score_card_version]
			total_score += score

		return total_score


if __name__ == "__main__":
	ex_file_name = "ex.txt"
	challenge_file_name = "input.txt"

	example_1 = challenge(ex_file_name, 0)
	assert example_1 == 15
	answer_1 = challenge(challenge_file_name, 0)
	print(answer_1)

	example_2 = challenge(ex_file_name, 1)
	assert example_2 == 12
	answer_2 = challenge(challenge_file_name, 1)
	print(answer_2)
