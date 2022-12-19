chars = list(input())
prior = {
    '(':1, 
    '+':2, 
    '-':2, 
    '*':3, 
    '/':3, 
    ')':4}
stack = []
result = []
operator = ['+', '-', '*', '/']

for char in chars:
    if char == '(':
        stack.append(char)
    elif char in operator:
        while stack and prior[stack[-1]] >= prior[char]:
            result.append(stack.pop())
        stack.append(char)
    elif char == ')':
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            result.append(temp)
    else:
        result.append(char)

while stack:
    result.append(stack.pop())

print(''.join(result))