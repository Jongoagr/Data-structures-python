stack = []
top = ""

def isempty():
    if stack == []:
        return True
    else:
        return False

def push(x,stack): #Input Values
    stack.append(x)
    top = str(x)
    print(stack)

def pop(stack): #remove latest value
    if isempty == True:
        print("stack is empty")
    else:
        stack.pop()
    print(stack)

def peek(stack): #see the latest value
    if isempty == True:
        print("stack is empty")
    else:
        print(top)

# Examples of the above functions in action

push(1,stack)
push(2,stack)
pop(stack)
peek(stack)