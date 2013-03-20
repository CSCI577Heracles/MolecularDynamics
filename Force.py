import numpy as np
import math

XAXIS = 1
YAXIS = 2
ZAXIS = 3

class Force(object):

    def __init__(self, c):
        self.c = c

    def pe(self):
        eps = 1.
        sig = 1.

        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr2 = self.c.dr2()

        r_mag = (dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)

        rgBuild = (4 * eps) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        rgBuild = np.nan_to_num(rgBuild)
        #print "rgBuild:"
        #print np.sum(rgBuild)
        #print "-------------------"
        return np.sum(rgBuild)

    def ke(self):
        d = 2.
        N = np.size(self.c.x)
        vx = self.c.vx.copy()
        vy = self.c.vy.copy()
        vz = self.c.vz.copy()
        return 1 / ((N - 1) * d) * sum(vx ** 2 + vy ** 2 + vz ** 2)

    def pressure(self):
        ps = 1.
        sig = 1.
        eps = 1.
        d = 2.
        N = np.size(self.c.x)
        
        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr2 = self.c.dr2()
        
        r_mag = (dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)
        
        px = dx * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        px = np.nan_to_num(px)
        px = np.triu(px)
        py = dy * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        py = np.nan_to_num(py)
        py = np.triu(py)
        pz = dz * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        pz = np.nan_to_num(pz)
        pz = np.triu(pz)
        pt = px + py + pz
        return 1 / (d * N * self.ke()) * np.sum(pt)

    def aLJ(self, axis):
        eps = 1.0
        sig = 1.0
        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr2 = self.c.dr2()

        r_mag = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)
        
        if axis == XAXIS:
        	dvar = dx
        elif axis == YAXIS:
        	dvar = dy
        elif axis == ZAXIS:
        	dvar = dz
        dvar = np.nan_to_num(dvar)

		avar = dvar * (24 * eps) / dr2 * (2 * (sig ** 12 / dr2 ** 6) - (sig ** 6 / dr2 ** 3))
        avar = np.nan_to_num(avar)

        return np.sum(avar, axis=1) / self.c.m 

	# This force is only in the x - direction
	def aX(self, t):
		p = self.c.p[-1] 

        return 100 * (0.1 * t - (p.x - self.c.xInit)) / self.c.m[-1]
        
    # acceleration due to damping force
    def aD(self, axis):
    	
    	x = self.c.x[self.c.cFloor] 
    	y = self.c.y[self.c.cFloor]
    	z = self.c.z[self.c.cFloor]
    	if axis == XAXIS:
        	var = x
        	vvar = self.c.vx[self.c.cFloor]
        elif axis == YAXIS:
        	var = y 
        	vvar = self.c.vy[self.c.cFloor]
        elif axis == ZAXIS:
        	var = z
        	vvar = self.c.vz[self.c.cFloor]
        dr = sqrt(x ** 2 + y ** 2 + z ** 2)

        return -10. * vvar * var / (dr * self.c.m[self.c.cFloor])
        
    # acceleration due to spring force
    def aS(self, axis, a=2 ** (1 / 6.)):
    	if axis == XAXIS:
        	tempa = (self.c.d_sled(XAXIS) - self.c.xspringMatrix) * -500
        	tempa = tempa * self.c.sledMatrix
        elif axis == YAXIS:
        	tempa = self.c.d_sled(YAXIS) - self.c.xspringMatrix) * -500
        	tempa = tempa * self.c.sledMatrix
        elif axis == ZAXIS:
        	tempa = self.c.d_sled(ZAXIS) - self.c.xspringMatrix) * -500
        	tempa = tempa * self.c.sledMatrix
        	
        return np.sum(tempa, axis=1) / self.c.m[self.c.cFloor:] 
