q = []

def isempty(q):
    if q == []:
        return True
    else:
        return False

def add(q,x):
    q.append(x)
    print(q)

def remove(q):
    if isempty(q) == True:
        print("The queue is empty")
    else:
        q.pop(0)
        print(q)

def peek(q):
    if isempty(q) == True:
        print("The queue is empty")
    else:
        print(q[0])

def length(q):
    l = len(q)
    print("Length is:", l)

add(q,1)
add(q,3)
add(q,2)
remove(q)
peek(q)
length(q)