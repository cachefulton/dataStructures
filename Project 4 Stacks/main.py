from stack import Stack

def in2post(expr):
    '''Takes an infix expression as an input and returns an equivalent postfix expression as a string.
    If the expression is not valid, raise a SyntaxError. 
    If the parameter expr is not a string, raise a ValueError.'''
    #make sure the input is a string
    if not isinstance(expr, str): 
        raise ValueError
    #check syntax and make sure the expression works correctly
    eval(expr)

    symbols = {'(':0, '+':1, '-':1, '*':2, '/':2} #set operators and precedence values
    oper = Stack()
    post_expr = []
    for character in expr:
        if character == " ": #get rid of spaces
            pass
        elif character == "(":
            oper.push(character)
        elif character in symbols and (oper.size() == 0 or symbols.get(oper.top()) < symbols.get(character)): #higher precedence operator or empty stack
            oper.push(character)
        elif character in symbols: #if character operator is less or equal in precedence than top of stack
            while oper.size() != 0 and symbols.get(oper.top()) >= symbols.get(character): #see above comment
                post_expr.append(oper.pop())
            oper.push(character)
        elif character == ")":
            while oper.top() != "(":
                post_expr.append(oper.pop())
            oper.pop() #gets rid of the left parenthesis (
        else: #a number
            post_expr.append(character)
    while oper.size() != 0:
        post_expr.append(oper.pop()) #get the last operations out of stack
    return " ".join(post_expr)
        
def eval_postfix(expr):
    '''Takes a postfix string as input and returns a number.
    If the expression is not valid, raise a SyntaxError.
    If the parameter expr is not a string, raise a ValueError.'''
    #make sure the input is a string
    if not isinstance(expr, str): 
        raise ValueError

    symbols = ('+', '-', '*', '/')
    operate = Stack()
    expr = expr.strip().split(' ')
    for item in expr:
        if item not in symbols:
            operate.push(item)
            try:
                int(item)
            except:
                raise SyntaxError #to make sure all terms have spaces bewteen them
        else: #there should be at least two numbers in the stack at all calculations until the answer
            num2 = operate.pop()
            num1 = operate.pop()
            push_ans = str(eval(num1 + item + num2)) #convert to string because it needs to run eval multiple times, which uses strings
            operate.push(push_ans)
    return float(operate.pop()) #returns the last item in the stack and empties stack

def main():
    file = open('data.txt', 'r')

    for line in file:
        expr = line.strip()
        print("\ninfix:", expr)

        post = in2post(expr)
        print("postfix:", post)

        print("answer:", eval_postfix(post))

if __name__ == "__main__":
    main()