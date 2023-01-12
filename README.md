# cell-duplication
simulator of random time cell duplication

To run the code matplotlib should be installed

Distribution in [stochastic simulation](https://github.com/margogeo/cell-duplication/blob/main/cells.py) can be changed in line 17 to on of the others available [here](https://docs.python.org/3/library/random.html#random.betavariate)

[Deterministic simulation](https://github.com/margogeo/cell-duplication/blob/main/determCells.py) allows to track the number of cells for much longer because we don't store every cell and time complexity depends on number of minutes, not on number of cells

Comparison of approaches:
- Max duration of tracking: ~1500 minutes for stochastic simulation, ~75000 minutes for deterministic simulation(the number of cells exceeds number of atoms in the universe after 20000 minutes)
- Given the same time period(1000 minutes) stochastic simulation result vary from 6000 to 20000 cells, deterministic simulation result is ~8500 cells

