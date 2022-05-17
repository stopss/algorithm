class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면
        if not self.output:
            #input에서 pop해서 output으로 push한다.
            while self.input:
                self.output.append(self.input.pop())
        # output의 가장 마지막으로 push된 값을 리턴
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


if __name__ == "__main__":
    a = MyQueue()
    a.push(1)
    a.push(2)

    print("peek: ", a.peek())
    print("pop: ", a.pop())
    print("empty: ", a.empty())
