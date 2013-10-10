import palindrome

# Not that brute method
def euler4(mul_len):
	#mul_len = 2
	mul = mul_len*[9]
	mul = palindrome.listToNumber(mul)
	piv = mul
	mul_num = mul ** 2
	all_pals = []


	while (mul > 0):
		mul_num = mul * piv
		pal = palindrome.palindrome(mul_num)

		# The pal is multiple of piv and mul
		if pal == mul_num:
			all_pals.append(pal)

		piv = piv - 1

		if len(palindrome.numberToList(piv)) < mul_len:
				mul = mul - 1
				piv = mul

		if len(palindrome.numberToList(mul)) < mul_len:
			break

	all_pals.sort()
	return all_pals[-1]

# Brute force method
def euler4_brute(mul_len):
	mul = mul_len*[9]
	mul = palindrome.listToNumber(mul)
	pal = []

	for i in reversed(range(1,mul)):
		if len(palindrome.numberToList(i)) < mul_len:
			break
		for j in reversed(range(1, mul)):
			if len(palindrome.numberToList(j)) < mul_len:
				break

			val = i * j
			temp = palindrome.palindrome(val)

			if (temp == val):
				pal.append(temp)

	pal.sort()
	return pal[-1]


# problem execution
mul_len = 3
pal = euler4(mul_len)
#pal = euler4_brute(mul_len)
print("The biggest palidnrome multiple of two number of lenght ", mul_len,
		"Being: ", pal)

