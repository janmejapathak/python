arr = [7, 1, 5, 3, 6, 4]

max_difference = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        difference = arr[j] - arr[i]

        if difference > max_difference:
            max_difference = difference

print(max_difference)
