# This PYTHON MODULE is a SECONDARY MODULE which is
# IMPORTED in ANOTHER MODULE which CONTAINS the main
# PROGRAMMING LOGIC. This MODULE is USED to IMPLEMENT
# a DIRECTED and UNWEIGHTED GRAPH. The GRAPH is
# IMPLEMENTED as a CLASS which CONTAINS various
# METHODS related to the creation and manipulation
# of the GRAPH. The BREADTH FIRST SEARCH(BFS)
# algorithm is APPLIED to the GREAPH for FINDING the
# SHORTEST PATH between TWO GIVEN VERTICES. 
import random as mr

#======================================================
# This PYTHON CLASS REPRESENTS a DIRECTED GRAPH consisting
# of VERTICES and DIRECTED EDGES. There is NO WEIGHT
# ASSOCIATED with ANY EDGE. This means that the COST of
# MOVING ACROSS an EDGE is the SAME for ALL EDGES. An
# ADJACENCY LIST is ASSOCIATED with EACH VERTEX of the
# GRAPH. If there is a DIRECTED EDGE going from a VERTEX
# V to some VERTEX W, the VERTEX W is INCLUDED in the
# ADJACENCY LIST of VERTEX V. The SET of ADJACENCY LISTS
# of ALL VERTICES is IMPLEMENTED as a PYTHON DICTIONARY
# with VERTEX NAMES as KEYS. A GIVEN NUMBER of EDGES MUST
# be included in the GRAPH, before the GRAPH can be USED
# for PROCESSING.  
# With MINOR MODIFICATIONS, this CLASS can be ADAPTED
# to IMPLEMENT a an UNDIRECTED UNWEIGHTED GRAPH.
class cl_shp_graph:
    v_set = []  # The PYTHON LIST CONTAINING NAMES of
                # VERTICES in the GRAPH.
    alists = {} # The PYTHON DICTIONARY CONTAINING ADJACENCY
                # LISTS of the VERTICES
    def __init__(me, v_n, e_n):
        #================================================
        # The total NUMBER of VERTICES to be INCLUDED in
        # the GRAPH.
        me.vertices_n = v_n
        #------------------------------------------------
        # The total NUMBER of EDGES to be INCLUDED in the
        # GRAPH.
        me.edges_n = e_n
        #================================================
    def add_edge(me, v_a, v_b):
        if v_a == v_b:
            # There is no need to have REFLEX EDGES.
            return False
        if v_a in me.alists.keys():
            al = me.alists[v_a]
            if (v_b in al) == False:
                # check for duplicate vertex
                al.append(v_b)
                return True
            else:
                return False
        else:
            al = [v_b]
            me.alists[v_a] = al
            return True
        if n < len(me.v_set):
            return me.v_set[n]
        else:
            return ' '
    def get_vertices(me):
        return me.v_set
    def get_vertex_count(me):
        return len(me.v_set)
    def get_vertex_n(me, n):
        if n in range(len(v_set)):
            return v_set[n]
        else:
            return ' '
    def get_degree_n(me, v_name):
        vl = me.alists[v_name]
        return len(vl)
        
    def get_adj_list(me, v_name):
        if v_name in me.alists.keys():
            return me.alists[v_name]
        else:
            return []
    def get_v_min(me):
        min_name = 'a'
        min_degree = me.get_degree_n(min_name)
        for n in range(me.vertices_n):
            v_name = chr(ord('a') + n)
            v_degree = me.get_degree_n(v_name)
            if v_degree < min_degree:
                min_name = v_name
                min_degree = v_degree
        return min_name
    def sort_adj_lists(me):
        for al in me.alists.values():
            al.sort()
    def build_shp_graph(me):
        # The GRAPH is CONSTRUCTED in a PURELY RANDOM MANNER.
        mr.seed()
        
        for n in range(me.vertices_n):
            v_name = chr(ord('a') + n)
            me.v_set.append(v_name)
            me.alists[v_name] = []
        for m in range(me.edges_n):
            v_a = me.get_v_min()
            for tries in range(5):
                v_b = chr(ord('a') + mr.randint(0, me.vertices_n - 1))
                if me.add_edge(v_a, v_b) == True:
                    break
        me.sort_adj_lists()
    def show_graph(me):
        print("***************************")
        for v, al in me.alists.items():
            s = v + ": "
            ln = len(al)
            for n in range(ln):
                s += al[n]
                if n < ln - 1:
                    s += ", "
            print(s)
                
