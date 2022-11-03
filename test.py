from collections import deque

def solution(rc, operations):
    answer = []
    for line in rc:
        print(line)
    mid_pillar, left_pillar, right_pillar = deque(), deque(), deque()
    for r in rc:
        mid_pillar.append(deque(r[1:-1]))
        left_pillar.append(r[0])
        right_pillar.append(r[-1])
    print(mid_pillar)
    print(left_pillar)
    print(right_pillar)
    for operation in operations:
        if operation == 'Rotate':
            if mid_pillar[0]:
                right_pillar.appendleft(mid_pillar[0].pop())
                mid_pillar[-1].append(right_pillar.pop())
            else:
                right_pillar.appendleft(left_pillar.popleft())

            if mid_pillar[-1]:
                left_pillar.append(mid_pillar[-1].popleft())
                mid_pillar[0].appendleft(left_pillar.popleft())
            else:
                left_pillar.append(right_pillar.pop())
        else:
            print("---------------------ShiftRow---------------")
            print(mid_pillar)
            mid_pillar.rotate(1)
            print(mid_pillar)
            print(left_pillar)
            left_pillar.rotate(1)
            print(left_pillar)
            right_pillar.rotate(1)

    for left, mid, right in zip(left_pillar, mid_pillar, right_pillar):
        answer.append([left] + list(mid) + [right])

    return answer

solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"])