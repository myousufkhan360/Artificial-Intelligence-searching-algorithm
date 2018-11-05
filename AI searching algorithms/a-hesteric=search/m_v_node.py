class v_node:
    
    def __init__(me, vertex, edge_cost, prev, goal_estimate):
        me.vertex = vertex
        me.prev = prev
        if prev == None:
            me.set_start(goal_estimate)
        else:
            me.set_values(vertex, edge_cost, goal_estimate)

    #==============VERY IMPORTANT=======================
    # Normally, in PYTHON, the '<', '>', and certain other
    # OPERATORS CANNOT be USED for COMPARING an OBJECT of a
    # USER-DEFINED CLASS with any ITEM. However, SUCH
    # COMPARISONS become POSSIBLE if a USER-DEFINED CLASS
    # CONTAINS a method having a PREDEFINED NAME CORRESPONDS
    # to an OPERATOR. For example, the '<' OPERATOR can be
    # implemented in a class by DEFINING the METHOD with
    # the PREDEFINED NAME '__lt__'. Similarly, the METHOD NAMES
    # '__le__' and '__gt__' CORRESPOND to the OPERATORS '<=' and
    # '>', RESPECTIVELY. This class implements the '<' OPERATOR.
            
    def __lt__(me, node_compare):
        # IMPLEMENTATION of '<' OPERATOR (required for SELECTION
        # in PRIORITY QUEUE).
        return me.get_priority() < node_compare.get_priority()
   
    #===================================================
    def get_priority(me):
        # This method returns the PRIORITY of this NODE as the
        # COMBINED HEURISTIC USED in this implementation of
        # of the A * Algorithm. This NODE as well as other NODES
        # are STORED in a PYTHON PRIORITY QUEUE. The Node with
        # LOWEST value of PRIORITY is REMOVED before OTHER NODES
        # from the PRIORITY QUEUE.
        return me.fn
    def set_values(me, vertex, edge_cost, goal_estimate):
        me.gn = me.prev.get_child_cost(edge_cost)
        me.hn = goal_estimate
        me.fn = me.gn + me.hn
    def set_start(me, goal_estimate):
        me.prev = None
        me.gn = 0
        me.hn = goal_estimate
        me.fn = me.gn + me.hn
        
    def get_trace_s(me):
        s = "Vertex: (" + me.vertex + "): \n"
        s += "<HEURISTIC(f(n) = COST + GOAL ESTIMATE(MINIMAL EDGE))>:\n "
        s += " COST(g(n)) = " + str(me.gn) + "\n "
        s += " GOAL ESTIMATE(h(n)) = " + str(me.hn) + "\n "
        s += "- - - - - - - -\n "
        s += " <HEURISTIC(f(n)) = " + str(me.fn) + ">"
        return s
    def show_values(me):
        print("NODE:", me.get_trace_s())
        print("NODE PATH: " + str(me.get_path()))
    def show_new_values(me):
        print("GENRATED CHILD: " + me.get_trace_s())
        print("CHILD PATH: " + str(me.get_path()))
    def get_path(me):
        path_curr = [(me.vertex, me.gn)]
        if me.prev == None:
            return path_curr
        else:
            return me.prev.get_path() + path_curr
    def get_child_cost(me, edge_cost):
        return me.gn + edge_cost
    def create_move(me, edge_vertex, edge_cost, goal_estimate):
        print("-----------------")
        print("EXPANDING EDGE(", me.vertex, "--", \
                      edge_vertex,")  EDGE COST:", edge_cost)
        child_v = v_node(edge_vertex, edge_cost, me, goal_estimate)
        child_v.show_new_values()
        return child_v
    
    
