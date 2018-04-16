import numpy as np
import matplotlib.pyplot as plt
def solver(I, w, dt, T):
	"""
	Solve u’’ + w**2*u = 0 for t in (0,T], u(0)=I and u’(0)=0,
	by a central finite difference method with time step dt.
	"""
	dt = float(dt)
	Nt = int(round(T/dt))
	u = np.zeros(Nt+1)
	t = np.linspace(0, Nt*dt, Nt+1)
	u[0] = I
	u[1] = u[0] - 0.5*dt**2*w**2*u[0]
	for n in range(1, Nt):
		u[n+1] = 2*u[n] - u[n-1] - dt**2*w**2*u[n]
	return u, t