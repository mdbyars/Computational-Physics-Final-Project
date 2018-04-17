from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

Z = 50.0
h0 = 20.0
g = 9.81

N = 100
a = Z/N
h = 1
epsilon = h/1000

 
def n(x, t):
	return 3*(x - np.sqrt(g*h0*t))/h0
	
def tauf(t):
	return (9./2)*(np.sqrt(g/h0))*t
	

t1 = 0.01
t2 = 0.1
t3 = 0.4
t4 = 1.0
t5 = 10.0
tend = t5 + epsilon

tau1 = tauf(t1)
tau2 = tauf(t2)
tau3 = tauf(t3)
tau4 = tauf(t4)
tau5 = tauf(t5)
tauend = tauf(tend)
print tauend

Slo = 0.0 #low displacement
Smid = 1.0 #intermediate displacement
Shi = 5.0 #high displacement

#Create arrays
S = np.empty(N+1, float)
S[0] = Shi
S[N] = Slo
S[1:N] = Smid
print S[0]
Sp = np.empty(N+1, float)
Sp[0] = Shi
Sp[N] = Slo

#Main loop
tau = 0.0
while tau < tauend:
	for i in range(1, N-1):
	#Calculate the new values of S
		"""print 'first term',S[i]
		print '2nd term',(h*S[i]/(2*a))*(S[i+1] - S[i-1])
		print '3rd term',(h/(2*a**3)*(S[i+2] - 2*S[i+1] + 2*S[i-1] - S[i-2]))"""
		t = (2*tau/9)*np.sqrt(h0/9)
		Sp[i] = S[i] - (h*S[i]/(2*n(a, t)))*(S[i+1] - S[i-1]) - (h/(2*n(a,t)**3)*(S[i+2] - 2*S[i+1] + 2*S[i-1] - S[i-2]))
		
	S, Sp = Sp, S
	tau += h

	# Make plots at the given times
	if abs(tau-tau1)<epsilon:
		plt.plot(S)
	if abs(tau-tau2)<epsilon:
		plt.plot(S)
	if abs(tau-tau3)<epsilon:
		plt.plot(S)
	if abs(tau-tau4)<epsilon:
		plt.plot(S)
	if abs(tau-tau5)<epsilon:
		plt.plot(S)
	

plt.xlabel('Tau')
plt.ylabel('S')
plt.show()
