"""
File: boggle.py
Name: Ashton Yang
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	grid = input_rows()
	# grid is a list of lists: eg.[['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	start = time.time()
	words = read_dictionary()
	final_answers = []
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			used_coordinates = []
			current_ans = []
			find_ans(words, grid, used_coordinates, current_ans, final_answers, x, y)
	n = count(final_answers)
	print('There are ', n, 'words in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def input_rows():
	rows = []
	while True:
		row_1 = input('1 row of letters: ')
		if legal_input(row_1):
			rows.append(row_1.split())
		else:
			print('Illegal input')
			break
		row_2 = input('2 row of letters: ')
		if legal_input(row_2):
			rows.append(row_2.split())
		else:
			print('Illegal input')
			break
		row_3 = input('3 row of letters: ')
		if legal_input(row_3):
			rows.append(row_3.split())
		else:
			print('Illegal input')
			break
		row_4 = input('4 row of letters: ')
		if legal_input(row_4):
			rows.append(row_4.split())
		else:
			print('Illegal input')
			break
		break
	return rows


def legal_input(row):
	lst = row.split()
	if len(lst) != 4:
		return False
	else:
		for ele in lst:
			if len(ele) != 1:
				return False
			else:
				return True


def find_ans(words, grid, used_coordinates, current_ans, final_answers, x, y):
	used_coordinates.append((x, y))
	current_ans.append(grid[y][x])
	if not has_prefix(current_ans, words):
		pass
	else:
		if len(current_ans) >= 4:
			current_ans_str = convert_2_string(current_ans)
			if current_ans_str in words and current_ans_str not in final_answers:
				print(f'Found \"{current_ans_str}\"')
				final_answers.append(current_ans_str)
		for dy in [-1, 0, 1]:
			for dx in [-1, 0, 1]:
				new_x = x + dx
				new_y = y + dy
				if (new_x, new_y) not in used_coordinates:
					if 0 <= new_x < len(grid) and 0 <= new_y < len(grid):
						find_ans(words, grid, used_coordinates, current_ans, final_answers, new_x, new_y)
						used_coordinates.pop()
						current_ans.pop()


def convert_2_string(current_ans):
	ans = ''
	for i in current_ans:
		ans += i
	return ans


def read_dictionary():
	words = []
	with open(FILE, 'r') as f:
		for line in f:
			words.append(line.strip())
	return words


def has_prefix(current_ans, words):
	sub_s = ''
	for alphabet in current_ans:
		sub_s += alphabet
	for word in words:
		if word.startswith(sub_s):
			return True


def count(final_ans):
	n = 0
	for ans in final_ans:
		n += 1
	return n


if __name__ == '__main__':
	main()
