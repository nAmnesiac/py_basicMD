# /runsamples/pressure_temperature/

## Shortly:
These output files were generated as part of a set of simulations to test the temperature-pressure relationship of systems simulated with a Berendsen thermostat in comparison to ideal gas.

## Simulation Files:
These are all simulations of systems of 300 atoms in a 120 by 120 by 120 angstorm box, each with mass of 30 AMU. LJ 12-6 potential parameters were set as follows: sigma = 4 angstrom, epsilon = 1000 J/mol. The system was affected by a Berendsen thermostat with a coupling constant with a unit of 50 timesteps. Simulations trajectories were run for 10 picoseconds with a 2 femtosecond timestep and each simulation outputted a PDB file (for visualization in VMD) and a text file with six columns of data. These columns are, respectively: Current Time (ps), Net System Energy (J/mol), Net Lennard-Jones Potential (J/mol), Net Kinetic Energy (J/mol), Instantaenous Temperature (K), and Instantaneous Pressure (Pa). 

Temperature used for generation of inital velocities via Maxwell-Boltzmann distribution and thermostat target temperature were the same, though this temperature varied between simulated systems. To determind the target system temperature for each file, see below. 

*(For example, [id01.pdb](https://github.com/nAmnesiac/py_basicMD/blob/main/runsamples/pressure_temperature/id01.pdb) and [id01.txt](https://github.com/nAmnesiac/py_basicMD/blob/main/runsamples/pressure_temperature/id01.txt) were generated from the same simulated system, using 200 degrees kelvin as target temperature)*




ID 01: 200 Kelvin <br/>
ID 02: 225 Kelvin <br/>
ID 03: 250 Kelvin <br/>
ID 04: 275 Kelvin <br/>
ID 05: 300 Kelvin <br/>
ID 06: 325 Kelvin <br/>
ID 07: 350 Kelvin <br/>
ID 08: 375 Kelvin <br/>
ID 09: 400 Kelvin
