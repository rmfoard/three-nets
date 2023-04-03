"""draw_graph
"""


class DrawGraph (object):

    def __init__(self, graph):
        self.graph = graph
        self.edges = graph.edges
        self.colors = graph.colors
        self.x_expansion = 8
        self.y_expansion = 8
        self.node_diameter = 4

        gw = GraphWin("Graph Title", 800, 800)
        gw.setCoords(-400, -400, 400, 400)
