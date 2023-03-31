"""gen_graph

[ ] next step: build a provisional network structure...
"""
import sys


def hex_points(left_point):
    """Return a list of a hexagon's vertex coordinates, given the coordinates of its 'left point'.
    """
    lpx = left_point[0]
    lpy = left_point[1]
    return [(lpx, lpy),
      (lpx+1, lpy+1),
      (lpx+2, lpy+1),
      (lpx+3, lpy),
      (lpx+2, lpy-1),
      (lpx+1, lpy-1)
    ]


def hex_edges(left_point):
    """Return a list of the 'left_point' hexagon's edges."""
    nodes = hex_points(left_point)
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


def left_points(max_points):
    """Generate hexagon "left points" spiraling out from (0, 1).

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
    coordgen = left_points(40)
    while True:
        try:
            coords = next(coordgen)
            print(f'{coords}')
            for point in hex_points(coords):
                print(f'    {point[0]}, {point[1]}')
            for edge in hex_edges(coords):
                print(f'  {edge[0]}--{edge[1]}')
        except Exception:
            sys.exit(0)


if __name__ == '__main__':
    main()
