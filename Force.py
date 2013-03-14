import numpy as np
import math


class Force(object):

    def __init__(self, c):
        self.c = c

    def pe(self):
        # TODO: return potential energy
        pass

    def ke(self):
        # TODO: return kinetic energy
        pass

    def pressure(self):
        # TODO: return kinetic energy
        pass

    def ax(self):
        eps = 1.0
        sig = 1.0
        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr = self.c.dr()

        r_mag = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)
        x_hat = dx / r_mag
        x_hat = np.nan_to_num(x_hat)

        #print "r_mag"
        #print r_mag

        #print "x_hat"
        #print x_hat

        ax = ((24 * eps) / r_mag * (2 * (sig / r_mag) ** 12 - (sig / r_mag) ** 6)) * x_hat
        ax = np.nan_to_num(ax)

        ax = -ax
        #force = r_hat * (24*eps)/r_mag * (2*(sig/r_mag)**12 - (sig/r_mag)**6)
        #print "ax: "
        #print np.sum(ax, axis=1)
        return np.sum(ax, axis=1)

    def ay(self):
        eps = 1.0
        sig = 1.0
        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr = self.c.dr()

        r_mag = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)
        y_hat = dy / r_mag
        y_hat = np.nan_to_num(y_hat)

        #print "r_mag"
        #print r_mag

        #print "y_hat"
        #print y_hat

        ay = y_hat * ((24 * eps) / r_mag * (2 * (sig / r_mag) ** 12 - (sig / r_mag) ** 6))
        ay = np.nan_to_num(ay)

        ay = -ay

        #force = r_hat * (24*eps)/r_mag * (2*(sig/r_mag)**12 - (sig/r_mag)**6)
        #print "ay: "
        #print np.sum(ay, axis=1)
        return np.sum(ay, axis=1)

    def az(self):
        eps = 1.0
        sig = 1.0
        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr = self.c.dr()

        r_mag = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)
        z_hat = dz / r_mag
        z_hat = np.nan_to_num(z_hat)

        #print "r_mag"
        #print r_mag

        #print "z_hat"
        #print z_hat

        az = z_hat * ((24 * eps) / r_mag * (2 * (sig / r_mag) ** 12 - (sig / r_mag) ** 6))
        az = np.nan_to_num(az)

        az = -az
        #force = r_hat * (24*eps)/r_mag * (2*(sig/r_mag)**12 - (sig/r_mag)**6)
        #print "az: "
        #print np.sum(az, axis=1)
        return np.sum(az, axis=1)