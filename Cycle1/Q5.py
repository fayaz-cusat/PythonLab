string = input("Enter string: ")

def get_substrings_k(string, k):
	res = []
	n = len(string)
	for i in range(n):
		if (i + k) <= n:
			res.append(string[i : i + k])
	return res

def get_all_substrings(string):
	res = []
	for k in range(1, len(string)):
		res.extend(get_substrings_k(string, k))
	return res
	
def get_kn_dist(string, k, n):
	res = []
	for substring in get_substrings_k(string, k):
		elems = []
		for char in substring:
			if char not in elems:
				elems.append(char)
		if len(elems) == n:
			res.append(substring)
	return res

def get_max_n_dist(string, n):
	res = ""
	for k in range(len(string) + 1):
		strings = get_kn_dist(string, k, n)
		for s in strings:
			if len(s) > len(res):
				res = s
	return res

print(get_max_n_dist(string, 4))
