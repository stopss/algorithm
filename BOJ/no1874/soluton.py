n = int(input())

stack = []
result = []
count = 1
message = True

for i in range(n):
    num = int(input())

    # 스택 push
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1

    # 스택 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    # 불가능한 경우
    else:
        message = False
        break

# 정답 출력
if message:
    for i in result:
        print(i)
else:
    print('NO')