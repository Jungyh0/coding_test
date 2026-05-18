import heapq

def solution(n, roads, sources, destination):
    graph = list([] for _ in range(n + 1))
    result = []

    for info in roads:
        graph[info[0]].append(info[1])
        graph[info[1]].append(info[0])

    def dai(n, graph, start, sources):
        result = []
        dist = list(float("inf") for _ in range(n + 1))
        dist[start] = 0
        q = []

        heapq.heappush(q, (dist[start], start))

        while q:
            cur_dist, cur_node = heapq.heappop(q)
            if cur_dist > dist[cur_node]:
                continue

            for next_node in graph[cur_node]:
                new_dist = 1 + cur_dist

                if new_dist < dist[next_node]:
                    dist[next_node] = new_dist
                    heapq.heappush(q, (dist[next_node], next_node))

        for soldier in sources:
            min_val = dist[soldier]

            if min_val == float("inf"):
                result.append(-1)
            else:
                result.append(min_val)
        return result



    result = dai(n, graph, destination, sources)

    return result
