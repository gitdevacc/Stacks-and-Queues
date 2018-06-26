
def isBalanced(input_string):
    if input_string=='':
        return True
    else:
        dict={'[':0, ']':0, '(':0, ')':0, '{':0, '}':0}
        for c in input_string:
            if c not in dict:
                return False
            else:
                dict[c]=dict[c]+1
        if dict['[']==dict[']']:
            if dict['(']==dict[')']:
                if dict['{']==dict['}']:
                    return True
            return False
print(isBalanced(input('Enter the sequence:')))