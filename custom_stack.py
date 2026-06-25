def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    stack = []
    matching = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        # If it's an opening bracket, push it onto the stack
        if char in '([{':
            stack.append(char)

        # If it's a closing bracket, check for a match
        elif char in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if top != matching[char]:
                return False

    # If stack is empty, all brackets were matched correctly
    return len(stack) == 0