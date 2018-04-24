from __future__ import division
import numpy as np
import math
import matplotlib.pyplot as plt

Z = 50.0
h0 = 20.0
E0 = Z / h0
g = 9.81

N = 100
a = Z/N
h = 0.01
epsilon = h/1000

tau1 = 0.0
tau2 = 2.0
tau3 = 4.0
tau4 = 6.0
tau5 = 8.0

tauend = tau5 + epsilon

def sol(n, tau):
	
	S = E0*((1/np.cosh((np.sqrt(E0/12))*(n - E0*tau/3.)))**2)
	return S
	
nlist = np.linspace(0, 100, 101)
"""
Slist1 = [sol(n, tau1) for n in nlist]
plt.plot(Slist1)

Slist2 = [sol(n, tau2) for n in nlist]
plt.plot(Slist2)

Slist3 = [sol(n, tau3) for n in nlist]
plt.plot(Slist3)
Slist4 = [sol(n, tau4) for n in nlist]
plt.plot(Slist4)
Slist5 = [sol(n, tau5) for n in nlist]"""




	
#Slo = 1.0 #low displacement
#Smid = 25.0 #intermediate displacement
#Shi = 50.0 #high displacement

#Create arrays
S = np.empty(N+1, float)
S[0] = sol(0, 0)
S[N] = sol(N, 0)
S[1:N] = [sol(n, tau3) for n in nlist[1:N]]

Sp = np.empty(N+1, float)
Sp[0] = sol(N, 0)
Sp[N] = sol(0, 0)

tau = 0.0
while tau < tauend:
	for i in range(1, N-1):
	#Calculate the new values of S


		Sp1 = S[i] 
		Sp2 = (h/(2*a))*(S[i+1] - S[i-1]) 
		Sp3 = (h/(2*a**3))*(S[i+1] - 2*S[i+1] + 2*S[i-1] - S[i - 2])
		Sp[i] = Sp1 - Sp2 - Sp3


	S, Sp = Sp, S
	tau += h
		# Make plots at the given times
	if abs(tau-tau1)<epsilon:
		plt.plot(S)
	"""if abs(tau-tau2)<epsilon:
		plt.plot(S)
	if abs(tau-tau3)<epsilon:
		plt.plot(S)
	if abs(tau-tau4)<epsilon:
		plt.plot(S)
	if abs(tau-tau5)<epsilon:
		plt.plot(S)"""
		

	
plt.xlabel('n(x, t)')
plt.ylabel('S')
#plt.xlim(0, 50.0)
plt.show()
