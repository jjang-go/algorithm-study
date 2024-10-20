class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.F = None
        self.R = None
        self.len = 0
        
    def push(self,data):
        new_node = ListNode(data)
        if self.F == None:
            self.F = self.R = new_node
        else:
            self.R.next = new_node
            self.R = new_node
        self.len += 1
        
    def size(self):
        return self.len
    
    def isEmpty(self):
        if self.len == 0:
            return True
        else:
            return False
    
    def pop(self):
        data = None
        if self.F == None:
            return data
        else:
            data = self.F.data
            self.F = self.F.next
            if self.F == None:
                self.R = None
            self.len -= 1
            return data
        
    def front(self):
        data = None
        if self.F != None:
            data = self.F.data
        return data
    
    def back(self):
        data = None
        if self.R != None:
            data = self.R.data
        return data
    
from sys import stdin as si

T = int(si.readline().rstrip())

a = Queue()

while T >= 1:
    T -= 1
    
    tmp = list(si.readline().split())
    
    if tmp[0] == "push":
        a.push(int(tmp[1]))
    elif tmp[0] == "pop":
        data = a.pop()
        if data == None:
            print(-1)
        else:
            print(data)
    elif tmp[0] == "size":
        print(a.size())
    elif tmp[0] == "empty":
        if a.isEmpty():
            print(1)
        else:
            print(0)
    elif tmp[0] == "front":
        data = a.front()
        if data == None:
            print(-1)
        else:
            print(data)
    elif tmp[0] == "back":
        data = a.back()
        if data == None:
            print(-1)
        else:
            print(data)