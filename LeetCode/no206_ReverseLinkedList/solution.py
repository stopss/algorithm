class Node:
    # 노드 정의
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def print_all(self):
        cur = self.head

        while cur:
            if cur.next != None:
                print(cur.value, '-> ', end='')
                cur = cur.next
            else:
                print(cur.value)
                cur = cur.next

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, val):
        # 첫 번째 노드가 없는 경우
        if not self.head:
            self.head = Node(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(val, None)


if __name__ == '__main__':
    li = LinkedList()
    li.append('a')
    li.append('b')
    li.append('c')
    li.append('d')
    li.print_all()
    li.reverseList(0)