def solution(dirs):
    x = 0
    y = 0
    visited = set()
    for char in dirs:
        if char == "U" and y < 5:
            visited.add((x, y, x, y + 1))
            y += 1
            print(visited)
            # (0,0) -> (0,1) / (0,1) -> (0,0)은 같은 요소로 취급해야 한다.
        elif char == "D" and y > -5:
            visited.add((x, y - 1, x, y))
            y -= 1
            print(visited)
        elif char == "L" and x > -5:
            visited.add((x - 1, y, x, y))
            x -= 1
            print(visited)
        elif char == "R" and x < 5:
            visited.add((x, y, x + 1, y))
            x += 1
            print(visited)

    return len(visited)




dirs = "ULURRDLLU"
dirs1 = "ULULDR"
dirs2 = "LULLLLLLU"
dirs3 = "UD"
print(solution(dirs3))