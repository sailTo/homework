import numpy as np
def func2(p,m,n):
	v = np.zeros((n,m+1))
	i = np.zeros((n,m+1))
	u = list(range(n))
	a,b = np.shape(p)
	p1 = np.zeros((m+1,n))
	p1[:a,:] = p[:,:]
	p=p1
	for t in range(m+1):
		v[0,t] = p[t,0]
		i[0,t] = t
		for k in range(1,n):
			v[k,t],i[k,t] = max((p[j,k]+v[k-1,t-j], j) for j in range(t+1))
			u[k] = int(i[k,t])
		for k in range(n-2,-1,-1):
			t=t-int(i[k+1,t])
			u[k]=int(i[k,t])
	return v[n-1,m],u
p = np.array([[10,4,14,6,39],[30,32,19,12,42],[35,46,46,25,47],[60,52,50,40,50],[95,90,55,52,82]])
m,n = 7,5
print("The optimal solution is",func2(p,m,n))
