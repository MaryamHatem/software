def balanced (sequence):
    stack = []
    for char in sequence:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0
sequence = input("Enter a sequence of brackets: ")

if balanced(sequence):
    print("Yes")
else:
    print("No")