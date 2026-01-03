''' Task 2

Using breadth-first search write an algorithm that can
determine the shortest path from each vertex to every other vertex.
This is called the all-pairs shortest path problem.'''

from collections import deque

graph = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B'],
         'D': ['B']
         }

def bfs_distances(graph, start):

    distances = {start: 0} 
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in distances:
                queue.append(neighbor)
                distances[neighbor] = distances[current] + 1
    return distances

def all_pairs_shortest_path(graph):
    result = {}
    all_pairs = graph.keys()
    
    for vertex in all_pairs:
        distances_from_vertex = bfs_distances(graph, vertex)
        result[vertex] = distances_from_vertex
    
    return result


        
# Тест
result = all_pairs_shortest_path(graph)

# результат
for start in result:
    print(f'\nВід {start}:')
    for end, distance in result[start].items():
        print(f' до {end}: {distance}')
   