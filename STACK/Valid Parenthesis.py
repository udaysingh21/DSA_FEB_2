def validparenthesis(string):
    opening='{[('
    closing='}])'

    stack=[]
    match={'{':'}','(':')','[':']'}

    for val in string:
        if val in opening:
            stack.append(val)
        else: # we got closing bracket
            if len(stack) == 0: return False # w/o opening bracket we got closing bracket
            top=stack[-1] # top = '['
            if match[top]==val:  # match['[']=  ']'==']'
                stack.pop()
            else:
                return False

    if len(stack)==0:
        return True
    else:
        return False

string='}{{[[(())]]}}()'
print(validparenthesis(string))