class node():

    def __init__(self,value):
        self.value = value
        self.next_node = None

class linkedList():
        
    def __init__(self):
        self.head = None
        
    def addNode(self,value,pos):
        new_node = node(value)
        if self.head == None:
            self.head = new_node
        if pos == 0:
            self.head = new_node

        cur = self.head
        n = 0
        while n <= pos:
            if n == pos - 1 :
                new_node = node(value)
                new_node.next_node = cur.next_node
                cur.next_node = new_node
            n += 1

# NOT DONE YET RAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH