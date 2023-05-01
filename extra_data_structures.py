class Stack:
    def __init__(self):
        self.stack = []
        self.bottom = self.stack[0]
        self.top = self.stack[len(self.stack)]
        self.top_index = len(self.stack)

    def _update(self):
        self.top = self.stack[len(self.stack)]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def Push(self, data) -> None:
        self.stack.append(data)

    def Pop(self):
        return self.stack.pop(self.top_index)

