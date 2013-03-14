import numpy as np
import Container
from math import sqrt
import math

class ContainerInitializer(object):


    def __init__(self, init_string):
        c = Container.Container()
        Lx = 10.
        Ly = 10.
        Lz = 0.
        dist = Lx / 5.
        vel = dist / 5.

        if init_string == 'one':
            c.Lx = Lx
            c.Ly = Ly
            c.Lz = Lz

            c.add_particle(0., dist, 0., 0., 0., 0.)

        elif init_string == 'two':
            c.Lx = Lx
            c.Ly = Ly
            c.Lz = Lz

            c.add_particle(1., 5., 0., 0.4, 0., 0.)
            c.add_particle(3., 5., 0., -0.4, 0., 0.)

        elif init_string == 'eight':
            lx = 10.
            ly = 10.
            dist = lx / 5.
            vel = dist / 5.
            #c.L = Vector_3D(10., 10., 0.)
            c.Lx = 10.
            c.Ly = 10.
            c.Lz = 0.
            c.add_particle(-dist+5,0.+5, 0., vel,0.,0.)
            c.add_particle(dist+5,0.+5,0., -vel,0.,0.)
            c.add_particle(0.+5,dist+5,0., 0.,-vel,0.)
            c.add_particle(0.+5,-dist+5,0., 0.,vel,0.)
            c.add_particle(dist/sqrt(2)+5,dist/sqrt(2)+5,0. , -vel/sqrt(2),-vel/sqrt(2),0.)
            c.add_particle(-dist/sqrt(2)+5,dist/sqrt(2)+5,0. , vel/sqrt(2),-vel/sqrt(2),0.)
            c.add_particle(-dist/sqrt(2)+5,-dist/sqrt(2)+5,0., vel/sqrt(2),vel/sqrt(2),0.)
            c.add_particle(dist/sqrt(2)+5,-dist/sqrt(2)+5,0., -vel/sqrt(2),vel/sqrt(2),0.)

        elif init_string == 'eight-zeros':
            lx = 10.
            ly = 10.
            dist = lx / 5.
            vel = dist / 5.
            #c.L = Vector_3D(10., 10., 0.)
            c.Lx = 10.
            c.Ly = 10.
            c.Lz = 0.
            c.add_particle(-dist+5,0.+5, 0., 0. ,0.,0.)
            c.add_particle(dist+5,0.+5,0., 0. , 0.,0.)
            c.add_particle(0.+5,dist+5,0., 0., 0. ,0.)
            c.add_particle(0.+5,-dist+5,0., 0.,vel,0.)
            c.add_particle(dist/sqrt(2)+5,dist/sqrt(2)+5,0. , 0., 0. , 0.)
            c.add_particle(-dist/sqrt(2)+5,dist/sqrt(2)+5,0. , 0., 0., 0.)
            c.add_particle(-dist/sqrt(2)+5,-dist/sqrt(2)+5,0., 0., 0., 0.)
            c.add_particle(dist/sqrt(2)+5,-dist/sqrt(2)+5,0., 0., 0. ,0.)

        elif init_string == 'square_lattice':
            N = 8             # Particles per row
            Lx = 9.
            Ly = Lx
            #c.Ly = c.Lx       # Extents determined by Lx input
            # TODO: set L
            #c.L = Vector_3D(30., 30., 0.)
            c.Lx = 9.
            c.Ly = 9.
            c.Lz = 0.
            d = 2.**(1/6.)    # Particle diameter
            x = np.linspace(d/2,Lx-d/2,N)
            y = np.linspace(d/2.,Lx-d/2,N)
            for i in range(x.size):
                for j in range(y.size):
                    c.add_particle(x[i],y[j],0., 0., 0., 0.)
                    #c.addParticle(x, y, z, vx, vy, ax, ay, mass)

        elif init_string == 'tri_lattice':
            Lx = 8.
            N = 8                       # particles per row
            Ly = sqrt(3) / 2. * Lx  # Set this based on Lx
            #c.L = Vector_3D(Lx, Ly, 0.)
            c.Lx = Lx
            c.Ly = Ly
            d = 2.**(1/6.)              # diameter
            x =  np.linspace(-c.Lx/2 + 3.*d/4.,c.Lx/2. - 1.*d/4., N) # Unstaggered
            xs = np.linspace(-c.Lx/2 + d/4.   ,c.Lx/2. - 3.*d/4., N) # Staggered
            y =  np.linspace(-c.Ly/2 + d/2.,c.Ly/2  - d/2, N)

            for i in range(N):
                for j in range(N):
                    if np.mod(i, 2)==0:
                        #c.addParticle(x[j],y[i],0,0,0,0,1)
                        c.add_particle(x[j], y[i], 0., 0., 0., 0.)
                    else:
                        #c.addParticle(xs[j],y[i],0,0,0,0,1)
                        c.add_particle(xs[j], y[i], 0., 0., 0., 0.)
        self.c = c


    def getContainer(self):
        return self.c



