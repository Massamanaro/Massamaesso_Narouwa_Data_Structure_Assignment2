
class CardsStacks:
    #  Implementation two stacks in a list

        def __init__(self, N):  # constructor
            self.size = N
            self.arr = [None] * N
            self.top1 = -1
            self.top2 = self.size

            # Method to push an element a to stack1

        def push1(self, a):

            # There is at least one empty space for new element
            if self.top1 < self.top2 - 1:
                self.top1 = self.top1 + 1
                self.arr[self.top1] = a

            else:
                print("Stack Overflow ")
                exit(1)

                # Method to push an element b to stack2

        def push2(self, b):

            # There is at least one empty space for new element
            if self.top1 < self.top2 - 1:
                self.top2 = self.top2 - 1
                self.arr[self.top2] = b

            else:
                print("Stack Overflow ")
                exit(1)

                # Method to pop an element from first stack

        def pop1(self):
            if self.top1 >= 0:
                x = self.arr[self.top1]
                self.top1 = self.top1 - 1
                return x
            else:
                print("Stack Underflow ")
                exit(1)

                # Method to pop an element from second stack

        def pop2(self):
            if self.top2 < self.size:
                x = self.arr[self.top2]
                self.top2 = self.top2 + 1
                return x
            else:
                print("Stack Underflow ")
                exit(1)



