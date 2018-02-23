def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    lpara = '({['
    for s_ in s:
        len_s = len(stack)
        if s_ in lpara:
            stack.append(s_)
        elif s_ == '}' and len(stack) > 0 and stack.pop() == '{':
            continue
        elif s_ == ')' and len(stack) > 0 and stack.pop() == '(':
            continue
        elif s_ == ']' and len(stack) > 0 and stack.pop() == '[':
            continue
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False


print(isValid('()'))