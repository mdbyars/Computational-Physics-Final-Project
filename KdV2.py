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

tau1 = 0.01
tau2 = 0.1
tau3 = 0.4
tau4 = 1.0
tau5 = 10.0
tauend = tau5 + epsilon

Slo = 1.0 #low displacement
Smid = 25.0 #intermediate displacement
Shi = 50.0 #high displacement

#Create arrays
S = np.empty(N+1, float)
S[0] = Shi
S[N] = Slo
S[1:N] = Smid
print S[0]
Sp = np.empty(N+1, float)
Sp[0] = Shi
Sp[N] = Slo

tau = 0.0
while tau < tauend:
	for i in range(1, N-1):
	#Calculate the new values of S


		Sp1 = S[i] 
		Sp2 = (h/(2*a))*(S[i+1] - S[i-1]) 
		Sp3 = (h/(2*a**3))*(S[i+1] - 2*S[i+1] + 2*S[i-1] - S[i - 2])
		Sp[i] = Sp1 - Sp2 - Sp3
		#t = (2*tau/9)*np.sqrt(h0/9)
		#Sp[i] = S[i] - (h*S[i]/(2*n(a, t)))*(S[i+1] - S[i-1]) - (h/(2*n(a,t)**3)*(S[i+2] - 2*S[i+1] + 2*S[i-1] - S[i-2]))
		
	S, Sp = Sp, S
	tau += h