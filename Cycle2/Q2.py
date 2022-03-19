nums = map(int, input("Enter a list of numbers: ").split())
k = int(input("Enter k: "))
n = len(nums)

rm = k % n

shifted = nums[-1 : -rm - 1 : -1] + nums[:-rm]
print("rotated list:", shifted)

tup = (x for x in shifted)
print("tuple of rotated list: ", tup)

lst = list(set(tup))
print("after removing duplicates:", lst)

final = [x**2 - x for x in lst]
print("after applying f(x):", final)

out = sorted(sorted(lst) + sorted(final))
print("final sorted list:", out)
