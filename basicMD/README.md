# /basicMD/
# This is a tutorial for running ideal and Lennard-Jones gas simulations

## Running Script:
   [LJmd_euler.py](https://github.com/nAmnesiac/py_basicMD/blob/main/basicMD/LJmd_euler.py) simulates Lennard-Jones gas particles using Euler integration

   [LJmd_velocityverlet.py](https://github.com/nAmnesiac/py_basicMD/blob/main/basicMD/LJmd_velocityverlet.py) simulates Lennard-Jones gas particles using velocity Verlet integration

   [IDEALmd_euler.py](https://github.com/nAmnesiac/py_basicMD/blob/main/basicMD/IDEALmd_euler.py) simulates ideal gas particles using Euler integration

## Run Function:

Simulation can be run using the "run" function and calling three necessary arguments: Integration Steps per Group, Integration Timestep (ps), and Number of Groups. MD smulation and integration is done every timestep, but data and particle coordinates are only outputted at the end of each group. 

For example, "run(10, 0.001, 1000)" would simulate a system integrating with 0.001 picosecond timesteps, outputting data every ten steps (0.01 ps) and running for a total of 10 picoseconds. 

   **Usage:** Simulation parameters can be modified by following in-file documentation. Simulation will ouput to a PDB file for visualization in VMD and data will be stored in a text file.  

   **Note**: Script is based on Python 3 and *NumPy* library is necessary.
