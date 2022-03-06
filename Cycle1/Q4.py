def is_happy(n):
	i = 0
	while n != 1:
		sos = 0
		while n > 0:
			sos += (n % 10) ** 2
			n //= 10
		n = sos
		i += 1
		if i == 100:
			return False
	return True

def find_happy_nums(start, stop):
	happy_nums = []
	for num in range(start, stop):
		if is_happy(num):
			happy_nums.append(num)
	return happy_nums

def n_happy_nums(n):
	happy_nums = []
	i = 0
	num = 0
	while i <= n:
		if is_happy(num):
			happy_nums.append(num)
			i += 1
		num += 1
	return happy_nums

print(is_happy(10))
print(find_happy_nums(10, 100))
print(n_happy_nums(10))
