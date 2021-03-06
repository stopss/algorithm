"""
힙이란?
: 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안되 완전 이진 트리이다.
항상 최대/ 최소 값들이 필요한 연산이 있다면 바로 힙을 쓰면 된다.
힙은 항상 큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있도록 하는 자료구조입니다.
즉, 부모 노드의 값이 자식 노드의 값보다 항상 커야 한다.
가장 큰 값은 모든 자식보다 커야 하기 때문에 가장 위로 가야한다.
따라서 최대의 값들을 빠르게 구할 수 있게 되는 것입니다.


이진 탐색 트리와 다르다. 좌, 우 자식의 위치가 대소관계를 반영하지 않는다.
힙에서 인덱스는 1부터 시작한다. 부모 인덱스 x, left:2x, right:2x+1

* 힙의 규칙
항상 큰 값이 상위 레벨, 작은 값이 하위 ㄹ벨
따라서, 원소를 추가하거나 삭제할 때도 위의 규칙이 지켜져야 한다.

* 최대 힙 - 삽입
원소를 추가할 때는 다음과 같이 하시면 됩니다.
1. 원소를 맨 마지막에 넣습니다.
2. 그리고 부모 노드와 비교한다. 만약 더 크다면 자리를 바굽니다.
3. 부모 노드보다 작거나 가장 위에 도달하지 않을 때까지, 2 과정을 반복한다.
-> 시간복잡도
완전 이진 트리의 최대 높이는 O(log(N))
최대 힙의 원소 추가는 O(log(N))만큼의 시간 복잡도를 가진다.

* 최대 힙 - 추출
1. 루트 노드와 맨 끝에 있는 원소를 교체한다.
2. 맨 뒤에 있는 원소(원래 루트 노드)를 삭제한다.
3. 변경된 노드와 자식 노드들을 비교한다. 두 자식 중 더 큰 자식과 배교해서 자신보다 자식이 더 크다면, 자리를 바꿉니다.
4. 자식 노드 둘 보다 부모 노드가 크거나 가장 바닥에 도달하지 않을 때까지, 3번의 과정을 반복합니다.
5. 2번에서 제거한 원래 루트 노드를 반환합니다.
-> 시간복잡도
완전 이진 트리 최대 높이는 O(log(N))
맥스 힙의 원소 삭제는 O(log(N))만큼의 시간 복잡도를 가진다.

"""