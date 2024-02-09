import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def visualize_dfs(tree_root):
    dfs_tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    dfs_tree = add_edges(dfs_tree, tree_root, pos)

    dfs_stack = [tree_root]
    visited = set()

    plt.figure(figsize=(8, 5))

    while dfs_stack:
        node = dfs_stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            # Зміна кольору вузла
            dfs_tree.nodes[node.id]['color'] = f'#FF{(len(visited)*35):02X}00'
            nx.draw(dfs_tree, pos=pos, labels={node.id: node.val}, node_color=[
                    dfs_tree.nodes[n]['color'] for n in dfs_tree.nodes()], with_labels=True, arrows=False, node_size=2500)
            plt.pause(1)  # Пауза для відображення кроку обходу
            if node.right:
                dfs_stack.append(node.right)
            if node.left:
                dfs_stack.append(node.left)
            plt.clf()

    plt.show()


def visualize_bfs(tree_root):
    bfs_tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    bfs_tree = add_edges(bfs_tree, tree_root, pos)

    bfs_queue = [tree_root]
    visited = set()

    plt.figure(figsize=(8, 5))

    while bfs_queue:
        node = bfs_queue.pop(0)
        if node.id not in visited:
            visited.add(node.id)
            # Зміна кольору вузла
            bfs_tree.nodes[node.id]['color'] = f'#FF{(len(visited)*35):02X}00'
            nx.draw(bfs_tree, pos=pos, labels={node.id: node.val}, node_color=[
                    bfs_tree.nodes[n]['color'] for n in bfs_tree.nodes()], with_labels=True, arrows=False, node_size=2500)
            plt.pause(1)  # Пауза для відображення кроку обходу
            if node.left:
                bfs_queue.append(node.left)
            if node.right:
                bfs_queue.append(node.right)
            plt.clf()

    plt.show()


# Приклад побудови бінарного дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходу у глибину (DFS)
visualize_dfs(root)

# Відображення обходу у ширину (BFS)
visualize_bfs(root)
