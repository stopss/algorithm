# 이진 트리

# 이진 트리의 구현 - 노드
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    # 이진 트리의 크기 - 재귀함수 이용
    def size(self):
        # 왼쪽 서브트리
        left_sub = self.left.size() if self.left else 0
        # 오른쪽 서브트리
        right_sub = self.right.size() if self.right else 0

        return left_sub + right_sub + 1

    # depth
    def depth(self):
        left_sub = self.left.depth() if self.left else 0
        right_sub = self.right.depth() if self.right else 0

        return max(left_sub, right_sub) + 1



# 이진 트리의 구현 - 트리(tree)
class BinaryTree:
    def __init__(self, r):
        self. root = r

    # 크기 구하기
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    # depth
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0