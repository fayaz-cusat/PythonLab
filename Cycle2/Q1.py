N = int(input("Enter N: "))

rows = []

rows.append(["Month", "Number of rabbits"])

prev = 0
now = 0
nxt = 1

for i in range(N):
	now = nxt
	rows.append([str(i + 1), str(now)])
	nxt = prev + now
	prev = now

def show_table(rows):
	max_len_x = 0
	max_len_y = 0
	for x, y in rows:
		if len(x) > max_len_x:
			max_len_x = len(x)
		if len(y) > max_len_y:
			max_len_y = len(y)
	row_size = max_len_x + max_len_y + 8
	
	def print_line():
		print('+' + '-' * (max_len_x + 3) + '+' + '-' * (max_len_y + 3) + '+')

	def print_element(element, size):
		print(f"{element.center(size)}", end='|')
	
	def print_row(row, divider=True):
		print('|', end='')
		print_element(row[0], max_len_x + 3)
		print_element(row[1], max_len_y + 3)
		print()
		if divider:
			print_line()

	print('+' + '-' * (row_size - 1) + '+')
	for row in rows[:-1]:
		print_row(row)
	print_row(rows[-1], divider=False)
	print('+' + '-' * (row_size - 1) + '+')

show_table(rows)
		
	
