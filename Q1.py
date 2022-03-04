num = int(input("Enter a four digit number: "))
d1 = num % 10
num //= 10
d2 = num % 10
num //= 10
d3 = num % 10
num //= 10
d4 = num % 10
sum_ = d1 + d2 + d3 + d4
rev = d1 * 1000 + d2 * 100 + d3 * 10 + d4
odd_prod = d2 * d4
even_prod = d1 * d3
diff = odd_prod - even_prod

print(sum_)
print(rev)
print(diff)


