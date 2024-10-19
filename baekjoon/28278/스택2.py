
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def len(self):
        return self.size
        
    def pop(self):
        data = None
        if self.isEmpty():
            return data
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
        return data
    
    def top(self):
        data = None
        if self.isEmpty():
            return data
        else:
            data = self.head.data
        return data

from sys import stdin as si
  
if __name__ == "__main__":
    a = Stack()
    T = int(si.readline().rstrip())
    
    while T >= 1:
        T -= 1
        
        tmp = list(map(int,si.readline().split()))
        
        if tmp[0] == 1:
            a.push(tmp[1])
        elif tmp[0] == 2:
            data = a.pop()
            if data == None:
                print(-1)
            else:
                print(data)
        elif tmp[0] == 3:
            print(a.len())
        elif tmp[0] == 4:
            if a.isEmpty():
                print(1)
            else:
                print(0)
        elif tmp[0] == 5:
            data = a.top()
            if data == None:
                print(-1)
            else:
                print(data)
