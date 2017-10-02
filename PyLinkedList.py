#Q1:
# Queue:
# First in First out
# DB: list: [5,4,3,2,1]
#         front       end

# put, pop, search, is_empty(is_full)

class Queue():
    """ Implementation of a queue"""
    q = []

    # Database
    def __init__(self):
        # Constructor
        print "A new Queue"

    def put(self, value):
        # Put value into queue
        self.q.append(value)
        print "Appended a new value: %s" % (value)

    def pop(self):
        pop_value = self.q.pop(0)
        print "The pop value is: %s" % (pop_value)
        return pop_value

    def search(self, value):
        # Search by value, return index if found,
        # otherwise return -1
        if value in self.q:
            print "Found it, %s's index is %s" % (value, self.q.index(value))
            return self.q.index(value)
        else:
            print "Not found"
            return -1

    def is_empty(self):
        # Check if db is empty
        if len(self.q) == 0:
            print "Queue is empty"
        else:
            print "Queue is not empty"

    def show(self):
        print "Your queue is: \n", self.q


print "Test our Queue"
queue = Queue()

# Innitialize a queue
for i in range(5, 0, -1):
    queue.put(i)
queue.show()
# Test is_empty
queue.is_empty()

# Test search
queue.search(3)

# Test pop
first = queue.pop()
queue.show()


# Define a node(value, next)

class Node():
    def __init__(self, value):
        # class variables: data and next
        self.data = value
        self.next = None


# link list: multiple nodes conntected consecutively and continuously
class LinkList():
    # Linklist: head
    def __init__(self, head):
        self.head = head

    def show(self):
        result = []
        cur = head.next
        while (cur != None):
            result.append(cur.data)
            cur = cur.next
        print result

    def search(self, target):
        cur = head.next
        index = 0
        while (cur != None):
            if cur.data == target:
                print "Find it ! ! ! "
                return index
            else:
                cur = cur.next
                index = index + 1
        print "No %s" % (target)
        return -1

    def add(self, node):
        # add node to the tail
        cur = head.next
        while (cur != None and cur.next != None):
            # Why not while(cur != None) ?
            # in order to reach the last valid node
            cur = cur.next
        cur.next = node
        return head

    def remove(self, value):
        # remove the node that node.data = value
        pre = self.head
        cur = self.head.next
        while (cur != None and cur.next != None and cur.data != value):
            cur = cur.next
            pre = pre.next
        # cur  = Node(3)
        pre.next = cur.next
        cur.next = None
        return self.head


# initialize nodes
head = Node(-999)  # can be Node(none)
node1 = Node(1)  # data = 1, next = None
node2 = Node(2)
node3 = Node(4)
node4 = Node(5)

# connect them into a link list
head.next = node1
node1.next = node2  # for node1: data = 1, next = node2
node2.next = node3
node3.next = node4

#                 index = 0
# Link List: head -> (1) -> (2) -> (4) -> (5) -> None
#                           pre    cur

# un-ordered link list
ll = LinkList(head)

ll.add(Node(6))
ll.add(Node(3))
ll.show()

ll.remove(5)
ll.show()

print ll.search(3)
print ll.search(5)








