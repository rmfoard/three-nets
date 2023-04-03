"""gen_graph
"""
import sys

from graph import Graph
from drawgraph import DrawGraph


def main():
    print(f'gen_graph  v0.0  03Apr2023', file=sys.stderr)

    graph_object = Graph(2048)
    edges = graph_object.edges

    for na, blist in edges.items():
        print(f'from {na}:')
        for nb in blist:
            print(f'  {na}->{nb}')

    dg = DrawGraph(graph_object)

    print('finis.')


if __name__ == '__main__':
    main()
