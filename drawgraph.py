"""draw_graph
"""
from graphics import GraphWin, Point, Circle


class DrawGraph (object):

    def __init__(self, graph, title):
        self.graph = graph
        self.edges = graph.edges
        self.colors = graph.colors
        self.x_expansion = 4
        self.y_expansion = 4
        self.node_radius = 2

        gw = GraphWin(title, 800, 800)
        gw.setCoords(-400, -400, 400, 400)

        for pt in graph.all_hex_points():
            x = pt[0] * self.x_expansion
            y = pt[1] * self.y_expansion
            c = Circle(Point(x, y), self.node_radius)
            if graph.colors[pt] == 1:
                c.setFill('green')
            c.draw(gw)

        #gw.getMouse()
        gw.close()
        del gw


def main():
    pass


if __name__ == '__main__':
    main()
