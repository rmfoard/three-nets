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

    rule = [0, 1, 1, 0, 1]

    graph_object = Graph(512)
    edges = graph_object.edges
    colors = graph_object.colors

    # Initialize the starting graph.
    colors[(0, 1)] = 1

    dg = DrawGraph(graph_object)

    # Run the machine.
    while True:
        # Create the next generation.
        next_graph_object = Graph(512)
        next_edges = next_graph_object.edges
        next_colors = next_graph_object.colors
        for pt in graph_object.all_hex_points():
            neighbor_sum = colors[pt] + colors[edges[pt][0]] + colors[edges[pt][1]] + colors[edges[pt][2]]
            next_colors[pt] = rule[neighbor_sum]
        dg = DrawGraph(next_graph_object)
        del graph_object
        graph_object = next_graph_object
        edges = graph_object.edges
        colors = graph_object.colors

    print('finis.')


if __name__ == '__main__':
    main()
