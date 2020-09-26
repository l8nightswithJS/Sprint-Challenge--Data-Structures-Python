class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
    
        #class that implements full buffer
        

    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.data.append(item)
            print()
            
    def get(self):
        return self.data