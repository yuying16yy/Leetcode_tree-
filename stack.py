# Stack, First in, last out.
# Thinking a cup, 5 pieces of oreo cookies.

# Cup            top
#  - - - - - - - -
# | A ,B, C, D, E  (append from right-hand side, pop also from right-side.)
#  - - - - - - - -

# out: E D C B A

#
# up | E | <-, top = 4
#    | D |
#    | C |
#    | B |
#down| A |
#     - -  <-, top = -1



# Method: push(put), pop, is_empty, is_full, show
# Attributes: size, top

class Stack():
    stack = []
    MAX_SIZE = 0
    top = -1

    def __init__(self, size):
        self.MAX_SIZE = size

    def push(self, value):
        # push a value into stack
        if len(self.stack) < self.MAX_SIZE:
            self.stack.append(value)
            self.top = self.top + 1
            print "Inserted %s into stack" % (value)
        else:
            print "Stack is full"

    def pop(self):
        # pop a value out from a stack
        if self.top >= 0:
            value = self.stack.pop(self.top)
            self.top = self.top - 1
            print "Pop out: %s" % (value)
            return value
        else:
            print "Stack is empty !"

    def is_empty(self):
        # check if stack is empty.global
        return len(self.stack) > 0

    def is_full(self):
        # check if stack is full
        return self.MAX_SIZE - 1 == self.top

    def show(self):
        print "*" + "- - - " * len(self.stack)
        print "*", stack.stack
        print "*" + "- - - " * len(self.stack)


stack = Stack(5)
for i in ["A", "B", "C", "D", "E"]:
    stack.push(i)

stack.show()

for i in range(5):
    stack.pop()

stack.show()