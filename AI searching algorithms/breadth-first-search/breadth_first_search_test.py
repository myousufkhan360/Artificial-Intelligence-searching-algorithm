# THIS PYTHON APPLICATION APPLIES the BREADTH FIRST
# SEARCH ALGORITHM in AI to a problem. The algorithm
# simply FINDS the SHORTEST PATH between TWO GIVEN
# VERTICES of a DIRECTED GRAPH. The EDGES of the GRAPH
# are DIRECTED and  UNWEIGHTED. By the PROBLEM
# DEFINITION and by the LOGIC of the ALGORITHM, the
# FIRST PATH DISCOVERED between the TWO VERTICES MUST
# be the SORTEST PATH. The ALGORITHM FAILS if there
# is NO PATH between the GIVEN VERTICES.
#
# The GRAPH is IMPLEMENTED in a SEPARATE PYTHON MODULE
# which is IMPORTED in this MODULE.
#=================VERY IMPORTANT=====================
# The LOGIC for FINDING the SHORTEST PATH MAY NOT
# EXACTLY MATCH the LOGIC USED in the STANDARD ALGORITHM
# for SHORTEST PATH. This is JUSTIFIED BECAUSE the PURPOSE
# here is ONLY to SHOW the WORKING of BREADTH FIRST SEARCH,
# in GENERAL. Therefore, the READER must NOT interpret
# the LOGIC as the STANDARD one.
#
from m_shp_graph import cl_shp_graph

class bfs:
    max_val = 20000
    def __init__(me):
        me.v_n = 15;  me.e_n = 35
        me.graph = cl_shp_graph(me.v_n, me.e_n)
        me.graph.build_shp_graph();
        me.vertices = me.graph.get_vertices()
    def init_prevs(me):
        me.prevs = dict()
        for v in me.vertices:
            me.prevs[v] = ' '
    def init_short_vals(me):
        me.short_vals = dict();
        vl = me.vertices;
        for v in vl:
            me.short_vals[v] = me.max_val
    def init_q(me):
        me.bfs_q = []
    def set_status(me):
        me.init_prevs();  me.init_short_vals()
        me.short_vals[me.v_start] = 0; me.init_q()
        
    def show_graph(me):
        print('==========GRAPH=============');  me.graph.show_graph()
    def get_v_path(me, v_first, v_last):
        vl = [];  v = v_last;  vl = [v_last]
        while v != v_first and v != ' ':
            v = me.prevs[v];  vl = [v] + vl
        return vl
    def print_result(me, v):
        print("====================RESULT=================")
        
        me.show_graph();
        if v == None:  print("There is no path.")
        else:
            print("Vertices are: " + me.v_start + ", " + v)
            print("SHORTEST PATH FOUND: " + str(me.get_path_str(v)))    
    def input_v_pair(me):
        print("=============================================")
        me.show_graph()
        me.v_start = input("Enter name of START VERTEX(vq to quit): ")
        if me.v_start == 'vq':
            me.v_goal = ' '; return False
        else:
            me.v_goal = input("Enter name of GOAL VERTEX: "); return True
    def is_q_empty(me):
        return len(me.bfs_q) == 0
    def add_to_q(me, v):
        # ADD the VERTEX to the QUEUE of FRINGE VERTICES.
        me.bfs_q += [v]; 
        
    def remove_from_q(me):
        # REMOVE the NEXT VERTEX from the QUEUE of FRINGE VERTICES
        # (in FIFO ORDER).
        if me.is_q_empty():  pass
        else:
            v = me.bfs_q[0];
            del me.bfs_q[0]
            print("REMOVED from Queue: Vertex(", v, ")"); return v
    def get_path_str(me, v):
        pl = me.get_v_path(me.v_start, v);  ps = "<PATH: "
        for v in pl:
            ps += "--" + v
        ps += ">"
        return ps
    def is_short(me, v, new_val):
        return new_val < me.short_vals[v]   
    def expand_vertex(me, v_curr):
        # This method EXPANDS a VERTEX X by GENERATING its CHILD
        # VERTICES, in the IMPLICIT SEARCH TREE. If there is an EDGE
        # going from the VERTEX X to some VERTEX V, VERTEX V may be
        # GENERATED as CHILD of X by ADDING it to the FIFO Queue of
        # VERTICES. A GENERATED VERTEX may be REMOVED from the Queue
        # later on for its EXPANSION. However, a vertex V is GENERATED
        # as a CHILD of X ONLY if this is the FIRST VISIT to V in the
        # SEARCH or if the PATH FOLLOWED by this INSTANCE of V is
        # SHORTER than the one followed by any previous instance of V.
        # Otherwise, V must NOT be ADDED to the QUEUE.
        print("Expanding Vertex(", v_curr, ")", me.get_path_str(v_curr))
        v_adj = me.graph.get_adj_list(v_curr)
        edge_val = me.short_vals[v_curr] + 1
        for edge_vertex in v_adj:
            if me.is_short(edge_vertex, edge_val) == False:
                print("PRUNED EDGE VERTEX(", v_curr+"--"+edge_vertex, ")")
            else:
                me.short_vals[edge_vertex] = edge_val
                me.add_to_q(edge_vertex);  me.prevs[edge_vertex] = v_curr
                print("ADDED to Queue: Edge Vertex(", v_curr \
                                      + "--" + edge_vertex, ")")
                if edge_vertex == me.v_goal: return edge_vertex
                            
        
        return None
    
        
    def breadth_first_search(me):
        if me.is_q_empty() == True:   return
        print("--------------------------------------------")
        #===============VERY IMPORTANT=====================
        # REMOVE next NODE from FRINGE in FIFO ORDER
        print("Queue: ", me.bfs_q);
        v_curr = me.remove_from_q()
            
        #==================================================
        if v_curr == me.v_goal:
            return v_curr
        else:
            return me.expand_vertex(v_curr)
    
    def start_bfs(me):

        me.goal = None # IMPORTANT
        while me.input_v_pair() == True:
            if not (me.v_start in me.vertices \
                   and me.v_goal in me.vertices):
                print("Invalid vertex names")
                continue
            print("<<<<<<<BREADTH FIRST SEARCH OUTPUT>>>>>>>>>>")
            print("Vertices are: " + me.v_start + ", " + me.v_goal)
            me.set_status()
            me.add_to_q(me.v_start)
            v_curr = None
            while v_curr == None:
                if me.is_q_empty() == True:
                    break
                else:
                    v_curr = me.breadth_first_search()
            print("Vertices are: (", me.v_start, "), (", me.v_goal, ")")
            me.print_result(v_curr)
        
            
        
bfs_v = bfs();
bfs_v.start_bfs()
