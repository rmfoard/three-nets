"""topo_graph
"""

class TopoGraph (object):

    def __init__(self, tier_limit):

        def add_edge(na, nb):
            """Add an edge in 'edges'."""
            if na in self.edges:
                if nb not in self.edges[na]:
                    self.edges[na].append(nb)
            else:
                self.edges[na] = [nb]
        # end add_edge

        # Start with an empty graph.
        self.edges = {}

        # Create mirrored edges, radiating out from q==r==s == 0.
        # Stack the origin to prime the process.
        stack = []
        outstarred = {}
        q = r = s = 0
        stack.append({'q': q, 'r': r, 's': s, 'orientation': 'left'})
        try:
            while True:
                center_node = stack.pop()
                q = center_node['q']
                r = center_node['r']
                s = center_node['s']
                orientation = center_node['orientation']
                
                if (q, r, s)  not in outstarred:
                    outstarred[(q, r, s)] = None
                else:
                    continue

                if orientation == 'left':
                    if abs(q+1) <= tier_limit:
                        add_edge((q, r, s), (q+1, r, s))
                        add_edge((q+1, r, s), (q, r, s))
                        stack.append({'q': q+1, 'r': r, 's': s, 'orientation': 'right'})
                    if abs(s+1) <= tier_limit:
                        add_edge((q, r, s), (q, r, s+1))
                        add_edge((q, r, s+1), (q, r, s))
                        stack.append({'q': q, 'r': r, 's': s+1, 'orientation': 'right'})
                    if abs(r-1) < tier_limit:
                        add_edge((q, r, s), (q, r-1, s))
                        add_edge((q, r-1, s), (q, r, s))
                        stack.append({'q': q, 'r': r-1, 's': s, 'orientation': 'right'})
                else:
                    assert orientation == 'right'
                    if abs(r+1) < tier_limit:
                        add_edge((q, r, s), (q, r+1, s))
                        add_edge((q, r+1, s), (q, r, s))
                        stack.append({'q': q, 'r': r+1, 's': s, 'orientation': 'left'})
                    if abs(q-1) < tier_limit:
                        add_edge((q, r, s), (q-1, r, s))
                        add_edge((q-1, r, s), (q, r, s))
                        stack.append({'q': q-1, 'r': r, 's': s, 'orientation': 'left'})
                    if abs(s-1) < tier_limit:
                        add_edge((q, r, s), (q, r, s-1))
                        add_edge((q, r, s-1), (q, r, s))
                        stack.append({'q': q, 'r': r, 's': s-1, 'orientation': 'left'})
        except IndexError:
            pass

        # Add self-loops to border nodes with only two incident edges and
        # set all node colors to white (0).
        self.colors = {}
        for a_node, b_nodes in self.edges.items():
            self.colors[a_node] = 0  # white
            assert len(b_nodes) == 2 or len(b_nodes) == 3
            if len(b_nodes) == 2:
                b_nodes.append(a_node)


    def all_nodes(self):
        """Generate all node coordinates."""
        for node in self.edges.keys():
            yield node
