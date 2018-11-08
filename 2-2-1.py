import numpy as np
def func1(p,m,n):
	v = np.zeros((n,m+1))
	i = np.zeros((n,m+1))
	u = list(range(n))
	for t in range(m+1):
		v[0,t] = p[t,0]
		i[0,t] = t
		for k in range(1,n):
			v[k,t],i[k,t] = min((p[j,k]*v[k-1,t-j], j) for j in range(t+1))
			u[k] = int(i[k,t])
		for k in range(n-2,-1,-1):
			t=t-int(i[k+1,t])
			u[k]=int(i[k,t])
	return v[n-1,m],u
p = np.array([[0.4,0.6,0.8],[0.2,0.4,0.5],[0.15,0.2,0.3],[0.1,0.17,0.25]])
m,n = 3,3
print("The optimal solution is",func1(p,m,n))
