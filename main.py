def longest_path(graph: list) -> int:
    n = len(graph)

    def topological_sort(graph):
        in_degree = [0] * n
        for u in range(n):
            for v, w in graph[u]:
                in_degree[v] += 1

        zero_in_degree = [i for i in range(n) if in_degree[i] == 0]

        topo_order = []
        while zero_in_degree:
            u = zero_in_degree.pop()
            topo_order.append(u)
            for v, w in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    zero_in_degree.append(v)

        return topo_order

    def calculate_longest_path(graph, topo_order):
        dist = [-float('inf')] * n
        for node in topo_order:
            if dist[node] == -float('inf'):
                dist[node] = 0
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
        return max(dist)

    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)


graph3 = [
    [(1, 10)],
    [(2, 10)],
    [(3, 10)],
    []
]
graph4 = [
    [(1, 1), (2, 1)],
    [(3, 1)],
    [(3, 1)],
    []
]
graph2 = [
    [(1, 2), (2, 1)],
    [(3, 1)],
    [(3, 5)],
    []
]
graph1 = [
    [(1, 3), (2, 2)],
    [(3, 4)],
    [(3, 1)],
    []
]
print(longest_path(graph1))
print(longest_path(graph2))
print(longest_path(graph3))
print(longest_path(graph4))
# i have cross varified multiple times but the ouput is coming 2 instead of 3 for implemtation purpose
# i have also give screenshots for rough work
# it has to be 2(graph 4)