# 배열을 이용한 풀이

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    # enQueue(): rear 포인터 이용
    def enQuene(self, value:int) -> bool:
        # rear 포인터 위치가 None이 아니면 공간이 남아있기 때문에 값을 넣어준다.
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            # rear 포인터 위치 한 칸 이동
            self.rear = (self.rear + 1) % self.maxlen
            return True

        # rear 포인터 위치가 None이면 공간이 꽉 찬 상태이거나 비정상적인 경우이므로 False를 리턴한다.
        else:
            return False

    # deQueue(): front 포인터 이용
    def deQueue(self):
        # front 포인터 위치가 None이면
        if self.q[self.front] is None:
            return False
        else:
            # front 포인터 위치가 None을 넣어 삭제를 한다.
            self.q[self.front] = None
            # front 포인터 위치 한 칸 이동
            self.front = (self.front + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def isEmpty(self):
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self):
        return self.front == self.rear and self.q[self.front] is not None


if __name__ == "__main__":
    a = MyCircularQueue(3)
    print(a.enQuene(1))
    print(a.enQuene(2))
    print(a.enQuene(3))
    print(a.enQuene(4))
    print(a.Rear())
    print(a.isFull())
    print(a.deQueue())
    print(a.enQuene(4))
    print(a.Rear())
    print(a.Front())


