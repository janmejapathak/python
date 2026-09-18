arr = [2, 2, 1, 1, 1, 2, 2]

for x in arr:
    if arr.count(x) > len(arr) // 2:
        print("Majority:", x)
        break
