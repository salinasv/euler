import math

# Transform an integer number to a list of digits.
def numberToList(number):
	numlist = []

	while number > 0:
		numlist.append(number % 10)
		number = int(number / 10)

	numlist.reverse()
	return numlist

# Transform a list of digits into a integer number
def listToNumber(list):
	num = 0

	for i in list:
		num = num*10 + i

	return num

# Calculates the next palindrome with less value than max
# if max is palindrome, returns the same value. AKA: NOP
def palindrome(max):

	number = numberToList(max)

	# Special case, a one digit value is already a palindrome.
	if len(number) == 1:
		return max

	first_part = number.copy()

	middle = math.floor(len(number)/2)

	# Remove the last part of the number
	for i in range(middle):
		first_part.pop()

	# go for the second part
	i = len(first_part)
	second_part = []

	offset = 0

	# if we repeat this number, the palindrome would be greater
	# than the max number we want
	while offset < len(number):

		# This number is palindrome... ¬¬ 
		if offset == len(first_part):
			return listToNumber(number)

		# If the center value is equal on both sides, go to the digit before
		if first_part[i - offset - 1] == number[middle + offset]:
			offset = offset + 1
			continue

		# If the lenght is odd
		if len(number) % 2:
			# If the last number before middle is bigger than the one next to it.
			if first_part[i - offset - 1] > number[middle + offset]:
				# go to the next value below
				first_part[i - 1] = first_part[i - 1] - 1
		# the lenght is even
		else:
			if first_part[i-offset -1 ] > number[middle + offset]:
				first_part[i - 1] = first_part[i - 1] - 1

		# fix signed values
		if (first_part[i - offset - 1]) == -1:
			first_part[i - offset - 1] = 9
		break

	second_part = first_part.copy()

	if len(number) % 2:
		second_part.pop()

	second_part.reverse()

	first_part.extend(second_part)


	return listToNumber(first_part)
