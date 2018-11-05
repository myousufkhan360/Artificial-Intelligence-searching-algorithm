# This class contains various FUNCTIONS for the CREATION
# and MANIPULATION of a SQUARE GRID. The SQUARE GRID is
# USED as INPUT to the GREEDY BEST FIRST SEARCH algorithm
# which SOLVES a particuar problem. The SQUARE GRID CONSISTS
# of CELLS distributed over N ROWS and N COLUMNS. The value
# of N is specified in a VARIABLE. Some of the CELLS are
# SPECIAL CELLS called PEGS. A DIFFERENT CONFIGURATION of PEGS
# RESULTS EACH TIME the GRID is CREATED. A PEG configuration
# is GENARATED in SUCH a WAY that the RESULTING SOLUTION
# PATHS have sufficient structural depth and the WORKING
# of the SEARCH ALGORITHM can be OBSERVED PROPERLY in the
# TRACE OUTPUT.
# 
import random as mr

class cl_grid:
    def __init__(me, n):
        me.w = n    # size of a row and column of the square me.grid.
        me.grid = []
        me.build_grid()
    def place_pegs(me): # This method would be overriden
        pass
    def set_initial_grid(me):
        me.g_initial = []
        for r in range(me.w):
            row = []
            for c in range(me.w):
                row.append(me.get_mark(r, c))
            me.g_initial.append(row)

    def build_grid(me):
        me.grid = []
        for r in range(me.w):
            row = []
            for c in range(me.w):
                row.append('*')
            me.grid.append(row)
        me.place_pegs()
        me.set_initial_grid()    
    def is_peg(me, row_n,col_n):
        row_l = me.grid[row_n]
        if row_l[col_n] == 'P' or row_l[col_n] == 'Q':
            return True
        else:
            return False
    def scan_peg(me, row_n,col_n):
        r = row_n
        while r >=0:
            if me.is_peg(r, col_n):
                return r
            else:
                r -= 1
        return -1
    def get_mark(me, row_n, col_n):
        rl = me.grid[row_n]
        return rl[col_n]
    def is_mark(me, r, c, mark):
        return me.get_mark(r, c) == mark
    def set_mark(me, r, c, mark):
        rl = me.grid[r]
        rl[c] = mark
    
    def set_peg_mark(me, r, c):
        me.set_mark(r, c, 'Q')
    def set_short_mark(me, r, c):
        me.set_mark(r, c, 'X')
    def set_search_marks(me):
        for r in range(me.w):
            for c in range(me.w):
                if me.is_mark(r, c, 'Q'):
                   me.set_mark(r, c, 'X')
    def mark_solution(me, path_v):
        ln = len(path_v)
        for n in range(ln):
            row_col = path_v[n]
            me.set_mark(row_col[0], row_col[1], 'V')

    def show_grid(me):
        print('==========GRID=============')
        for n in range(me.w):
            print(n, ": ", me.grid[n])
    def show_initial_grid(me):
        print('==========INITIAL GRID=============')
        for n in range(me.w):
            print(n, ": ", me.g_initial[n])
    def show_solution(me, path_v):
        print("============SOLUTION============")
        me.mark_solution(path_v)
        me.show_grid()
class gbfs_grid(cl_grid):
    def __init__(me, n):
        super().__init__(n)
    
    def place_pegs(me):
        mr.seed()
        #================================================
        # This method MARKS PEGS in the GRID. A LOCATION
        # for a PEG is SELECTED amongst all CELLS. The letter
        # 'P' is PLACED in the CELL to mark it as PEG. For
        # the purpose of programming, a PEG may later be
        # marked with the letter 'Q'.
        #================================================
        for col_n in range(me.w):
            half = int(me.w / 2)
            if col_n < 2:
                count = 1
            else:
                count = mr.randint(1, 2 + int(col_n / 2))
            for n in range(count):
                for tries in range(5):
                    if col_n < 2:
                        row_n = half + mr.randint(0, int(half))
                    else:
                        row_n =  mr.randint(0, me.w - 1)
                    if row_n > me.w - 1:
                        row_n = me.w - 1
                
                    rl = me.grid[row_n]
                    if rl[col_n] == 'P':
                        continue
                    else:
                        rl[col_n] = 'P'
                        break
    
    
