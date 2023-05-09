"""draw_geom_graph
"""
from graphics import GraphWin, Point, Circle
import math


class DrawTopoGraph (object):

    def __init__(self, graph, scale, node_radius, title):
        self.graph = graph
        self.edges = graph.edges
        self.colors = graph.colors
        self.scale = scale
        self.node_radius = node_radius

        gw = GraphWin(title, 800, 800)
        gw.setCoords(-400, -400, 400, 400)

        for pt in graph.all_nodes():
            q = float(pt[0])
            r = float(pt[1])
            s = float(pt[2])

            root3_2 = math.sqrt(3) / 2.0

            x = scale * (r + q/2.0 + s/2.0)
            y = scale * (q * root3_2 - s * root3_2)

            c = Circle(Point(x, y), self.node_radius)
            if graph.colors[pt] == 1:
                c.setFill('green')
            c.draw(gw)

        gw.getMouse()
        gw.close()
        del gw


def main():
    pass


if __name__ == '__main__':
    main()
