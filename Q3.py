name = input("Enter name: ")
code = input("Enter code: ")
bp = float(input("Enter basic pay: "))	

def get_parts(bp):
	if bp < 10000:
		da = 0.05
		hra = 0.025
		ma = 500
		pt = 20
		pf = 0.08
		it = 0
	elif bp < 30000:
		da = 0.075
		hra = 0.05
		ma = 2500
		pt = 60
		pf = 0.08
		it = 0
	elif bp < 50000:
		da = 0.11
		hra = 0.075
		ma = 5000
		pt = 60
		pf = 0.11
		it = 0.11
	else:
		da = 0.25
		hra = 0.11
		ma = 7000
		pt = 80
		pf = 0.12
		it = 0.2

	gross = bp + bp * da + bp * hra + ma
	deduction = pt + bp * pf + bp * it
	net_salary = gross - deduction
	return gross, deduction, net_salary

gross, deduction, net_salary = get_parts(bp)
print("\nPaySlip")
print("***********************")
print("Employee name:", name)
print("Employee code:", code)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net_salary)
