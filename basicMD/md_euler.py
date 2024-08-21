#======IMPORTING LIBRARIES===================================================#

import math
import numpy as np
import sys
import random
import os.path
#======END===================================================================#



#======MD PARAMETERS (VALUES CAN BE MODIFIED)================================#
numberofatoms = 300
#number of particles used to simulate

boxsize = [120, 120, 120] 
#boxsize for x, y, z dimensions in Angstrom

mass = 0.03
#mass of particles in kilograms/mol

temperature = 300 
#temperature in kelvin used to generate initial
#particle velocities using Maxwell-Boltzmann distribution

elipson = 1000. 
#strength of Lennard Jones interaction in Joules/mol
#(depth of potential well/minimum potential energy)

sigma = 4. 
#distance where Lennard Jones potential energy is zero in Angstrom

tau = 50
#Coupling constant for Berendsen thermostat in unit of integration timestep

thermostattemp = 300
#External Berendsen thermostat heat bath temperature in Kelvin
#======END===================================================================#



#======GLOBAL VARIABLES TO STORE ONGOING VALUES==============================#
ljenergy = 0        # instantaneous total Lennard Jones potential in Joules/mol
currenttime = 0     # time elapsed during simulation in picoseconds
kenergy = 0         # instantaneous total kinetic energy in Joules/mol
ctemperature = 0    # instantaneous temperature of system in Kelvin
cpressure = 0       # instantaneous pressure of system in Pascals
#======END===================================================================#



#======MD PARTICLE INITALIZATION================================================#
#Particles generated at random coordinates within box (Angstrom)
coords = np.hstack((np.random.uniform(0.0, boxsize[0], (numberofatoms, 1)),
                    np.random.uniform(0.0, boxsize[1], (numberofatoms, 1)),
                    np.random.uniform(0.0, boxsize[2], (numberofatoms, 1))))

#Particles evenly distributed throughout box using uniform grid
#to minimize steric clash of particles (Angstrom)
gengridsize = math.ceil(numberofatoms**(1/3))
genatomindex = 0
for xed in range(gengridsize):
    currentx = (xed) * (boxsize[0]/gengridsize)
    for yed in range(gengridsize):
        currenty = (yed) * (boxsize[1]/gengridsize)
        for zed in range(gengridsize):
            currentz = (zed) * (boxsize[2]/gengridsize)
            coords[genatomindex, 0] = currentx
            coords[genatomindex, 1] = currenty
            coords[genatomindex, 2] = currentz
            genatomindex += 1
            if genatomindex >= numberofatoms: break
        if genatomindex >= numberofatoms: break
    if genatomindex >= numberofatoms: break

#Velocity array in x, y, z dimensions generated using
#Maxwell-Boltzmann distribution in Angstrom/picoseconds
velocity = 0.01 * math.sqrt((8.314*temperature)/(mass))*(np.random.normal(0, 1, (numberofatoms, 3)))

#Force array in x, y, z dimensions in (kg*angstrom)/(mol*ps*ps)
force = np.zeros((numberofatoms, 3))
#======END===================================================================#



#======NESTED INTEGRATION FUNCTIONS==========================================#
#Appends to (or creates if file does not exist) "pdb_file.pdb"
#with new model with current particle coordinates in pdb format
#Function arguments can optionally be modified
def outputpdb(model = 1, atom="ATOM", name="", alt_indicator="", resname="", chainid="", res_seqnum="", rescode=""):
    output = open("pdb_file.pdb", "a")
    output.write("MODEL     %4d\n" % model)
    for serialnumber in range(0, numberofatoms):
        output.write("%-6s%5d %-4s%1s%3s %1s%4s%1s   %8.3f%8.3f%8.3f\n" % \
                     (atom, serialnumber + 1, name, alt_indicator, resname, chainid, res_seqnum, rescode, \
                      coords[serialnumber, 0], coords[serialnumber, 1], coords[serialnumber, 2]))
    output.write("ENDMDL\n")
    output.close()

#Appends to (or creates if file does not exist) "data_file.txt"
#with six 9 character columns of data separated by two spaces each
#outputted data respectively:
#Time(ps), Net System Energy(J/mol), Net Lennard Jones Potential(J/mol),
#Net Kinetic Energy(J/mol), Instantaneous Temperature(K), Instantaneous Pressure(Pa)
def outputdata(ctime):
    global ctemperature
    global cpressure
    output = open("data_file.txt", "a")
    output.write("%-.9e  %-.9e  %-.9e  %-.9e  %-.9e  %-.9e\n" % \
                 ((ctime), (ljenergy+kenergy), ljenergy, kenergy, ctemperature, cpressure))

#Only run at beginning of simulation
#Renames any existing "pdb_file.pdb" files to "pdb_backup??.pdb" where
#?? is the smallest avaliable number
def clearpdb():
    if os.path.exists("pdb_file.pdb"):
        backupnumber = 1
        while os.path.exists("pdb_backup%d.pdb" % (backupnumber)) == True:
            backupnumber += 1
        os.system("cp pdb_file.pdb pdb_backup%d.pdb" % (backupnumber))
        os.system("rm pdb_file.pdb")

#Only run at beginning of simulation
#Renames any existing "data_file.txt" files to "data_backup??.txt" where
#?? is the smallest avaliable number
def cleardata():
    if os.path.exists("data_file.txt"):
        backupnumber = 1
        while os.path.exists("data_backup%d.txt" % (backupnumber)) == True:
            backupnumber += 1
        os.system("cp data_file.txt data_backup%d.txt" % (backupnumber))
        os.system("rm data_file.txt")

#Updates global force array for every particle within a cutoff
    #distance (default 25 angstrom) using Lennard Jones 12-6
    #Cutoff distance can be modified or removed
#Calculates net Lennard Jones Potential and updates global "ljenergy"
#Calculates net Kinetic Energy and updates global "kenergy"
def cforceenergy():
    global force
    global ljenergy
    global kenergy
    force[:,:] = 0
    ljenergy = 0
    for a1 in range(0, numberofatoms-1):
        for a2 in range(a1 + 1, numberofatoms):
                x1 = coords[a1, 0]
                x2 = coords[a2, 0]
                y1 = coords[a1, 1]
                y2 = coords[a2, 1]
                z1 = coords[a1, 2]
                z2 = coords[a2, 2]
                r = math.sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 ) 

                if r > 25: continue #LENNARD JONES CUTOFF DISTANCE (Angstrom)
                
                otherblock = ( ((2*(sigma**12))/(r**13)) - (sigma**6)/(r**7) )
                xforce = 0.0024 * elipson * otherblock * \
                                 ( (x2-x1)/(r) ) 
                force[a2, 0] += xforce
                force[a1, 0] += xforce * -1
                yforce = 0.0024 * elipson * otherblock * \
                                 ( (y2-y1)/(r) ) 
                force[a2, 1] += yforce
                force[a1, 1] += yforce * -1
                zforce = 0.0024 * elipson * otherblock * \
                                 ( (z2-z1)/(r) ) 
                force[a2, 2] += zforce
                force[a1, 2] += zforce * -1
                
                ljenergy += 4 * elipson * ( ((sigma/r)**12) - ((sigma/r)**6))
                                            
    kenergy = 0
    for atom in range(0, numberofatoms):
        netvelocity = math.sqrt(velocity[atom,0]*velocity[atom,0] +\
                                velocity[atom,1]*velocity[atom,1] + \
                                velocity[atom,2]*velocity[atom,2])
        kenergy += 5000 * mass * (netvelocity*netvelocity) #Joules/mol


#Checks for particles that have exceeded the bounds of the box and
#modifies them to have appropriate positions and velociites
def checkbounds():
    global coords
    global velocity
    for atom in range(0, numberofatoms):
        for axis in range(0, 3):
            if coords[atom, axis] >= boxsize[axis]:
                coords[atom, axis] = (2 * boxsize[axis]) - coords[atom, axis]
                velocity[atom, axis] = -1 * velocity[atom, axis]
            elif coords[atom, axis] <= 0:
                coords[atom, axis] = -1 * coords[atom, axis]
                velocity[atom, axis] = -1 * velocity[atom, axis]

#Calculates instantaneous pressure and updates global "cpressure"
def pressure():
    global cpressure
    firsthalf = (1.380649)*(numberofatoms)*(ctemperature)*((10**7)/((boxsize[0]*boxsize[1]*boxsize[2])))
    secondhalf = 0
    for atom in range(numberofatoms):
        for axis in range(3):
            secondhalf += coords[atom, axis] * force[atom, axis] * 10**4
    cpressure = firsthalf + secondhalf * (10**7/(3*(boxsize[0]*boxsize[1]*boxsize[2]))) * (1/6.023)

#Updates particle velocites based on force array and updates
#particle coordinates based on velocity array using Euler integration
def run_euler(rounds, timestep):
    global force
    global velocity
    global coords
    for x in range(rounds):
        cforceenergy()
        velocity += force/mass * timestep
        coords += velocity * timestep
        checkbounds()
#======END===================================================================#


                    
#====== MD INTEGRATOR =======================================================#
#Runs simulation using an integration timestep of "timestep"

#Simulation outputs to data and pdb files at the end of each group,
#for "groups" number of groups and "roundspergroup" integration steps
#in each group

#To run simulation with Berendsen thermostat off, remove/comment indicated
#thermostat line below

#Simulation prints basic output data after each group while running.
        
def run(roundspergroup, timestep, groups):
    global velocity
    global ctemperature
    global tau
    global thermostattemp
    clearpdb()
    cleardata()
    currenttime=0
    for x in range(groups):
        currenttime+=timestep*roundspergroup
        run_euler(roundspergroup, timestep)
        ctemperature = kenergy * (2/3) * (1/8.314) * (1/numberofatoms)
        velocity = velocity * math.sqrt( (1/tau)*((thermostattemp/ctemperature)-1) + 1 ) #THERMOSTAT LINE
        outputpdb()
        pressure()
        outputdata(currenttime)
        print("Time: %.3e  |  TotalEnergy: %.3e  |  KEnergy: %.3e  |  LJEnergy: %.3e  |  Temp: %.3e  |  Pressure: %.3e" % \
              (currenttime, ljenergy+kenergy, kenergy, ljenergy, ctemperature, cpressure))

                    

        




    
