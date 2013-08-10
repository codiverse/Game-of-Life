#!/usr/bin/python

#
# Conway's Game of Life
#
# Works on a provided 'layout' from same directory level file - grid.py
#
# Terminology and operation:
#
# 'Universe' is comprised of a 'grid' 'layout', made up of 'cells'.
#
# Cells are stored in 'columns' and 'rows', a 2D nested list in code terms,
# they can either be 'alive' (represented by a 1) or 'dead' (by a 0).
#
# Each change of the grid layout is a 'Generation' and matches a time 'tick',
# which is accompanied by a refresh of the screen.
#
# Usage:
# python game_of_life.py -h
#


import sys
import os

from optparse import OptionParser
from copy import deepcopy
from time import sleep

# Same directory level grid.py file, should contain 2D list 'layout'
import grid
from grid import random_universe


def show_universe(universe, show_grid, character):
    """ Prints the Universe to screen, a row (line) at a time """
    row_number = 0
    column_number = 0
    line = ""

    for row in universe:
        for cell in row:
            current_cell = [row_number, column_number]
            if universe[current_cell[0]][current_cell[1]] == 0:
                if show_grid == True:
                    line += "[ ]"
                else:
                    line += "   "
            else:
                if show_grid == True:
                    line += "[%s]" % character
                else:
                    line += " %s " % character
            column_number += 1

        print line
        line = ""
        column_number = 0
        row_number += 1

def count_alive_neighbours(universe, current_cell):
    """ Counts the surrounding 8 cells that are of value 1 (alive) 
    
    Works on a single input cell at a time.
    
    Returns the sum total of alive surrounding cells.    
    """
    current_row = current_cell[0]
    current_column = current_cell[1]

    try:
        # Prevents 'wrap around' of grid due to possibility of negative indexes
        if current_row - 1 < 0 or current_column - 1 < 0:
            return 0
        else:
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
    """ Runs the rule set against the current cell and its neighbour count.
    
    Returns the final cell state.
    """

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
    """ Works through every cell in the provided Universe.
    
    Acquires in turn each cell's position and current value.
    Also calculates the sum of alive cells surrounding it.
    Runs the current value and the sum of alive surrounding cells 
    against the ruleset, altering state as appropriate.
    
    Returns the next Universe layout grid.
    """

    # deepcopy (recursive) is required due to nested list objects
    next_universe = deepcopy(universe)
    row_number = 0
    column_number = 0
    for row in universe:
        for cell in row:
            current_cell = [row_number, column_number]
            alive_neighbour_count = count_alive_neighbours(universe,
                                                           current_cell)
            current_cell_value = universe[current_cell[0]][current_cell[1]]
            end_state = process_rules(current_cell_value, alive_neighbour_count)
            next_universe[row_number][column_number] = end_state
            column_number += 1
        column_number = 0
        row_number += 1

    return next_universe

def set_options():
    """ Separated out to keep main() code cleaner """
    # TODO: add option for which layout to use, and time tick rate
    parser = OptionParser()
    parser.add_option("-g", "--generations", dest="generations", default=50,
                      help="Number of Generations to run for")
    parser.add_option("-s", "--showgrid", dest="show_grid",
                      action="store_true", default=False,
                      help="Specify whether to show detailed universe grid")
    parser.add_option("-r", "--randomsize", dest="random_size",
                      default=0,
                      help="Build a random Universe of this grid size")
    parser.add_option("-t", "--timetick", dest="time_tick", default=0.1,
                      help="The time interval of generations, in seconds")
    parser.add_option("-c", "--character", dest="character", default="#",
                      help="Character used to display a living cell")
    (options, args) = parser.parse_args()

    show_grid = options.show_grid
    generations = int(options.generations)
    random_size = int(options.random_size)
    time_tick = float(options.time_tick)
    character = options.character

    return (show_grid, generations, random_size, time_tick, character)


def main():
    show_grid, generations, random_size, time_tick, character = set_options()

    generation = 0
    if random_size != 0:
        universe = random_universe(random_size)
    else:
        universe = grid.layout

    # tick spans a generation
    for tick in range(generations + 1):
        os.system('clear')
        print "generation %d / %d [%s seconds per generation]" % (generation,
                                                           generations,
                                                           time_tick)
        current_state = universe
        show_universe(current_state, show_grid, character)
        if generation == 0:
            sleep(1)

        next_universe = process_cells(universe)
        universe = next_universe

        sleep(time_tick)

        generation += 1


if __name__ == "__main__":
    os.system('clear')
    main()
