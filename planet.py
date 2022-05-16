# John Idarraga, 2022
# Simple integrator example for OOP training

import matplotlib.pyplot as plt
import numpy as np

class Planet:
    def __init__(self, name, mass, xpos, ypos, xvel, yvel) -> None:
        self.__name = name
        self.__mass = mass
        self.__xpos = xpos
        self.__ypos = ypos
        self.__xvel = xvel
        self.__yvel = yvel
    def __del__(self):
        pass

    def dump(self, kinematics=False):
        print("Object: (%s) Mass = %s Jupiter masses"%(self.__name, self.__mass))
        if kinematics: print("        (x,y): (%s,%s) | (vx,vy): (%s,%s)"%(self.__xpos, self.__ypos, self.__xvel, self.__yvel))

    def printPosition(self):
        print("[%s]  (x,y): (%s,%s) | (vx,vy): (%s,%s)"%(self.__name, self.__xpos, self.__ypos, self.__xvel, self.__yvel))

    def getName(self):
        return self.__name
    def getMass(self):
        return self.__mass
    def getX(self):
        return self.__xpos
    def getY(self):
        return self.__ypos
    def getForceX(self):
        return self.__fx
    def getForceY(self):
        return self.__fy

    # private
    __name = ""
    __mass = 0.
    __xpos = 0.
    __ypos = 0.
    __xvel = 0.
    __yvel = 0.
    __fx = 0.
    __fy = 0.

    def getDistance(self, otherPlanet) -> float:
        xdelta = otherPlanet.getX() - self.__xpos
        ydelta = otherPlanet.getY() - self.__ypos
        return np.sqrt(xdelta**2 + ydelta**2)

    def zeroForce(self):
        self.__fx = 0.
        self.__fy = 0.

    def euler_method(self, delta_t):
        self.__xvel = self.__xvel + (self.__fx*delta_t/self.__mass)
        self.__yvel = self.__yvel + (self.__fy*delta_t/self.__mass)
        self.__xpos = self.__xpos + self.__xvel*delta_t
        self.__ypos = self.__ypos + self.__yvel*delta_t

    # calc force on self due to otherPlanet
    def calcForce(self, otherPlanet):

        dist = self.getDistance(otherPlanet)
        distX = self.getX() - otherPlanet.getX() 
        distY = self.getY() - otherPlanet.getY()

        #print("calcForce on the %s due to %s | dX=%s dY=%s d=%s"%(self.__name, otherPlanet.getName(), distX, distY, dist))

        # The cuadrant is naturally selected here
        cos_theta = distX/dist
        sin_theta = distY/dist

        self.__fx += -1.*cos_theta*GRAV_CNST * self.__mass * otherPlanet.getMass() / dist**2
        self.__fy += -1.*sin_theta*GRAV_CNST * self.__mass * otherPlanet.getMass() / dist**2

# Initial conditions
# All masses in Jupiter masses.
# Positions in astronomical units.
# Time in Earth hours
# Gravitational constant in AU/(Jm*eh)
GRAV_CNST = 4.904099987329075e-10

# Sun
sun = Planet("Sun", 1047, 0, 0, 0, 0)
sun.dump(True)

# Jupiter mass = 1,898 × 10^27 kg
# Orbital Velocity 13.06 km/s --> AU/earth_hour
jupiter = Planet("Jupiter", 1, 5.2, 0, 0, 0.00031428227650102275)
jupiter.dump(True)

# Earth mass 5,972 × 10^24 kg
# Orbital Velocity 29.78 km/s --> AU/earth_hour
earth = Planet("Earth", 0.00314647, 1, 0, 0, 0.0007166405967994224)
earth.dump(True)

# My solar system
solarSystem = [sun, jupiter, earth]

# Integration controls. Time in earth hours
t_start = 0.0
t_stop = 100000
t_num = 1000
delta_t = float((t_stop - t_start)/t_num)
time_vector = np.linspace(t_start, t_stop, t_num)

# Plotting
plot_vectors = { 
    jupiter : ([],[]),
    earth: ([],[])
}
print("--- Start integration: delta_t = %s"%delta_t)
for t in time_vector:
     for idx, planet_pivot in enumerate(solarSystem):
        print("--- %s ---- t: %s ---------"%(planet_pivot.getName(),t))
        planet_pivot.zeroForce()
        for idx2, planet_force in enumerate(solarSystem):
            if (idx != idx2) :
                planet_pivot.calcForce(planet_force)
                # with all forces ready then integrate
        #print("  fx, fy : %s, %s"%(round(planet_pivot.getForceX(), 2), round(planet_pivot.getForceY(), 2)))
        planet_pivot.euler_method(delta_t)
        if ( "Jupiter" in planet_pivot.getName() ):
            planet_pivot.printPosition()
            plot_vectors[jupiter][0].append( planet_pivot.getX() )
            plot_vectors[jupiter][1].append( planet_pivot.getY() )
        if ( "Earth" in planet_pivot.getName() ):
            planet_pivot.printPosition()
            plot_vectors[earth][0].append( planet_pivot.getX() )
            plot_vectors[earth][1].append( planet_pivot.getY() )

earth_years = (t_stop-t_start)/(24*365);
jupiter_years = earth_years/11.86;
print("[DONE] Simulated: %s Earth years | %s Jupiter years "%(round(earth_years, 2), round(jupiter_years,2)))
print("       Integration step: delta_t = %s Earth hours"%delta_t)

#x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(plot_vectors[jupiter][0], plot_vectors[jupiter][1], s=1, c='b', marker="s", label='Jupiter')  # Plot the sine of each x point
ax1.scatter(plot_vectors[earth][0], plot_vectors[earth][1], s=1, c='r', marker="o", label='Earth')  # Plot the sine of each x point
plt.legend(loc='upper left')
plt.show()
