class gbfs_node:
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
    
    
    def __init__(me, r, c, parent):
        me.row_n = r
        me.col_n = c
        me.parent = parent
        me.found = False
        if parent == None:
            me.set_root()
                                            
    def __lt__(me, node_compare):
        # IMPLEMENTATION of '<' OPERATOR (required for SELECTION
        # in PRIORITY QUEUE).
        return me.get_priority() < node_compare.get_priority()
    
    def __init__(me, r, c, parent):
        me.row_n = r
        me.col_n = c
        me.parent = parent
        me.found = False
        if parent == None:
            me.set_root()
                                    
    def __lt__(me, node_compare):
        return me.get_priority() < node_compare.get_priority()
    #===================================================
    def get_priority(me):
        # This method returns the PRIORITY of this NODE as the
        # SINGLE HEURISTIC USED in this implementation of
        # of the GBFS Algorithm. This NODE as well as other NODES
        # are STORED in a PYTHON PRIORITY QUEUE. The Node with
        # LOWEST value of PRIORITY is REMOVED before OTHER NODES
        # from the PRIORITY QUEUE.
        return me.fn
    def set_root(me):
        me.parent = None
        me.cost = 0
        me.fn = me.get_goal_estimate()
    def get_trace_s(me):
        s = "(r,c) = (" + str(me.row_n) + ", " + \
          str(me.col_n) + ")"
        s += "   <COST = " + str(me.cost) + ">"
        return s
    def get_path(me):
        path_curr = [(me.row_n, me.col_n)]
        if me.parent == None:
            return path_curr
        else:
            return me.parent.get_path() + path_curr
    def show_values(me):
        print("NODE:", me.get_trace_s())
        print("NODE PATH: " + str(me.get_path()))
        print("NODE HEURISTIC(GOAL MIN): " + str(me.fn))
    def show_new_values(me):
        print("-----------------")
        print("GENRATED CHILD: " + me.get_trace_s())
        print("CHILD PATH: " + str(me.get_path()))
        print("CHILD HEURISTIC(GOAL MIN) = " + str(me.fn))
    def get_v_cost(me, child_r):
        return me.row_n - child_r
    def get_r_cost(me, child_c):
        return child_c - me.col_n
    def get_cost_bound(me, gw):
        #-----------------------------------------------------
        # The COST BOUND would be the COST associated with the
        # WORST SOLUTION PATH. The WORTH PATH would result if
        # the CURSOR makes ONLY SHORT MOVES to REACH the GOAL
        # (FIRST) ROW. The problem definition implies that SUCH
        # a SOLUTION PATH ALWAYS EXISTS and its COST can be
        # USED as an UPPER BOUND on the COST of ANY SOLUTION.
        return (gw - 1) * 2
    def get_child_increase(me, child_r, child_c):
        return me.get_v_cost(child_r) + me.get_r_cost(child_c)
    def get_short_increase(me):
        return 2
    def get_goal_estimate(me):
        return me.get_v_cost(0)
    def create_move(me, child_r, child_c):
        child_v = gbfs_node(child_r, child_c, me)
        child_v.cost = me.cost + me.get_child_increase(child_r, child_c)
        child_v.fn = child_v.get_goal_estimate()
        child_v.show_new_values()
        return child_v
    def create_short_move(me):
        child_v = gbfs_node(me.row_n - 1, me.col_n, me)
        child_v.cost = me.cost + me.get_short_increase()
        child_v.fn = child_v.get_goal_estimate()
        child_v.show_new_values()
        return child_v
       
    
    
