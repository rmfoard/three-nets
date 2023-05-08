"""draw_graph
"""
from graphics import GraphWin, Point, Circle


class DrawGraph (object):

    def __init__(self, graph, x_expansion, y_expansion, node_radius, title):
        self.graph = graph
        self.edges = graph.edges
        self.colors = graph.colors
        self.x_expansion = x_expansion
        self.y_expansion = y_expansion
        self.node_radius = node_radius

        gw = GraphWin(title, 800, 800)
        gw.setCoords(-400, -400, 400, 400)

        for pt in graph.all_nodes():
            x = pt[0] * self.x_expansion
            y = pt[1] * self.y_expansion
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
