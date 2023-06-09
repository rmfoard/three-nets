"""gen_topo_graph
"""
from random import random
import sys

from topo_graph import TopoGraph
from draw_topo_graph import DrawTopoGraph


def main():
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <rule>', file=sys.stderr)
        sys.exit(1)

    print(f'gen_topo_graph  v0.1  03Apr2023', file=sys.stderr)

    rule_int = int(sys.argv[1])
    assert rule_int < 32 and rule_int >= 0
    rule = [
        1 if (rule_int >> 4) & 1 else 0,
        1 if (rule_int >> 3) & 1 else 0,
        1 if (rule_int >> 2) & 1 else 0,
        1 if (rule_int >> 1) & 1 else 0,
        1 if (rule_int >> 0) & 1 else 0,
    ]
    print(f'rule {rule_int}: {rule}', file=sys.stderr)

    tier_limit = 30  # size parameter
    graph_object = TopoGraph(tier_limit)
    edges = graph_object.edges
    colors = graph_object.colors

    # Initialize the starting graph.
    colors[(1, 0, 0)] = 1
    colors[(0, -1, 0)] = 1
    colors[(0, 0, 1)] = 1
    #for pt in graph_object.all_nodes():
    #    colors[pt] = 1 if random() > 0.5 else 0

    iter_nr = 0
    dg = DrawTopoGraph(graph_object, 7.0, 2, f'Machine hex4 rule {rule_int} iter {iter_nr}')

    # Run the machine.
    while True:
        # Create the next generation.
        next_graph_object = TopoGraph(tier_limit)
        next_edges = next_graph_object.edges
        next_colors = next_graph_object.colors
        for pt in graph_object.all_nodes():
            neighbor_sum = colors[pt] + colors[edges[pt][0]] + colors[edges[pt][1]] + colors[edges[pt][2]]
            next_colors[pt] = rule[neighbor_sum]
        if (iter_nr % 1) == 0:
            dg = DrawTopoGraph(next_graph_object, 6.0, 3, f'Machine hex4 rule {rule_int} iter {iter_nr}')
            del dg
        del graph_object
        iter_nr += 1
        graph_object = next_graph_object
        edges = graph_object.edges
        colors = graph_object.colors

    print('finis.')


if __name__ == '__main__':
    main()
