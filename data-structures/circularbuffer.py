class bufferqueue:

    def __init__(self,max_size=10):
        self.head = 0
        self.tail = 0
        self.max_size = max_size
        self.lst = [None] * max_size

    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def isFull(self):
        if self.tail + 1 % self.max_size == self.head :
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty() == False :
            print(self.lst[self.head])
        else:
            print("There is nothing to see")

    def add(self):
        if self.isFull() == True:
            print("Buffer has no room")
        else:
            x = input("Enter element to add into buffer")
            self.lst[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
    
    def remove(self):
        if self.isEmpty():
            print("The buffer is empty")
        else:
            self.lst[self.head] = None
            self.head = self.head + 1 % self.max_size