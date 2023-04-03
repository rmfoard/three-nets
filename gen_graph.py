"""gen_graph
"""
from graph import Graph


def main():
    graph_object = Graph(10)
    edges = graph_object.edges

    for na, blist in edges.items():
        print(f'from {na}:')
        for nb in blist:
            print(f'  {na}->{nb}')

    print('finis.')


if __name__ == '__main__':
    main()
