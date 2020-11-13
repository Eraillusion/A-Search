import heapq
import collections
# Principle of the program: Utilize BFS to find the shortest path, search the all the neighbors in next level , and import "heapq" to sort the weight.


def ShortestPathBFS(edges, source, dest):
    # Create a weighted DAG - {node:[(cost,neighbour), ...]}
    graph = collections.defaultdict(list)
    for length, former, latter in edges:
        graph[length].append((latter,former))
    # Create a priority queue and hash set to store visited nodes
    queue = [(0, source, [])]
    visited_node = set()
    heapq.heapify(queue)
    # Traverse graph with BFS
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        # Visit the node if it was not visited before
        if node not in visited_node:
            # Try to visit the new node.
            visited_node.add(node)
            # Path need to add this one.
            path = path + [node]
            # Search the dest
            if node == dest:
                # Return the weight value and path with vertex.
                return (path, cost)
            # If node is not the final nodel, then visit neighbours.
            for count, neighbour in graph[node]:
                if neighbour not in visited_node:
                    heapq.heappush(queue, (cost+count, neighbour, path))
    return float("inf")

if __name__ == "__main__":
    # Load the information of the graph.
    edges = [
        ("A", "B", 4),
        ("B", "C", 2),
        ("B", "D", 9),
        ("C", "D", 3),
        ("D", "E", 10),
        ("D", "F", 2),
        ("F", "G", 2)
    ]

    print("The shortest path from A to G with BFS algorithm is ")
    print (ShortestPathBFS(edges, "A", "G"))