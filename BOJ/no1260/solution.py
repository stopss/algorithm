import sys

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N + 1)]

for _ in range(M):
  m1, m2 = map(int, input().split())
  # 노드 연결 하기
  graph[m1][m2] = graph[m2][m1] = 1

print(graph)



