import numpy as np


class Container(object):

    def __init__(self):
        self._x = np.array([])
        self._y = np.array([])
        self._z = np.array([])

        self.vx = np.array([])
        self.vy = np.array([])
        self.vz = np.array([])

        self.ax = np.array([])
        self.ay = np.array([])
        self.az = np.array([])

        self.Lx = 0.
        self.Ly = 0.
        self.Lz = 0.

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x_prime):
        self._x = x_prime % self.Lx

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y_prime):
        self._y = y_prime % self.Ly

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z_prime):
        #self._z = z_prime % self.Lz
        self._z = z_prime

    def add_particle(self, x, y, z, vx, vy, vz):
        self.x = np.hstack((self.x, x))
        print "x: "
        print self.x
        self.y = np.hstack((self.y, y))
        self.z = np.hstack((self.z, z))

        self.vx = np.hstack((self.vx, vx))
        self.vy = np.hstack((self.vy, vy))
        self.vz = np.hstack((self.vz, vz))
        #self.vx = vx
        #self.vy = vy
        #self.vz = vz

    def dx(self):
        #print "x: "
        #print self.x
        xtemp = np.tile(self.x, (self.x.size,1))
        #print "xtemp"
        #print xtemp
        dx = xtemp - xtemp.T
        dx[dx > self.Lx / 2.] -= self.Lx
        dx[dx < -self.Lx / 2.] += self.Lx
        #print "dx"
        #print dx
        return dx

    def dy(self):
        ytemp = np.tile(self.y, (self.y.size, 1))
        dy = ytemp - ytemp.T
        dy[dy > self.Ly / 2.] -= self.Ly
        dy[dy < -self.Ly / 2.] += self.Ly
        return dy

    def dz(self):
        ztemp = np.tile(self.z, (self.z.size, 1))
        dz = ztemp - ztemp.T
        dz[dz > self.Lz / 2.] -= self.Lz
        dz[dz < -self.Lz / 2.] += self.Lz
        return dz

    def dr(self):
        # TODO: return dr here
        pass