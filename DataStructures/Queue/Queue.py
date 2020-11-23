import threading
import time

from collections import deque

q = deque()
q.appendleft(4)
q.appendleft(6)
q.appendleft(10)
q.pop()
print(q)

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


q = Queue()
def place_orders(list):
#     q = Queue()
    for elm in list:
        print("Placing order for:", elm)#added
        q.enqueue(elm)
        time.sleep(0.5) #added
    # return q

# def serve_order(queue):
def serve_orders():
    time.sleep(1) #add
    while True:
        order = q.dequeue()
        print("Now serving: ", order)
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target=place_orders, args=(orders,))
t2 = threading.Thread(target=serve_orders)

t1.start()
t2.start()