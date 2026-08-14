"""
Write a function that checks if the brackets in a string are valid.
A string is valid if every opening bracket has a matching closing bracket
in the correct order.
Allowed brackets: (), [], {}
"""
def bracket_validator(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False

    return not stack


if __name__ == "__main__":
    test_string = "{[hello()] world}"
    print(f"Is the string '{test_string}' balanced? {bracket_validator(test_string)}")
