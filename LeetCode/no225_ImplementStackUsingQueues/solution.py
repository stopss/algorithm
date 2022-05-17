# Implement Stack using Queues
import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        # 마지막 원소(x)를 제외한 나머지를 꺼내서 다시 차례대로 push 해준다.
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


if __name__ == '__main__':
    a = MyStack()
    a.push(1)
    a.push(2)
    a.push(3)
    print("top: ", a.top())
    print("pop: ", a.pop())
    print("empty: ", a.empty())