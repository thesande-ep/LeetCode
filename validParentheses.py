def isValid(s: str) -> bool:
    stack = []
    mapping = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    for i in s:
        if i in mapping:
            top_element = stack.pop() if stack else "#"
            print(top_element)
            if mapping[i] != top_element:
                return False
        else:
            stack.append(i)
    return not stack

st = "([]"
print(isValid(st))
