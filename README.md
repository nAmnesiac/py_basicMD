# py_basicMD Molecular Dynamics Engine in Python
[*basicMD*](https://github.com/nAmnesiac/py_basicMD/tree/main/basicMD): setup and script for running simulation <br/>
[*learnhere*](https://github.com/nAmnesiac/py_basicMD/tree/main/learnhere): report and data analysis <br/>
[*runsamples*](https://github.com/nAmnesiac/py_basicMD/tree/main/runsamples): sample simulation output files

# Project Introduction
The purpose of this project was to implement a simple molecular dynamics (MD) engine using Python for simulating ideal and Lennard-Jones gas in a fixed box. The engine was constructed from scratch using Python, and then used to assess Euler and velocity Verlet integration algorithms and the effects of various simulation parameters upon long-term stability of the simulation, as well as the pressure-temperature relationship and Lennard-Jones gas deviation from ideal gas under various temperatures. Additionally, construction of this engine served as an impactful learning experience in molecular dynamics simulation and computation. By analyzing the average net system energy, it was concluded that both integration algorithms were able to conserve system energy with fluctuations and drift on the same order of magnitude. Additionally, pressure and temperature increased with a linear relationship which better modeled ideal gas at higher temperatures, which is the expected behavior and indicates that the model functions as a relatively accurate tool for simulating simple gases. 

## Shortly
This is a basic molecular dynamics (MD) engine for simulating ideal and Lennard-Jones gas in a fixed box. This MD engine can simulate using Euler or velocity Verlet integration algorithms and adjust temperature using a Berendsen thermostat. Lennard-Jones gas is modeled with Lennard-Jones 12-6 potential. While simulating, this MD engine outputs data to a text file and records particle positions in Protein Data Bank format. 

For running a MD simulation, follow [README.md](https://github.com/nAmnesiac/py_basicMD/blob/main/basicMD/README.md) in [basicMD](https://github.com/nAmnesiac/py_basicMD/tree/main/basicMD) for instructions.

For detailed report of MD engine functionality and analysis of simulation data, see [README.md](https://github.com/nAmnesiac/py_basicMD/blob/main/learnhere/README.md) in [learnhere](https://github.com/nAmnesiac/py_basicMD/tree/main/learnhere).

For sample simulation data used in MD engine report, see [README.md](https://github.com/nAmnesiac/py_basicMD/blob/main/runsamples/README.md) in [runsamples](https://github.com/nAmnesiac/py_basicMD/tree/main/runsamples).</br></br></br>

Allen Chen, <i>Northfield Mount Hermon & University of Massachusetts Amherst</i>
**Contact:** allen.m.chen07@gmail.com
