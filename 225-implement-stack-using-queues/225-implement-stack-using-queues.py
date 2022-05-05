class MyStack:

    def __init__(self):
        self.qas = []  #qas is used as name for queues as stacks
        
    def push(self, x: int) -> None:
        self.qas = self.qas[::-1] #reverse the reversed queue to make it as usual queue - O(n)
        self.qas.append(x)   # push to the rear of the queue - O(1)
        self.qas = self.qas[::-1] #reverse the queue to facilitate popping and showing top
            
    def pop(self) -> int:
        v = self.qas[0] 
        del self.qas[0]
        return v
        
    def top(self) -> int:
        return self.qas[0]

    def empty(self) -> bool:
        return len(self.qas) == 0