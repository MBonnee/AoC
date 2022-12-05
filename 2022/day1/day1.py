def challenge(file_name, top_n):
	with open(file_name) as f:
		calories = 0
		calorie_list = []
		for line in f:
			if line == "\n":
				calorie_list.append(calories)
				calories = 0
			else:
				calories += int(line)

		calorie_list.sort(reverse=True)
		calorie_list = calorie_list[:top_n]

		return sum(calorie_list)


if __name__ == "__main__":
	ex_file_name = 'ex.txt'
	challenge_file_name = 'input.txt'

	assert challenge(ex_file_name, 1) == 24000
	print(challenge(challenge_file_name, 1))

	assert challenge(ex_file_name, 3) == 45000
	print(challenge(challenge_file_name, 3))
