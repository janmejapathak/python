n = input("Enter number: ")

valid = True

for i in range(len(n)):
    if n.count(str(i)) != int(n[i]):
        valid = False
        break

if valid:
    print("Self-descriptive")
else:
    print("Not self-descriptive")
