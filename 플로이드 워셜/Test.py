INF = int(1e9) #INFINITY 10억

n = int(input())
m = int(input())

#2차원 리스트(그래프 표현) 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 각 간선에 거리 저장
for i in range(m):
    #A에서 B로 가는 비용 = C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 수행
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        # 끊겨 있는 곳은 INF
        if graph[a][b]==INF:
            print("INFINITY", end=' ')
        # 도달할 수 있는 거리 출력
        else:
            print(graph[a][b], end=' ')
    print()

-----------입력-----------
# 4
# 7
# 1 2 4 
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
-----------출력-----------
# 0 4 8 6 
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0

