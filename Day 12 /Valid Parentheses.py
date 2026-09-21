s = "({[]})"

stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

valid = True

for ch in s:
    if ch in "([{":
        stack.append(ch)

    else:
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break

        stack.pop()

if stack:
    valid = False

print(valid)
