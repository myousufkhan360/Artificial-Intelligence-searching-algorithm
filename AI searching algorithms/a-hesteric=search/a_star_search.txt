# This Python application applies the A * SEARCH
# ALGORITHM in AI for solving a problem. The problem
# is to FIND a SHORTEST PATH between TWO VERTICES of
# a DIRECTED GRAPH that has WEIGHTED EDGES. The graph
# itself is implemented as a class in a SEPARATE PYTHON
# MODULE. The class for graph is imported by this module.
#
# A * Search is ONE TYPE of a Best First Search Algorithms.
# According to the DEFINIIION of A * SEARCH ALGORITHM,
# TWO HEURISTIC VALUES MUST be COMBINED to GENERATE
# the HEURISTIC VALUE that would be USED for MOVE
# SELECTION during the SEARCH. In each iteration of the
# SEARCH, a VERTEX is SELECTED as the CURRENT VERTEX. Each
# POSSIBLE MOVE is BASED on FOLLOWING a SINGLE EDGE from
# the CURRENT VERTEX to the TERMINATING VERTEX of that EDGE.
# For each move, The FIRST HEURISTIC g(n) is the VALUE of the
# TOTAL COST involved if the MOVE is MADE. FOR EACH MOVE, the
# SECOND HEURISTIC h(n) is the ESTIMATE of the AMOUNT by which
# the TOTAL COST may INCREASE during SUBSEQUENT MOVES until
# the GOAL VERTEX is REACHED. The ACTUAL ADDITIONAL COST of
# REACHING the GOAL MUST NEVER EXCEED the ESTIMATED COST,
# if the FIRST SOLUTION YIELDED is to be an OPTIMAL SOLUTION.
# 
# The FULL HEURISTIC VALUE fn for a MOVE is computed as:
#               f(n) = g(n) + h(n)
# Thus, for each move, the FULL HEURISTIC takes into ACCOUNT
# both the CUMULATIVE COST if the MOVE is SELECTED as well
# as POSSIBLE FURTHER (OPTIMISTIC) COST.
#
# In this implementation, the VALUE for GOAL ESTIMATE is
# determined as the COST of ONE of the EDGES that are going
# out of the VERTEX for which the heuristic is to be computed.
# The the SMALLEST COST among COSTS of SUCH EDGES is SET as
# the VALUE of the SECOND HEURISTIC h(n). It is obvious that,
# the ACTUAL VALUE of ADDITIONAL COST involved in REACHING the
# GOAL CANNOT be LESS THAN the MINIMAL ESTIMATE h(n). Note that
# the COST of any EDGE CANNOT be NEGATIVE. This makes the
# heuristic hn an ADMISSIBLE HEURISTIC. Also, the requirement of
# CONSISTENCY is FULFILLED by the HEURISTIC. For a DEFINITION of
# terms "ADMISSIBLE" and "CONSISTANT" "HEURISTIC", the READER might
# REFER to some relevent material on Artificial Intelligence.
#
# Since the application of the HEURISTIC, in this implementation
# of the A * Algorithm, is BOTH ADMISSIBLE and CONSISTENT, it is
# CORRECT to CONCLUDE that the FIRST SOLUTION YIELDED would be an
# OPTIMAL SOLUTION (i.e. a PATH having MINIMUM TOTAL COST). 
#
#==============================================================
import heapq as mq
from m_shp_w_graph import cl_shp_w_graph
from m_v_node import v_node
class a_star_shp:
    def __init__(me):
        me.max_val = 200000
        me.graph = cl_shp_w_graph(12, 22)
        me.graph.build_shp_graph()
        me.vertices = me.graph.get_vertices()
    def init_a_star_q(me):
        me.pq = []
        mq.heapify(me.pq)
    def init_cost_mins(me):
        # SET the INITIAL MINMUM COST for EACH VERTEX to a VERY
        # HIGH (IMPOSSIBLE) VALUE. The VALUE REPRESENTS INFINITY.
        me.cost_mins = dict()
        for v in me.vertices:
            me.cost_mins[v] = me.max_val
        me.cost_mins[me.v_start] = 0
    def init_goal_estimates(me):
        # SET the INITIAL MINMUM GOAL ESTIMATE for EACH VERTEX V by
        # SELECTING the MINIMUM COST VERTIX in the ADJACENCY LIST of V.
        me.goal_estimates = dict()
        for v in me.vertices:
            adj_values = me.get_adj_list(v)
            min_cost = -1
            for adj_vertex, edge_cost in adj_values:
                if min_cost == -1:
                    min_cost = edge_cost
                elif edge_cost < min_cost:
                    min_cost = edge_cost
            me.goal_estimates[v] = min_cost
        
    def initialize(me):
        me.init_a_star_q()
        me.init_cost_mins()
        me.init_goal_estimates()
    def get_adj_list(me, vertex):
        return me.graph.get_adj_list(vertex)
    def show_result(me, node_v):
        me.graph.show_graph()
        if node_v == None:
            print("The vertices", me.v_start, "and", me.v_goal, \
                  " are NOT CONNECTED.")
        else:
            print("Shortest Path from VERTEX(", me.v_start, \
                  "to", me.v_goal, ")")
            print("SHORTEST PATH:", node_v.get_path())
                    
        
    def create_root(me):
        node_v = v_node(me.v_start, 0, None, me.goal_estimates[me.v_start])
        me.add_to_q(node_v)
        return node_v
    def input_vertices(me):
        me.graph.show_graph()
        me.v_start = input("Enter start vertex. vq to quit: ")
        if me.v_start == 'vq':
            return False
        else:
            me.v_goal = input("Enter vertex to be reached: ")
            return True
    #<<<<<<<<<<<<<<<<<<<<<VERY IMPORTANT>>>>>>>>>>>>>>>>>>>
    def is_q_empty(me):
        return len(me.pq) == 0
    def add_to_q(me, node_v):
        mq.heappush(me.pq, node_v)
    def remove_from_q(me):
        #===============================================
        # The NODE HAVING THE SMALLEST HEURISRIC is REMOVED
        # FIRST from the HEAP BASED PRIORITY QUEUE. 
        #
        if len(me.pq) == 0:
            pass
        else:
            return mq.heappop(me.pq)
        #================================================
      
    #<<<<<<<<<<<<<<<<<<------------------->>>>>>>>>>>>>>>>>>>
    def a_star_search(me):
        #===================================================
        #===================================================
        # SELECT a NODE as the CURRENT NODE by REMOVING it from the
        # PRIORITY QUEUE. The NODE with the LOWEST HEURISTIC fn (LEAST
        # TOTAL COST) is REMOVED.
        if me.is_q_empty():
            # If the PRIRITY QUEUE is EMPTY it implies that the GOAL
            # VERTEX CANNOT be REACHED from the START VERTEX.
            me.found = False
            me.failed = True
            return None
        curr_v = me.remove_from_q()
        
        print("===============================================")
        print("REMOVED NODE")
        curr_v.show_values()
        print("---------------")
        if curr_v.vertex == me.v_goal:
            me.found = True
            me.failed = False
            return curr_v
        #===================================================
        
        adj_values = me.get_adj_list(curr_v.vertex)
        #===================VERY IMPORTANT=======================
        # This LOOP GENARATES CHILD NODES of the CURRENT (REMOVED)
        # NODE and ADDS them to the PRIORITY QUEUE. However, if the
        # MINIMUM PATH COST ASSOCIATED with the VERTEX of a CHILD 
	# NODE is LESS THAN or EQUAL to the COST of the PATH UP TO
	# the CHILD NODE, that CHILD NODE is NOT GENERATED and NOT 
	# ADDED to the PRIORITY QUEUE.  
        for edge_vertex, edge_cost in adj_values:
            child_cost = curr_v.gn + edge_cost
            if me.cost_mins[edge_vertex] <= child_cost:
                print("PRUNED EDGE(", curr_v.vertex, "--", \
                    edge_vertex, "): COST = ", child_cost )
            else:
                me.cost_mins[edge_vertex] = child_cost
                child_v = curr_v.create_move(edge_vertex,
                            edge_cost, me.goal_estimates[edge_vertex])
                me.add_to_q(child_v)
                
        return curr_v 
    
    def start_shp(me):
         me.v_start = ' '
         while me.input_vertices() == True:
             print("==========================================")
             
             if me.v_start not in me.vertices or me.v_goal not in me.v_goal:
                 print("Invalid vertex name")
                 continue
             print("A * Search: Shotest Path Problem---OUTPUT")
             print("Vertices are: ", me.v_start, ", ", me.v_goal)
             me.initialize()
             curr_v = me.create_root()
             me.failed = False
             me.found = False
             while me.failed == False:
                 curr_v = me.a_star_search()
                 if me.found == True:
                     break
             me.show_result(curr_v)
             
ob = a_star_shp()
ob.start_shp()
