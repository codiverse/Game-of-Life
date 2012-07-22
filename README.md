# Conway's Game of Life

http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

This is an implementation of Conway's game of life in Python.

An early Python project for myself, experimenting with building something from scratch.


## Example Grid Layouts

There are two example grid layouts provided, one is a simple oscillator that is also used in the tests,
the other is the Gosper Glider Gun which is a fair bit more interesting to watch :-)

## Usage

	python game_of_life.py <number of generations to run for>
	eg.
	python game_of_life.py 200
	
If no number of generations is provided the default run is 10.

There is no sophistication to the argument parsing at present, so it will break easily.