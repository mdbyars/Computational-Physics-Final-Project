from __future__ import division
from numpy import empty
from pylab import plot, xlabel, ylabel, show

#Constants
L = 0.01
D = 4.25e-6
N = 100
a = L/N
h = 1.e-4
epsilon = h/1000

Tlo = 0.0 #low temp
Tmid = 20.0 #intermediate temp
Thi = 50.0 #high temp

t1 = 0.01
t2 = 0.1
t3 = 0.4
t4 = 1.0
t5 = 10.0
tend = t5 + epsilon

#Create arrays
T = empty(N+1, float)
T[0] = Thi
T[N] = Tlo
T[1:N] = Tmid
Tp = empty(N+1, float)
Tp[0] = Thi
Tp[N] = Tlo

#Main loop
t = 0.0
c = h*D/(a*a)
while t < tend:

	#Calculate the new values of T
	for i in range(1, N):
		Tp[i] = T[i] + c*(T[i+1]+T[i-1]-2*T[i])
	T, Tp = Tp, T
	t += h
	
	# Make plots at the given times
	if abs(t-t1)<epsilon:
		plot(T)
	if abs(t-t2)<epsilon:
		plot(T)
	if abs(t-t3)<epsilon:
		plot(T)
	if abs(t-t4)<epsilon:
		plot(T)
	if abs(t-t5)<epsilon:
		plot(T)

xlabel("x")
ylabel("T")
show()