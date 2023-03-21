# cell-duplication
simulator of random time cell duplication

To run the code matplotlib and scipy should be installed

Distribution in [stochastic simulation](https://github.com/margogeo/cell-duplication/blob/main/cells.py) can be changed in line 17 to on of the others available [here](https://docs.python.org/3/library/random.html#random.betavariate)

[Deterministic simulation](https://github.com/margogeo/cell-duplication/blob/main/determCells.py) allows to track the number of cells for much longer because we don't store every cell and time complexity depends on number of minutes, not on number of cells

Comparison of approaches:
- Max duration of tracking: ~1500 minutes for stochastic simulation, ~75000 minutes for deterministic simulation(the number of cells exceeds number of atoms in the universe after 20000 minutes)
- Given the same time period(1000 minutes) stochastic simulation result vary from 6000 to 20000 cells, deterministic simulation result is ~8500 cells

----------------

[Gillespie algorithm vs differential equation solution](https://github.com/margogeo/cell-duplication/blob/main/Gillespie.py)
This version of G. algorithm can be applied to a model of 1 or 2 components(reaction propensities can be changed). It returns a plot with multiple trajections, its mean and a mean value from differential equation for one component.

![image](https://user-images.githubusercontent.com/70298122/226743785-cdcbfc38-d60f-41fd-b4a4-f8f3a855413a.png)
(blue lines are trajectories, red line is a mean of trajectories, yellow is value of m at which growth and descending processes balance)
