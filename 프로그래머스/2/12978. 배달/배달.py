import sys

def solution(N, road, K):
    result = 0
    graph = list([] for _ in range(N + 1))
    dist = list(float("inf") for _ in range(N + 1))
    dist[1] = 0
    
    for info in road:
        graph[info[0]].append((info[1], info[2]))
        graph[info[1]].append((info[0], info[2]))
        
    for _ in range(N - 1):
        for node in range(1, N + 1):
            for next_node, next_dist in graph[node]:
                if dist[node] != float("inf") and dist[node] + next_dist < dist[next_node]:
                    dist[next_node] = dist[node] + next_dist
                
    hascycle = False
    for next_node, next_dist in graph[node]:
        if dist[node] != float("inf") and dist[N] + next_dist < dist[next_node]:
            has_cycle = True
            break
    if hascycle:
        print("음수 사이크 존재")
    else:
        for i in range(1, N + 1):
            if dist[i] <= K:
                result = result + 1
    
    return result