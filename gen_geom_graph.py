"""gen_geom_graph
"""
from random import random
import sys

from geom_graph import GeomGraph
from draw_geom_graph import DrawGeomGraph


def main():
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <rule>', file=sys.stderr)
        sys.exit(1)

    print(f'gen_graph  v0.0  03Apr2023', file=sys.stderr)

    rule_int = int(sys.argv[1])
    assert rule_int < 32 and rule_int > 0
    rule = [
        1 if (rule_int >> 4) & 1 else 0,
        1 if (rule_int >> 3) & 1 else 0,
        1 if (rule_int >> 2) & 1 else 0,
        1 if (rule_int >> 1) & 1 else 0,
        1 if (rule_int >> 0) & 1 else 0,
    ]
    print(f'rule {rule_int}: {rule}', file=sys.stderr)

    graph_object = GeomGraph(2048)
    edges = graph_object.edges
    colors = graph_object.colors

    # Initialize the starting graph.
    #colors[(0, 1)] = 1
    colors[(2, 2)] = 1
    colors[(2, 0)] = 1
    colors[(1, 1)] = 1
    #for pt in graph_object.all_nodes():
    #    colors[pt] = 1 if random() > 0.5 else 0

    iter_nr = 0
    dg = DrawGeomGraph(graph_object, 8, 8, 4, f'Machine hex4 rule {rule_int} iter {iter_nr}')

    # Run the machine.
    while True:
        # Create the next generation.
        next_graph_object = GeomGraph(1024)
        next_edges = next_graph_object.edges
        next_colors = next_graph_object.colors
        for pt in graph_object.all_nodes():
            neighbor_sum = colors[pt] + colors[edges[pt][0]] + colors[edges[pt][1]] + colors[edges[pt][2]]
            next_colors[pt] = rule[neighbor_sum]
        if (iter_nr % 1) == 0:
            dg = DrawGraph(next_graph_object, 8, 8, 4, f'Machine hex4 rule {rule_int} iter {iter_nr}')
            del dg
        del graph_object
        iter_nr += 1
        graph_object = next_graph_object
        edges = graph_object.edges
        colors = graph_object.colors

    print('finis.')


if __name__ == '__main__':
    main()
