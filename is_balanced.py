def is_balanced(expression):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack:
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

assert is_balanced("(){{[]}}()(){{}}") == True
assert is_balanced("(23(2-3);") == False  
assert is_balanced("(11}") == False