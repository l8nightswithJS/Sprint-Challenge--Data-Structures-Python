class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0
        #class that implements full buffer
        
    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)           
        else:
            self.data[self.current] = item
            if self.current < len(self.data) -1:
                self.current += 1
            else:
                self.current = 0
                
            
            
    def get(self):
        return self.data