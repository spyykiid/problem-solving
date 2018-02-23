'''Checking Paranthesis'''

def checkParanthesis(str_):
    stack = []
    
    for s in str_:
        
        if s in '{[(':
            stack.append(s)
        
        elif s in ']' and stack[-1] == '[' and len(stack) > 0:
            stack.pop()
            
        elif s in '}' and stack[-1] == '{' and len(stack) > 0:
            stack.pop()
            
        elif s in ')' and stack[-1] == '(' and len(stack) > 0:
            stack.pop()
            
        else:
            
        
    if len(stack) > 0:
        return False
    else:
        return True


assert checkParanthesis('[(abc)]') == True
#assert checkParanthesis('[abc)]') == False
#assert checkParanthesis('[(abc]') == False
