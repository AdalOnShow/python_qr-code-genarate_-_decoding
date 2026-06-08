class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)

    def push(self, val):
        self.s.insert(0, val)

    def peak(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        return self.s[0]

    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        val = self.s[0]
        del self.s[0]
        return val


stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk.pop())
print(stk.peak())
print(stk.pop())
print(stk.length())
