# THIS PYTHON APPLICATION APPLIES the DEPTH FIRST SEARCH(DFS)
# ALGORITHM in AI for GENERATING the LIST of VERTICES that 
# are REACHABLE from a GIVEN VERTEX in a GRAPH which is
# DIRECTED and UNWEIGHTED. The ALGORITHM NEVER FAILS beacause
# the LIST of REACHABLE VERTICES can ALWAYS be FOUND. A PRUNING
# LOGIC is used in this implementation for EXLUDING UNNECESSARY
# subsequent GRAPH EDGES from the search. 
# The GRAPH is IMPLEMENTED in a SEPARATE PYTHON MODULE which
# is IMPORTED in this MODULE.

import random as mr
from m_reach_graph import cl_reach_graph

class node:
    # A PYTHON LIST is included as a member of EACH INSTANCE of
    # this class. The list CONTAINS the NAMES of CANDIDATE VERTICES
    # which may be USED for EXPANSION, from this NODE, during the
    # DFS SEARCH. The VERTEX NAMES are a SUBSET of those vertices
    # to which there are EDGES going from the vertex associated with
    # THIS INSTANCE of the class. Names of PRUNED VERTICES are
    # excluded from the list.
    #
    def __init__(me, vertex, parent, vl):
        me.parent = parent
        me.vertex = vertex
        me.edge_vertices = vl
        if parent == None:
            me.set_root()
        else:
            me.is_root = False
            me.path = me.parent.path + [me.vertex]
    def set_root(me):
        me.is_root = True
        me.parent = None
        me.path = [me.vertex]
    def get_path_str(me):
        ps = "PATH: "
        for v in me.path:
            ps += "--" + v
        return ps
    def get_next_edge_vertex(me):
        if len(me.edge_vertices) == 0:
            return None
        else:
            ev = me.edge_vertices[0]
            del me.edge_vertices[0]
        return ev
    def show_moving_back(me):
        if me.parent == None:
            return
        else:
            print("Moving back to NODE(" + me.parent.vertex + ")")
    
    
    
class dfs:
    def __init__(me):
        me.v_n = 15
        me.e_n = 16
        me.graph = cl_reach_graph(me.v_n, me.e_n)
        me.graph.build_reach_graph()
        me.vertices = me.graph.get_vertices() 
        me.reachable_lists = dict()
        for v in me.vertices:
            me.reachable_lists[v] = []
     
    def show_graph(me):
        print('==========GRAPH=============')
        me.graph.show_graph()
    def show_result(me):
        
        print("====================RESULT=================")
        me.show_graph()
        print("LIST of VERTICES REACHABLE from " + me.v_start + ": ")
        
        rl = me.reachable_lists[me.v_start]
        print(rl)
    def get_adj_list(me, v):
            return me.graph.get_adj_list(v)
    def add_reachable(me, v):
        rl = me.reachable_lists[me.v_start]
        if v not in rl:
            rl.append(v)
    def get_expanding_vertices(me, vertex):
        # A vertex V is passed as a parameter to this mehod. This
        # method returns the list of candidate vertices which may be
        # USED for EXPANSION of the SEARCH from vertex V. The vertices
        # that have already been REACHED are EXCLUDED from  the list.
        adj_l = me.graph.get_adj_list(vertex)
        rl = me.reachable_lists[me.v_start]
        vl = []
        for av in adj_l:
            if av not in rl:
                vl += [av]
        return vl
        
    def get_next_node(me, node_v):
        # This METHOD RETURNS the NEXT NODE to be PROCESSED in the
        # DFS SEARCH. A NODE D is PASSED as a PARAMETER to this mehod.
        # NODE D contains a list of REMAINING VERTICES that are
        # CANDIDATES for EXPANSION from NODE D. The FIRST VERTEX is
        # SELECTED from the list. Following that, a NEW CHILD NODE
        # is CREATED based on the SELECTED VERTEX. This method returns the
        # child node. If the list of REMAINING VERTICES for the NODE D
        # is EMPTY, the SAME LOGIC is applied RECURSIVELY to SUCCESSIVE
        # ANCESTORS of this NODE until an ANCESTOR with NON-EMPTY list
        # is FOUND, or the ROOT of the SEARCH TREE is REACHED. Going UPWARD
        # in the TREE is in ESSENCE the application of the BACKTRACKING
        # concept in AI.
        if node_v != None:
            edge_vertex = node_v.get_next_edge_vertex()
            if edge_vertex == None:
                if node_v.parent == None:
                    return None
                else:
                    print("NEXT NODE: Moving BACK to NODE(" + \
                          node_v.parent.vertex + ")")
                    return me.get_next_node(node_v.parent)
            else:
                vl = me.get_expanding_vertices(edge_vertex)
                child_v = node(edge_vertex, node_v, vl)
                print("NEXT NODE:", child_v.vertex)
                return child_v
        else:
            return None
    
    def depth_first_search(me, node_v):
        if node_v == None:
            return
        elif node_v.vertex in me.reachable_lists[me.v_start]:
            print("PRUNED VERTEX(", node_v.vertex, ")")
            me.depth_first_search(me.get_next_node(node_v))
        else:                        
            print("------------------------------")
            print("CURRENT VERTEX(",node_v.vertex, \
                  ")...", node_v.get_path_str())
            me.add_reachable(node_v.vertex)
            next_node = me.get_next_node(node_v)
            me.depth_first_search(next_node)
            
    def initialize_dfs(me):
        #============VERY IMPORTANT==================
        # These initializations MUST be performed before EACH START
        # of the DEPTH-FIRST SEARCH algorithm with a GIVEN VERTEX.
        vl = me.get_expanding_vertices(me.v_start)
        node_v = node(me.v_start, None, vl)
        return node_v
    def input_v(me):
        me.show_graph()
        me.v_start = input("Enter name of START VERTEX(vq to quit): ")
        if me.v_start == 'vq':
            me.v_goal = ' ';
            return False
        else:
            return True
        
    def start_dfs(me):
        while me.input_v() == True:
            if me.v_start not in me.vertices:
                print("ERROR: Invalid vertex names.")
                continue
            else:
                print("<<<<<<<DEPTH FIRST SEARCH OUTPUT>>>>>>>>>>")
                print("START VERTEX is: " + me.v_start)
                me.depth_first_search(me.initialize_dfs())
                me.show_result()
        
dfs_v = dfs()
dfs_v.start_dfs()

