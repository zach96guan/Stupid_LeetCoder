# dictionary + doubly-linked list

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def get(self, key: int) -> int:
        if key in self.dic:
            tmp = self.dic[key]
            self.remove(tmp)
            self.add(tmp)
            return tmp.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        tmp = Node(key, value)
        self.add(tmp)
        self.dic[key] = tmp
        
        if len(self.dic) > self.capacity:
            tmp = self.head.next
            self.remove(tmp)
            del self.dic[tmp.key]
    
    
    def add(self, node):
        tmp = self.tail.prev
        tmp.next = node
        self.tail.prev = node
        node.prev = tmp
        node.next = self.tail
        
    
    def remove(self, node):
        tmp1 = node.prev
        tmp2 = node.next
        tmp1.next = tmp2
        tmp2.prev = tmp1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)