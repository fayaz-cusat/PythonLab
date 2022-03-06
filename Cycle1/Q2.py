from math import sqrt

def get_sides():
	sides = [float(input("Enter side %d: " % (i + 1))) for i in range(3)]
	return sides

def calc_area(sides):
	a, b, c = sides
	s = sum(sides) / 2
	area = sqrt(s * (s - a) * (s - b) * (s - c))
	return area

print("Triangle 1")
t1 = get_sides()
print("\nTriangle 2")
t2 = get_sides()
ar1, ar2 = calc_area(t1), calc_area(t2)
print(ar1, ar2)
total = ar1 + ar2

print("Total area enclosed =", total)
print("%% contribution of first triangle = %f%%" % ((ar1 / total) * 100))
print("%% contribution of second triangle = %f%%" % ((ar2 / total) * 100))
