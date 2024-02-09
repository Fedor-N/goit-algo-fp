import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        self.vertices[from_vertex][to_vertex] = weight

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def visualize(self):
        G = nx.DiGraph()
        for vertex, edges in self.vertices.items():
            for neighbor, weight in edges.items():
                G.add_edge(vertex, neighbor, weight=weight)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=1500,
                node_color="skyblue", font_size=15, arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()


# Приклад використання
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A', 'B', 6)
graph.add_edge('A', 'D', 1)
graph.add_edge('B', 'D', 2)
graph.add_edge('B', 'E', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('D', 'E', 1)
graph.add_edge('E', 'C', 5)

# Візуалізуємо граф
graph.visualize()

# Знаходимо найкоротші шляхи та виводимо їх
shortest_distances = graph.dijkstra('A')
print("Shortest distances:", shortest_distances)
