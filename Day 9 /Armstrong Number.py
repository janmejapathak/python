n = int(input("Enter number: "))

temp = n
total = 0
digits = len(str(n))

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if n == total:
    print("Armstrong")
else:
    print("Not Armstrong")
