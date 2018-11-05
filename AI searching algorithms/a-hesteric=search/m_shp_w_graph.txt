# This PYTHON MODULE is a SECONDARY MODULE which is
# IMPORTED in ANOTHER MODULE which CONTAINS the main
# PROGRAMMING LOGIC. This MODULE is USED to IMPLEMENT
# a DIRECTED and WEIGHTED GRAPH. The GRAPH is
# IMPLEMENTED as a CLASS which CONTAINS various
# METHODS related to the creation and manipulation
# of the GRAPH.  
import random as mr

#======================================================
# This PYTHON CLASS REPRESENTS a DIRECTED GRAPH consisting
# of VERTICES and DIRECTED EDGES. There is a WEIGHT
# ASSOCIATED with ANY EDGE. This means that the COST of
# MOVING ACROSS an EDGE may be DIFFERENT for VARIOUS EDGES.
# An ADJACENCY LIST is ASSOCIATED with EACH VERTEX of the
# GRAPH. If there is a DIRECTED EDGE going from a VERTEX
# V to some VERTEX W, the VERTEX W is INCLUDED in the
# ADJACENCY LIST of VERTEX V, along with the COST of the
# EDGE. The SET of ADJACENCY LISTS of ALL VERTICES is
# IMPLEMENTED as a PYTHON DICTIONARY with VERTEX NAMES as
# KEYS. A GIVEN NUMBER of EDGES MUST be included in the GRAPH,
# before the GRAPH can be USED for PROCESSING.  
# 
class cl_shp_w_graph:
#======================================================
    
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
        me.v_set = []  # The PYTHON LIST CONTAINING NAMES of
                # VERTICES in the GRAPH.
        me.alists = {} # The PYTHON DICTIONARY CONTAINING ADJACENCY
                # LISTS of the VERTICES
    def is_v_adj(me, v_a, v_b):
        adj_list = me.alists[v_a]
        for v_name, edge_cost in adj_list:
            if v_name == v_b:
                return True
        return False
    def add_edge(me, v_a, v_b, e_cost):
        #================================================
        # There is NO USE for REFLEX EDGES.
        if v_a == v_b:
            return False
        #================================================
        elif v_a in me.alists.keys():
            adj_list = me.alists[v_a]
            if me.is_v_adj(v_a, v_b) == False:
                # check for duplicate vertex
                adj_list.append((v_b, e_cost))
                return True
            else:
                return False
        else:
            adj_list = [(v_b, e_cost)]
            me.alists[v_a] = adj_list
            return True
    def get_vertices(me):
        return me.v_set
    def get_vertex_count(me):
        return len(me.v_set)
    def get_vertex_n(me, n):
        if n in range(len(v_set)):
            return v_set[n]
        else:
            return ' '
    def get_adj_list(me, v_name):
        if v_name in me.alists.keys():
            return me.alists[v_name]
        else:
            return []
    def get_out_degree(me, v_name):
        return len(me.get_adj_list(v_name))
    def get_v_min(me):
        min_v_name = 'a'
        min_degree = me.get_out_degree(min_v_name)
        for n in range(me.vertices_n):
            v_name = chr(ord('a') + n)
            v_degree = me.get_out_degree(v_name)
            if v_degree < min_degree:
                min_v_name = v_name
                min_degree = v_degree
        return min_v_name
    def sort_adj_lists(me):
        for al in me.alists.values():
            #==================================================
            # The TUPLES in each LIST would be SORTED ONLY with
            # respect to VERTEX NAMES because ALL VERTEX NAMES
            # in the TUPLES are DISTINCT .
            al.sort()
            #=======================================
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
                if me.add_edge(v_a, v_b, mr.randint(2, 10)) == True:
                    break
        me.sort_adj_lists()
    def show_graph(me):
        print("***************************")
        for v_name, al in me.alists.items():
            s = v_name + ": "
            ln = len(al)
            for n in range(ln):
                s += str(al[n])
                if n < ln - 1:
                    s += ", "
            print(s)
                
