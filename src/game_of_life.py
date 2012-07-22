#!/usr/bin/python

import sys
import os
from copy import deepcopy
from time import sleep

import grid

"""
def create_universe():
    universe  = [
                 [0,0,0,0,0,0],
                 [0,1,1,1,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]
                ]
    
    return universe
"""
    
def show_universe(universe):
    #universe_height = len(universe)
    #print "universe height = %s"  % universe_height
    #universe_width = len(universe[0])
    #print "universe_width = %s" % universe_width
    #print ""
    
    #for row in universe:
    #    print row

    row_number = 0
    column_number = 0
    line = ""
    
    for row in universe:
        for cell in row:
            current_cell = [row_number,column_number]
            if universe[current_cell[0]][current_cell[1]] == 0:
                #line += "[   ]"
                line += "   "
            else:
                #line += "[ * ]"
                line += " * "
            column_number += 1
            
        print line
        line = ""
        column_number = 0
        row_number +=1
        print ""

def count_alive_neighbours(universe, current_cell):
    current_row = current_cell[0]
    current_column = current_cell[1]
    
    #print "current row = %d" % current_row
    #print "current column = %d" % current_column

    #print "full row = %s" % universe[current_row]

    try:
        total = 0
        total += universe[current_row - 1][current_column - 1]
        total += universe[current_row - 1][current_column]
        total += universe[current_row - 1][current_column + 1]
        total += universe[current_row][current_column - 1]
        total += universe[current_row][current_column + 1]
        total += universe[current_row + 1][current_column - 1]
        total += universe[current_row + 1][current_column]
        total += universe[current_row + 1][current_column + 1]
    except (IndexError):
        pass
    
    return total

def process_rules(current_cell_value, alive_neighbour_count):
    if current_cell_value == 0:
        if alive_neighbour_count == 3:
            # born
            #print "born due to 3 neighbours"
            return 1
        else:
            # still dead
            #print "still dead due to anything other than 3 neighbours"
            return 0
    else:
        if alive_neighbour_count < 2:
            # died
            #print "died due to less than 2 neighbours"
            return 0
        
        if alive_neighbour_count == 2 or alive_neighbour_count == 3:
            # survived
            #print "survived due to 2 or 3 neighbours"
            return 1
    
        if alive_neighbour_count > 3:
            # died
            #print "died due to more than 3 neighbours"
            return 0

def process_cells(universe):
    next_universe = deepcopy(universe)
    row_number = 0
    column_number = 0
    for row in universe:
        for cell in row:
            current_cell = [row_number,column_number]
            #print "current cell = %s" % current_cell
            alive_neighbour_count =  count_alive_neighbours(universe, current_cell)
            current_cell_value = universe[current_cell[0]][current_cell[1]]
            end_state = process_rules(current_cell_value, alive_neighbour_count)
            next_universe[row_number][column_number] = end_state
            column_number += 1
        column_number = 0
        row_number +=1
    
    return next_universe

def main():
    generation = 0
    #universe = create_universe()
    universe = grid.layout
    
    for tick in range(count+1):
        os.system('clear')
        print "generation %d / %d" % (generation, count)
        print "" 
        current_state = universe
        #print "current state:\n"
        show_universe(current_state)
        print ""
    
        next_universe = process_cells(universe)
        universe = next_universe
        
        sleep(0.1)
        generation += 1
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        count = int(sys.argv[1])
    else:
        count = 10
    os.system('clear')
    main()
    

"""
current_cell = [0,1]
alive_neighbour_count =  count_alive_neighbours(universe, current_cell)
print "alive neighbours = %d" % alive_neighbour_count

current_cell_value = universe[current_cell[0]][current_cell[1]]

print process_rules(current_cell_value, alive_neighbour_count)
"""

"""
next_state = deepcopy(universe)
next_state[0][0] = 1
show_universe(next_state)
"""