def check_brackets(text):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in text:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if len(stack) == 0:
                return False
            last_char = stack.pop()
            if pairs[last_char] != char:
                return False
    
    return len(stack) == 0
