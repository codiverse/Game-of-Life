from unittest import TestCase

from game_of_life import count_alive_neighbours
from game_of_life import process_rules
from game_of_life import process_cells
from grid import test_layout

class grid_test(TestCase):
    
    def setUp(self):
        self.universe =  [
             [0,0,0,0,0,0],
             [0,0,1,0,0,0],
             [0,0,1,0,0,0],
             [0,0,1,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]
          ]
    
    def load_grid_test(self):
        self.assertEqual(test_layout, self.universe)

class game_of_life_test(TestCase):
    
    def setUp(self):
        self.universe =  [
             [0,0,0,0,0,0],
             [0,0,1,0,0,0],
             [0,0,1,0,0,0],
             [0,0,1,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]
          ]
        self.next_universe =  [
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,1,1,1,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]
          ]
        self.wrap_test_universe =  [
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,1,1,1,0]
          ]
        
    
    def count_alive_neighbours_none_test(self):
        self.current_cell = [0,0]
        self.alive_neighbours = count_alive_neighbours(self.universe, self.current_cell)
        self.assertEqual(self.alive_neighbours, 0)
    
    def count_alive_neighbours_one_test(self):
        self.current_cell = [3,2]
        self.alive_neighbours = count_alive_neighbours(self.universe, self.current_cell)
        self.assertEqual(self.alive_neighbours, 1)
        
    def count_alive_neighbours_two_test(self):
        self.current_cell = [1,1]
        self.alive_neighbours = count_alive_neighbours(self.universe, self.current_cell)
        self.assertEqual(self.alive_neighbours, 2)
        
    def count_alive_neighbours_three_test(self):
        self.current_cell = [2,1]
        self.alive_neighbours = count_alive_neighbours(self.universe, self.current_cell)
        self.assertEqual(self.alive_neighbours, 3) 
        
    def dead_cell_born_test(self):
        self.current_cell_value = 0
        self.alive_neighbour_count = 3
        self.end_state = process_rules(self.current_cell_value, self.alive_neighbour_count)
        self.assertEqual(self.end_state, 1)
        
    def dead_cell_still_dead_due_to_less_than_three_neighbours_test(self):
        self.current_cell_value = 0
        self.alive_neighbour_count = 2
        self.end_state = process_rules(self.current_cell_value, self.alive_neighbour_count)
        self.assertEqual(self.end_state, 0)
        
    def dead_cell_still_dead_due_to_more_than_three_neighbours_test(self):
        self.current_cell_value = 0
        self.alive_neighbour_count = 4
        self.end_state = process_rules(self.current_cell_value, self.alive_neighbour_count)
        self.assertEqual(self.end_state, 0)
    
    def alive_cell_died_due_to_less_than_two_neighbours_test(self):
        self.current_cell_value = 1
        self.alive_neighbour_count = 1
        self.end_state = process_rules(self.current_cell_value, self.alive_neighbour_count)
        self.assertEqual(self.end_state, 0)    
    
    def alive_cell_still_alive_due_to_two_neighbours_test(self):
        self.current_cell_value = 1
        self.alive_neighbour_count = 2
        self.end_state = process_rules(self.current_cell_value, self.alive_neighbour_count)
        self.assertEqual(self.end_state, 1)
        
    def alive_cell_still_alive_due_to_three_neighbours_test(self):
        self.current_cell_value = 1
        self.alive_neighbour_count = 3
        self.end_state = process_rules(self.current_cell_value, self.alive_neighbour_count)
        self.assertEqual(self.end_state, 1)
        
    def alive_cell_died_due_to_more_than_three_neighbours_test(self):
        self.current_cell_value = 1
        self.alive_neighbour_count = 4
        self.end_state = process_rules(self.current_cell_value, self.alive_neighbour_count)
        self.assertEqual(self.end_state, 0)
        
    def no_wrap_around_test_expected(self):
        self.current_cell = [0,3]
        alive_neightbour_count = count_alive_neighbours(self.wrap_test_universe, self.current_cell)
        self.assertEqual(alive_neightbour_count, 0)
    
    def no_wrap_around_test_not_expected(self):
        self.current_cell = [0,3]
        alive_neightbour_count = count_alive_neighbours(self.wrap_test_universe, self.current_cell)
        # 3 alive neghbours will be present if top wraps to bottom 
        self.assertNotEqual(alive_neightbour_count, 3)
        

    def process_cells_test(self):
        self.assertEqual(process_cells(self.universe), self.next_universe)