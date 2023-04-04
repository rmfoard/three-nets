"""gen_graph
"""
import sys

from graph import Graph
from drawgraph import DrawGraph


def main():
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <rule>', file=sys.stderr)
        sys.exit(1)

    print(f'gen_graph  v0.0  03Apr2023', file=sys.stderr)

    rule_int = int(sys.argv[1])
    assert rule_int < 32
    rule = [
        1 if (rule_int >> 4) & 1 else 0,
        1 if (rule_int >> 3) & 1 else 0,
        1 if (rule_int >> 2) & 1 else 0,
        1 if (rule_int >> 1) & 1 else 0,
        1 if (rule_int >> 0) & 1 else 0,
    ]
    print(f'rule {rule_int}: {rule}', file=sys.stderr)

    graph_object = Graph(2048)
    edges = graph_object.edges
    colors = graph_object.colors

    # Initialize the starting graph.
    colors[(0, 1)] = 1
    colors[(2, 2)] = 1

    iter_nr = 0
    dg = DrawGraph(graph_object, f'Machine hex4 rule {rule_int} iter {iter_nr}')

    # Run the machine.
    while True:
        # Create the next generation.
        next_graph_object = Graph(2048)
        next_edges = next_graph_object.edges
        next_colors = next_graph_object.colors
        for pt in graph_object.all_hex_points():
            neighbor_sum = colors[pt] + colors[edges[pt][0]] + colors[edges[pt][1]] + colors[edges[pt][2]]
            next_colors[pt] = rule[neighbor_sum]
        dg = DrawGraph(next_graph_object, f'Machine hex4 rule {rule_int} iter {iter_nr}')
        iter_nr += 1
        del graph_object
        graph_object = next_graph_object
        edges = graph_object.edges
        colors = graph_object.colors

    print('finis.')


if __name__ == '__main__':
    main()
