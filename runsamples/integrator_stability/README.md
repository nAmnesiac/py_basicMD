# /runsamples/integrator_stability/

## Shortly:
These output files were generated as part of a set of simulations to test the stability of Euler and velocity Verlet integration algorithms at various timesteps. 

## Simulation Files:
These are all simulations of systems of 100 atoms in a 100 by 100 by 100 angstorm box, each with mass of 30 AMU. Temperatures were generated using Maxwell-Boltzmann distribution at 300 degrees Kelvin. LJ 12-6 potential parameters were set as follows: sigma = 4 angstrom, epsilon = 1000 J/mol. Simulations trajectories were run for 15 picoseconds and each simulation outputted a PDB file (for visualization in VMD) and a text file with six columns of data. These columns are, respectively: Current Time (ps), Net System Energy (J/mol), Net Lennard-Jones Potential (J/mol), Net Kinetic Energy (J/mol), Instantaenous Temperature (K), and Instantaneous Pressure (Pa). 

Simulations were run at a variety of timesteps with one of two different integration algorithms. To determine the integration algorithm and timestep used to generate each file, see below.

*(For example, [id01.pdb](https://github.com/nAmnesiac/py_basicMD/blob/main/runsamples/integrator_stability/id01.pdb) and [id01.txt](https://github.com/nAmnesiac/py_basicMD/blob/main/runsamples/integrator_stability/id01.txt) were generated from the same simulated system, using 1 femtosecond integration timesteps and Euler integration algorithm)*

ID 01: Euler Integrator, 1 femtosecond timestep<br/>
ID 02: Euler Integrator, 2 femtosecond timestep<br/>
ID 03: Euler Integrator, 4 femtosecond timestep<br/>
ID 04: Euler Integrator, 8 femtosecond timestep<br/>
ID 05: Euler Integrator, 16 femtosecond timestep<br/>
ID 06: Velocity Verlet Integrator, 1 femtosecond timestep<br/>
ID 07: Velocity Verlet Integrator, 2 femtosecond timestep<br/>
ID 08: Velocity Verlet Integrator, 4 femtosecond timestep<br/>
ID 09: Velocity Verlet Integrator, 8 femtosecond timestep<br/>
ID 10: Velocity Verlet Integrator, 16 femtosecond timestep<br/>
