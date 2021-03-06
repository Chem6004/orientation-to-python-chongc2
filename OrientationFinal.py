# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
'''
import turtle


turtle.shape("turtle")
turtle.left(45)
turtle.position()
(0.00,0.00)
turtle.forward(50)
turtle.color("green")
turtle.right(50)
turtle.circle(125,350)
turtle.home()
big=("Arial", 20, "normal")
turtle.penup()
turtle.goto(-40,150)
turtle.write("Hello Friend!", font=big)
turtle.goto(-40,100)
turtle.write("Welcome to my home", font=big)

turtle.home()
turtle.back(10)
turtle.exitonclick()

'''
#number of particles assigned can be varied
#assignment is to chose 5 different N values
Npart = 10
Npart_array = [10,20,30,40,50,1000]
KE_array = [31.25,62.5, 93.75, 125.0,156.25, 3125.0]
PE_array = [192.89682539682542,519.547931428736,898.4961392761172,
            1311.4172155745546,1749.602669164726, 64854.70860551561]
Npart_array1 = [10,20,30,40,50]
Time_array = [0.3112938404083252,0.31322407722473145, 0.3245081901550293, 
              0.3370239734649658,0.3811812400817871]



#creation of an array "m" and "v" to store the masses and velocities of the 10 particles
# each entry will start as zero and later adjusted 


#create empty lists for each quantity
m = np.zeros(Npart)
v = np.zeros(Npart)


for i in range(0,Npart):
    m[i] = 1.0
    v[i] = 2.5
print(m)




## i will be the syntax in our loop and will represent the range from (0,Npart) of the loop. 
## now we can use i to continue our code.

    
print("Printing array of masses:",m)
print("Printing array of velocities:",v)

#now we can input the formula for kinetic energies of each ith particle

T = 1/2 * m[i] * v[i]**2

print(T)

## initialize a sym variable to zero
T_tot_loop = 0
#loop over elements of the T array and compute the sum

for i in range(0,Npart):
    T_tot_loop = T_tot_loop + T
    
# or you can try another method by using np.sum which will be shown in the code below
# both entries shoul give you the same number

#T_tot_sum = np.sum(T)

print("Result from kinetic energy is ",T_tot_loop)
#print(result from kinetic energy is",T_tot_sum)

#consider potnetial energy
#x_i will considee the position of the particle i
#x_j will consider position of particle j
#tot potential energy will be a sum over the potential energy for each particle
#We need to compute two nested sums to get the tot potential energy

##we need charge of particle, separation between each particle pair
#to store separations between particle pairs we need to use 2-D array

### create 1-D arrays of length Npart for q... assign each particle charge of 1 natural unit
q = np.ones(Npart)

### create a 1-D array of length Npart for x... use np.linspace to automatically
### assign values since we want the particles evenly spaced.
# for our purposes np.linspace(start,stop,num)
## stop will be reduced by 1(charge) and mulitplied by 0.2(separation)

x = np.linspace(0,(Npart-1)*0.2,Npart)

#not to sure what a 2D array is.

## create a 2-D array that is Npart x Npart for the separations between particle pairs
r = np.zeros((Npart,Npart))

### compute all separations using two nested for-loops to access the positions of each particle
for i in range(0,Npart):
    for j in range(0,Npart):
        r[i][j] = np.sqrt( (x[i]-x[j])**2 )

### now print all arrays 
print("Printing array of charges ",q)
print("Printing array of charges ",x)
print("Printing array of charges \n",r)

### function to compute potential energy given an array of separations and an array of charges
def Potential(sep_array, charge_array):
    ### presumably the number of particles is equal to the length
    ### of the array of charges
    N = len(charge_array)
    
    ### initialize the potential energy to zer
    Pot = 0.
    ### nested loop
    for i in range(0,N):
        for j in range(0,N):
            ### do not calculate potential of particle with itself!
            if (i!=j):
                Pot = Pot + charge_array[i]*charge_array[j]/sep_array[i][j]
    return Pot
print("potential energy", Potential)
## Compute total potential energy and store it as the variable V_tot
V_tot = Potential(r, q)

### print it to see what it is!
print(V_tot)

### import time library
import time
### import pyplot as library
from matplotlib import pyplot as plt

### get the time at the beginning of the program
start = time.time()
### create an array of
x1 = Npart_array
### create an array of y-values 
y1 = KE_array

x2 = Npart_array
y2 = PE_array

### plot y = x^2 with a red line!
plt.plot(x1, y1, 'blue')
plt.plot(x1,y1, label = "kinetic")

plt.plot(x2, y2, 'red')
plt.plot(x2,y2, label = "potential")

plt.xlabel('Number of Particles')
plt.ylabel('Kinetic and Potential Energy')
plt.title('Kinetic and Potential vs # particles')
plt.savefig("test.png")
plt.ylim(0,70000) 
plt.xlim(10,1000)
plt.legend()
plt.show()

### figure out how much time this whole program took to run!
end = time.time()
how_long = end - start
### print the total time taken in seconds
print("Hi Dr.Foley, my answers for the following questions are in this code")
print("Kinetic Energy scales linearly")
print("Potential Energy scales quadratically")

#print("Total time to run in seconds is: ",how_long)

### import time library
import time
### import pyplot as library
from matplotlib import pyplot as plt

### get the time at the beginning of the program
##start = time.time()

x = Npart_array1
y = Time_array

plt.plot(x, y, 'b--o')
plt.plot(x,y, label = "Time")
plt.xlabel('Number of Particles')
plt.ylabel('Time (s)')
plt.title('Time Taken in relation to # of particles')
plt.legend()
plt.show()
