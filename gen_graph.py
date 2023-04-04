"""gen_graph
"""
import sys

from graph import Graph
from drawgraph import DrawGraph


def main():
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <rule>')
        sys.exit(1)
    print(f'gen_graph  v0.0  03Apr2023', file=sys.stderr)

    rule = [0, 0, 0, 0, 1]

    graph_object = Graph(2048)
    edges = graph_object.edges
    colors = graph_object.colors

    # Initialize the starting graph.
    colors[(0, 1)] = 1
"""
    for na, blist in edges.items():
        print(f'from {na}:')
        for nb in blist:
            print(f'  {na}->{nb}')
"""

    dg = DrawGraph(graph_object)

    while True:
        # Create the next generation.
        next_graph_object = Graph(2048)
        next_edges = next_graph_object.edges
        next_colors = next_graph_object.colors
        for pt in graph_object.all_hex_points():
            neighbor_sum = colors[pt] + colors[edges[pt][0]] + colors[edges[pt][1]] + colors[edges[pt][2]]
            next_colors[pt] = rule[neighbor_sum]
        dg = DrawGraph(next_graph_object)
        graph_object = next_graph_object

    print('finis.')


if __name__ == '__main__':
    main()
