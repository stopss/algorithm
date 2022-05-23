# 인접 행렬

# n,m = map(int, input().split())
# g = [[0]*(n+1) for _ in range(n+1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     g[a][b] = 1
#     g[b][a] = 1
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(g[i][j], end=' ')
#     print()


# 인접 리스트 _ 연결리스트
node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
for _ in range(edge*2):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)


# 인접 리스트 - 딕셔너리
# node, edge = map(int, input().split())
# graph = {}
# for _ in range(edge*2):
#     a, b = map(int, input().split())
#     if a not in graph.keys():
#         graph[a] = set([b])
#     else:
#         graph[a].add(b)
#     if b not in graph.keys():
#         graph[b] = set([a])
#     else:
#         graph[b].add(a)
#
# print(graph)