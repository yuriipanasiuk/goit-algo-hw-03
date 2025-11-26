def is_valid_parentheses(s):
    """symmetry check"""
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    opening = set(mapping.values())

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"


if __name__ == "__main__":
    test_cases = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]

    for case in test_cases:
        print(f"{case}: {is_valid_parentheses(case)}")
