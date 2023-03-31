"""gen_graph

[ ] next step: build a provisional network structure...
"""
import sys


def hex_points(key_point):
    """Return a list of a hexagon's vertex coordinates, given the coordinates of its 'key point'.
    """
    kpx = key_point[0]
    kpy = key_point[1]
    return [(kpx, kpy),
      (kpx+1, kpy+1),
      (kpx+2, kpy+1),
      (kpx+3, kpy),
      (kpx+2, kpy-1),
      (kpx+1, kpy-1)
    ]


def hex_edges(key_point):
    """Return a list of the 'key_point' hexagon's edges."""
    nodes = hex_points(key_point)
    edges = []
    for i in range(5):
        edges.append([nodes[i], nodes[i+1]])
        edges.append([nodes[i+1], nodes[i]])
    edges.append([nodes[5], nodes[0]])
    edges.append([nodes[0], nodes[5]])
    return edges


def spiral_points():
    """Generate 2D coordinates spiraling out from (0, 1).
    """
    x = 0
    xmin = -1
    xmax = 1

    y = 1
    ymin = 0
    ymax = 2

    yield (x, y)
    while True:
        while x < xmax:
            x += 1
            yield (x, y)
        xmax += 1

        while y > ymin:
            y -= 1
            yield (x, y)
        ymin -= 1

        while x > xmin:
            x -= 1
            yield (x, y)
        xmin -= 1

        while y < ymax:
            y += 1
            yield (x, y)
        ymax += 1


def key_points(max_points):
    """Generate hexagon "key points" spiraling out from (0, 1).

    Generate coordinates for the leftmost vertexes of hexagons that
    tile a plane. Filter a generated "spiral-out" sequence of
    all 2D coordinates.
    """
    nr_points = 0
    pointgen = spiral_points()
    while True:
        if nr_points > max_points:
            break
        else:
            coord = next(pointgen)
            x = coord[0]
            y = coord[1]
            if (x % 2) == 0:
                if (x % 4) == 0:
                    if (y % 2) == 1:
                        nr_points += 1
                        yield coord
                elif (y % 2) == 0:
                    nr_points += 1
                    yield coord


def main():
    def add_edge(na, nb):
        """Add an edge in graph 'g'."""
        if na in g:
            if nb not in g[na]:
                g[na].append(nb)
        else:
            g[na] = [nb]
    # end add_edge

    g = {}
    coordgen = key_points(4)
    while True:
        try:
            coords = next(coordgen)
            for edge in hex_edges(coords):
                assert len(edge) == 2
                add_edge(edge[0], edge[1])
                add_edge(edge[1], edge[0])
        except Exception:
            break

    for na, blist in g.items():
        print(f'from {na}:')
        for nb in blist:
            print(f'  {na}->{nb}')

    print('finis.')


if __name__ == '__main__':
    main()
