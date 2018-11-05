# This Python application applies the GREEDY BEST FIRST
# SEARCH (GBFS) ALGORITHM in AI for solving a problem. The
# problem is given the name "CURSOR PROBLEM". The READER must
# READ the DESCRIPTION of the CURSOR PROBLEM, in order to fully
# UNDERSTAND its LOGICAL STRUCTURE. The DESCRIPTION is saved
# as an MS-Word DOCUMENT within a folder INSIDE the FOLDER
# of THIS MODULE.
#
# GBFS Algorithm is ONE TYPE of Best First Search Algorithms.
# According to the DEFINIIION of GBFS ALGORITHM, the HEURISTIC
# VALUE fn for ANY MOVE of the CURSOR is COMPUTED as the ESTIMATE
# of the REMAINING INCREASE in the COST that can TAKE PLACE AFTER
# making that MOVE. In other words, the HEURISTIC is an ESTIMATE
# of the POSSIBLE FURTHER INCREASE in COST until the GOAL is
# REACHED. The ACTUAL VALUE of REMAINING COST would be BASED on
# the CONFIGURATION of PEGS in the GRID. In this implementation,
# the ESTIMATE fn of the REMAINING INCREASE in COST is MINIMAL (MOST
# OPTIMISTIC). Therefore, the value of the ACTUAL INCREASE can
# NEVER be LESS than the ESTIMATE.   
#
# It must be NOTED that GBFS algorithm, in general, DOES NOT
# yield an OPTIMAL SOLUTION. 
#
# As the CURSOR makes MOVES, information about each of its
# LOCATIONS is STORED in NODES. In each ITERATION of the GBFS
# Algorithm, the NODE with the LOWEST HEURISIC value is
# SELECTED as the CURRENT NODE. The CURRENT NODE results in
# genaration of CHILD NODES corresponding to moves that
# can be made from the CURRENT NODE. The ALGORITHM ENDS when
# the ROW of the CURRENT NODE is the FIRST ROW.

#==============================================================
import heapq as mq
from m_gbfs_grid import gbfs_grid 
from m_gbfs_cursor import gbfs_node
class cl_gbfs:
    def initialize_gbfs(me):
        me.grid = gbfs_grid(5)
        me.init_gbfs_q()
    def init_gbfs_q(me):
        me.pq = []
        mq.heapify(me.pq)
    
    def show_result(me, node_v):
        if node_v.row_n == 0:
            me.grid.show_initial_grid()
            me.grid.set_search_marks()
            print("====SEARCH STATES=======")
            me.grid.show_grid()
            me.grid.show_solution(node_v.get_path())    
            print("SOLUTION COST: ", node_v.cost)
        else:
            print("There is no solution.")
        
    def create_root(me):
        node_v = gbfs_node(me.grid.w - 1, 0, None)
        me.add_to_q(node_v)
        return node_v
    #<<<<<<<<<<<<<<<<<<<<<VERY IMPORTANT>>>>>>>>>>>>>>>>>>>
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
      
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>
    def gbfs(me):
        #===================================================
        # On the basis of the PROBLEM DEFINITION, the CURSOR
        # would ALWAYS REACH the FIRST ROW. So there is NO NEED
        # to CHECK for FAILURE.
        #===================================================
        #===================================================
        # SELECT a NODE as the CURRENT NODE by REMOVING it from the
        # PRIORITY QUEUE. The NODE with the LOWEST HEURISTIC fn is
        # REMOVED.
        curr_v = me.remove_from_q()
        #===================================================
        print("===============================================")
        print("REMOVED NODE")
        curr_v.show_values()
        if curr_v.row_n == 0:
            return curr_v
        print("---------------")
                
        c = curr_v.col_n - 1
        while c < me.grid.w - 1:
            c += 1
            #==============================================
            # The UPWARD SCANNING for the CLOSEST PEG in a COLUMN
            # is performed here. The SCANNING must obviously START
            # from the ROW IMMEDIATELY ABOVE the CURRENT ROW.
            new_row = me.grid.scan_peg(curr_v.row_n-1,c)
            #=================================================
        
            if new_row != -1:
                # CREATE a CHILD NODE.
                short = False
                child_v = curr_v.create_move(new_row, c)
                
            elif c == curr_v.col_n:
                # CREATE a SHORT MOVE NODE
                short = True
                child_v = curr_v.create_short_move()
                
            else:
                # There is NO MOVE if there is NO PEG REMAINING in the
                # COLUMN.
                continue
            #-------------------------------------------------
            # Add the CHILD NODE to the PRIORITY QUEUE ONLY if the
            # TOTAL COST for the CHILD NODE is NOT GREATER than the
            # FINAL COST of the WORST SOLUTION PATH. This is a PRUNING
            # OPERATION.
            if child_v.cost <= me.cost_bound:
                if short == False:
                    me.grid.set_peg_mark(child_v.row_n, child_v.col_n)
                else:
                    me.grid.set_short_mark(child_v.row_n, child_v.col_n)    
                me.add_to_q(child_v)
            else:
                print("CHILD PRUNED: CHILD COST HIGHER THAN WORST CASE")
            #-------------------------------------------------    
                        
        return curr_v
    def start_gbfs(me):
        me.initialize_gbfs()
        me.grid.show_initial_grid()
        curr_v = me.create_root()
        me.cost_bound = curr_v.get_cost_bound(me.grid.w)
        print("UPPER BOUND COST:", me.cost_bound)
        count = 0
        while curr_v.row_n != 0:
            if len(me.pq) == 0:
                # The above condition would imply failure. A failure
                # would NOT occur for the given problem.
                break
            else:
                curr_v = me.gbfs()
            count += 1
        me.show_result(curr_v) 
        print("Number of GBFS function invocations = " + str(count))
cl_gbfs().start_gbfs()
