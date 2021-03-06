import Container
import Force
import Integrator
import ContainerInitializer

import numpy as np
import matplotlib.pyplot as plt

FRAME_RATE = 10
DELTA_T = 0.01
NUM_TIMESTEPS = 500


def circle( xy, radius, color="lightsteelblue", facecolor="green", alpha=.6, ax=None ):

    e = plt.Circle( xy=xy, radius=radius )
    if ax is None:
        ax = plt.gca()
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_edgecolor( color )
    e.set_linewidth(3)
    e.set_facecolor( facecolor )
    e.set_alpha( alpha )

c = ContainerInitializer.ContainerInitializer("prob3").getContainer()
f = Force.Force(c)
i = Integrator.Integrator(DELTA_T, f)

state_list = []
pe_list = []
ke_list = []
pressure_list = []
count = 0

plt.figure(1)
plt.clf()
plt.ion()
plt.xlim((0, c.Lx))
plt.ylim((0, c.Ly))
plt.grid()
ax = plt.gca()
plt.show()

while count < NUM_TIMESTEPS:
    #print "--------- BEGIN TIMESTEP " + str(count) + " --------------"
    i.integrate()
    pe_list.append(f.pe())
    ke_list.append(f.ke())
    pressure_list.append(f.pressure())
    #print "AX TIMESTEP " + str(count)
    #print c.ax

    #print "AY TIMESTEP " + str(count)
    #print c.ay

    #plt.plot(c.x, c.y)
    #plt.show()

    c.Lx -= 0.01
    c.Ly -= 0.01

    if count % FRAME_RATE == 0:
        #print "c.x"
        #print c.x
        #print "c.y"
        #print c.y


        for particle in range(c.x.size):
            part_x = 0.
            part_y = 0.
            circle((c.x[particle], c.y[particle]), radius = 0.5*2**(1/6.), ax=ax, facecolor='green')
        plt.draw()
            #particles[particle] = {"x": c.x[particle], "y": c.y[particle]}
            #plt.xlim((0, 10))
            #plt.ylim((0, 10))
            #plt.plot(c.x[particle], c.y[particle], 'o')
        #plt.show()

    count += 1

time = np.linspace(0, NUM_TIMESTEPS*DELTA_T, NUM_TIMESTEPS)

#print "time:"
#print time
#print "---------"
#print "pe_list:"

#print "len time: " + str(len(time))
#print "len pe_list " + str(len(pe_list))
#print pe_list

# Plot Potential Energy
plt.clf()
plt.plot(time, pe_list)
plt.ylabel('Potential Energy')
plt.title('Potential Energy Plot')
plt.xlabel('Time Units')
plt.savefig('prob3_pe.png')
plt.show(block=True)


# ke plot
plt.clf()
plt.plot(time, ke_list)
plt.xlabel('Time Units')
plt.ylabel('Kinetic Energy')
plt.title('Kinetic Energy Plot')
plt.savefig('prob3_ke.png')
plt.show(block=True)


# pressure plot
#plt.figure(2)
plt.clf()
plt.plot(time, pressure_list)
plt.xlabel('Time Units')
plt.ylabel('Pressure Relation')
plt.title('Pressure Relationship Plot')
plt.savefig('prob3_pressure.png')
plt.show(block=True)


