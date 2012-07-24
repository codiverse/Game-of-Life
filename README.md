# Conway's Game of Life

http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

This is an implementation of Conway's game of life in Python.

An early Python project for myself, experimenting with building something from scratch.


## Example Grid Layouts

There are two example grid layouts provided, one is a simple oscillator that is also used in the tests,
the other (default) is the Gosper Glider Gun which is a fair bit more interesting to watch :-)

## Usage

	# Usage
	game_of_life.py -h
	
	Usage: game_of_life.py [options]

	Options:
  		-h, --help 			show this help message and exit
  		-g GENERATIONS, --generations=GENERATIONS
							Number of Generations to run for
  		-s, --showgrid 		Specify whether to show detailed universe grid
  		-r RANDOM_SIZE, --randomsize=RANDOM_SIZE
							Build a random Universe of this grid size
  		-t TIME_TICK, --timetick=TIME_TICK
							The time interval of generations, in seconds
  		-c CHARACTER, --character=CHARACTER
							Character used to display a living cell

	# Run with defaults - 50 generations, no detailed grid (only alive cells), # alive cell display character
	game_of_life.py
	
	# Run for 200 generations, no detailed grid
	game_of_life.py -g 200
	
	# Run for 200 generations, show full grid 
	game_of_life.py -g 200 -s
	
	# Run with a randomised Universe of 40x40 cells  
	game_of_life.py -r 40
	
	# Run for 50 generations, with 0.5 seconds per generation
	game_of_life.py -t 0.5
	
	# Run with a custom alive cell display character
	game_of_life.py -c .
