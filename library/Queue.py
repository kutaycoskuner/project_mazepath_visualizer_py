#
# ==== Libraries

# ==== Classes
class Queue:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.insert(0, item)

    def addFront(self,item):
        self.data.append(item)

    def pop(self):
        self.data.pop(-1)        

    def peek(self):
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0


# ==== Functions

# ==== Variables

# ==== Main