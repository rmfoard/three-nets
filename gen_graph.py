"""gen_graph
"""
from graph import Graph


def main():
    graph_object = Graph(10)
    g = graph_object.g

    for na, blist in g.items():
        print(f'from {na}:')
        for nb in blist:
            print(f'  {na}->{nb}')

    print('finis.')


if __name__ == '__main__':
    main()
