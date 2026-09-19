n = input("Enter number: ")

digits = list(n)

for i in range(len(digits) - 2, -1, -1):
    if digits[i] < digits[i + 1]:
        break
else:
    print("No greater number")
    exit()

for j in range(len(digits) - 1, i, -1):
    if digits[j] > digits[i]:
        digits[i], digits[j] = digits[j], digits[i]
        break

digits[i + 1:] = sorted(digits[i + 1:])

print("Next greater:", "".join(digits))
