n = int(input("Number of people: "))
k = int(input("Elimination step: "))

people = list(range(1, n + 1))
index = 0

while len(people) > 1:
    index = (index + k - 1) % len(people)
    people.pop(index)

print("Survivor:", people[0])
