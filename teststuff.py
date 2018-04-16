from __future__ import division
import numpy as np

Slo = 1.0 #low displacement
Smid = 2.0 #intermediate displacement
Shi = 5.0 #high displacement
N = 100
#Create arrays
S = np.empty(N+1, float)
S[0] = Shi
S[N] = Slo
S[1:N] = Smid
print S[0]
Sp = np.empty(N+1, float)
Sp[0] = Shi
Sp[N] = Slo

tauend = 400.0
h = 0.1
tau = 0.0
while tau < tauend:
	for i in range(1, N-1):

		
		#Sp[i] = S[i] - S[i]*(S[i+1] - S[i-1]) - 2*h*(S[i+2] - 2*S[i+1] + 2*S[i-1] - S[i-2])
		Sp[i] = S[i] - (h*S[i])*(S[i+1] - S[i-1]) - (h/(2*(0.5**3))*(S[i+2] - 2*S[i+1] + 2*S[i-1] - S[i-2]))
		print S[i]
		Sp, S = S, Sp
	
	tau += h
	
print S