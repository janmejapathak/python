s = input("Enter string: ")
count = 0

for ch in s:
    if ch.isalpha() and ch not in "aeiouAEIOU":
        count += 1

print("Consonants:", count)
