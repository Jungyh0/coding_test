import heapq

def solution(n, s, a, b, fares):
    graph = list([] for _ in range(n + 1))

    for info in fares:
        graph[info[0]].append((info[2], info[1]))
        graph[info[1]].append((info[2], info[0]))

    def dai(s):
        dist = [float("inf") for _ in range(n + 1)]

        dist[s] = 0
        q = [(dist[s], s)]

        while q:
            cur_dist, cur_v = heapq.heappop(q)

            if cur_dist > dist[cur_v]:
                continue

            for next_dist, next_v in graph[cur_v]:
                new_dist = cur_dist + next_dist

                if new_dist < dist[next_v]:
                    dist[next_v] = new_dist
                    heapq.heappush(q, (dist[next_v], next_v))

        return dist


    dist_s = dai(s)
    dist_a = dai(a)
    dist_b = dai(b)

    ans = float("inf")

    for num in range(1, n + 1):
        coast = dist_s[num] + dist_a[num] + dist_b[num]
        ans = min(ans, coast)

    return ans