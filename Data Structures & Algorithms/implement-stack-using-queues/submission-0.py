from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()
        self.queue1 = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        length = len(self.queue) - 1
        while length:
            self.queue.append(self.queue.popleft())
            length = length - 1
        return self.queue.popleft()
        

    def top(self) -> int:
        length = len(self.queue) - 1

        while length:
            self.queue.append(self.queue.popleft())
            length = length - 1
        top_val = self.queue.popleft()
        self.queue.append(top_val)
        return top_val
        

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()