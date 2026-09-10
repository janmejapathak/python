s = input("Enter string: ")
count = 0

for ch in s:
    if ch.isdigit():
        count += 1

print("Digits:", count)
