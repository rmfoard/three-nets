"""graph
"""

class Graph (object):

    def __init__(self, nr_key_points):

        def add_edge(na, nb):
            """Add an edge in 'edges'."""
            if na in self.edges:
                if nb not in self.edges[na]:
                    self.edges[na].append(nb)
            else:
                self.edges[na] = [nb]
        # end add_edge

        # Create mirrored edges, hexagon-wise.
        self.nr_key_points = nr_key_points
        self.edges = {}
        for coords in self.key_points(nr_key_points):
            for edge in self.hex_edges(coords):
                assert len(edge) == 2
                add_edge(edge[0], edge[1])
                add_edge(edge[1], edge[0])

        # Add self-loops to border nodes with only two incident edges and
        # set all node colors to white (0).
        self.colors = {}
        for a_node, b_nodes in self.edges.items():
            self.colors[a_node] = 0  # white
            assert len(b_nodes) == 2 or len(b_nodes) == 3
            if len(b_nodes) == 2:
                b_nodes.append(a_node)


    def all_points(self):
        checklist = {}
        for kp in self.key_points(self.nr_key_points):
            for pt in self.hex_points(kp):
                if pt not in checklist:
                    checklist[kp] = True
                    yield pt


    def hex_points(self, key_point):
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


    def hex_edges(self, key_point):
        """Return a list of the 'key_point' hexagon's edges."""
        nodes = self.hex_points(key_point)
        edges = []
        for i in range(6):
            edges.append([nodes[i], nodes[(i+1) % 6]])
            edges.append([nodes[(i+1) % 6], nodes[i]])
        return edges


    def spiral_points(self):
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


    def key_points(self, max_points):
        """Generate hexagon "key points" spiraling out from (0, 1).

        Generate coordinates for the leftmost vertexes of hexagons that
        tile a plane. Filter a generated "spiral-out" sequence of
        all 2D coordinates.
        """
        nr_points = 0
        pointgen = self.spiral_points()
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
