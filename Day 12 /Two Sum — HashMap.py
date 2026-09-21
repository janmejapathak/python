nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(nums)):
    need = target - nums[i]

    if need in seen:
        print(seen[need], i)
        break

    seen[nums[i]] = i
