 #PART I
 #Name: Massamaesso Narouwa
 #Cohort: CS Cohort 1

d = int
# We want to implent a queue for stock_analyser using a linked list
class Node: # Node definition
    def __init__(self,d):
        self.data = d
        self.next = None
    def getdata(self):
        return self.data




class Queue:  #Queue class definition
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self,item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
            return
            self.rear.next = temp
            self.rear = temp

    def dequeue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None
        return str(temp.data)
    def get_front(self):
        print(self.front)
    def peek(self):
        return self.front




shares = Queue()# Shares object will stock shares  that have been bought.

Price = Queue()  #Price object will store the different prices of each share

shares_for_sale = 0
current_price=0

def gain(): # this class will calculate the capital gain
    if shares_for_sale < shares.front :
        temp = shares.front - shares_for_sale
        capital_gain = shares_for_sale*(current_price - Price.front )
        temp = shares.peek()
        return capital_gain
    elif shares_for_sale == shares.front + shares.next:

        capital_gain = shares.front*(current_price-Price.front ) + shares.next*(current_price - Price.next)
        return capital_gain
    shares.dequeue()
    Price.dequeue()
    shares.next.dequeue()
    Price.next.dequeue()





