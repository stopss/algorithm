import sys

input = sys.stdin.readline

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for _ in range(n + 1)]  # 0번은 취급하지 않기위해 n+1길이만큼 생성 -> 노드연결정보
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)

# 최단거리테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)  # 최단거리테이블

# 모든 간성정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input ).split())
    graph[a].append((b, c))  # a에서부터 b까지 가는 거리가 c다
    # a ----(c)-----> b


def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i


    return index  # 방문하지 않은 노드중 최단 거리값이 짧은 노드의 인덱스 반환


# 다익스트라 알고리즘 - 방문처리여부를 확인 필요X
def dijkstra(start):
    # 시작노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 호출
dijkstra(start)

# 다익스트라 수행후 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(inf)라고 출력
    if distance[i] == INF:
        print('inf')
    else:
        print(distance[i])