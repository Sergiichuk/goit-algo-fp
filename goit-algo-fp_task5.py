import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    return root


def dfs_traversal(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return order


def bfs_traversal(root):
    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return order


def generate_colors(n):
    colors = []
    for i in range(n):
        value = 30 + int((225 / max(1, n - 1)) * i)
        hex_color = f"#{value:02x}{value:02x}ff"
        colors.append(hex_color)
    return colors


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / 2 ** layer, y - 1)
            add_edges(graph, node.left, pos, x - 1 / 2 ** layer, y - 1, layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / 2 ** layer, y - 1)
            add_edges(graph, node.right, pos, x + 1 / 2 ** layer, y - 1, layer + 1)


def draw_tree(root, title):
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(graph, root, pos)

    colors = [graph.nodes[n]['color'] for n in graph.nodes]
    labels = {n: graph.nodes[n]['label'] for n in graph.nodes}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(graph, pos, labels=labels, node_color=colors,
            node_size=2500, arrows=False)
    plt.show()


root = build_tree()

dfs_nodes = dfs_traversal(root)
dfs_colors = generate_colors(len(dfs_nodes))
for node, color in zip(dfs_nodes, dfs_colors):
    node.color = color

draw_tree(root, "DFS")


bfs_nodes = bfs_traversal(root)
bfs_colors = generate_colors(len(bfs_nodes))
for node, color in zip(bfs_nodes, bfs_colors):
    node.color = color

draw_tree(root, "BFS")
