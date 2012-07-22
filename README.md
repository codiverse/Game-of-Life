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

	# Run with defaults - 50 generations, no detailed grid (only alive cells)
	game_of_life.py
	
	# Run for 200 generations, no detailed grid
	game_of_life.py -g 200
	
	# Run for 200 generations, show full grid 
	game_of_life.py -g 200 -s 
