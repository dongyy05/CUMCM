import networkx as nx
import matplotlib.pyplot as plt

# 定义图的边和权重
s = [9, 9, 1, 1, 3, 3, 3, 2, 2, 5, 5, 7, 7, 8]  # 起始节点
t = [1, 2, 2, 3, 4, 6, 7, 4, 5, 4, 7, 6, 8, 6]  # 终止节点
w = [4, 8, 3, 8, 2, 7, 4, 1, 6, 6, 2, 14, 10, 9]  # 边的权重

# 创建一个带权图 G
G = nx.Graph()

# 向图中添加边
for i in range(len(s)):
    G.add_edge(s[i], t[i], weight=w[i])

# 绘制图 G 并显示边的权重
pos = nx.spring_layout(G)  # 选择布局方式
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# 使用 shortest_path 计算从节点 9 到节点 8 的最短路径及其距离
P = nx.shortest_path(G, source=9, target=8, weight='weight')
d = nx.shortest_path_length(G, source=9, target=8, weight='weight')
print("Shortest path from 9 to 8:", P)
print("Distance:", d)

# 在图 G 中高亮显示最短路径
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
nx.draw_networkx_edges(G, pos, edgelist=list(zip(P, P[1:])), edge_color='r', width=2)
plt.show()

# 计算图 G 中所有节点之间的最短路径距离
D = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))
print("Distances matrix:", D)

# 输出节点 1 和 2 之间的最短路径
print("Distance between 1 and 2:", D[1][2])

# 输出节点 9 和 4 之间的最短路径
print("Distance between 9 and 4:", D[9][4])

# 寻找图 G 中距离节点 2 距离不超过 10 的所有节点
nearest_nodes = nx.single_source_dijkstra_path_length(G, 2, cutoff=10, weight='weight')
print("Nodes within distance 10 from node 2:", nearest_nodes)
