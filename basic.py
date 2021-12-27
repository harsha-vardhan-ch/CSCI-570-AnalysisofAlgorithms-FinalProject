
import time, os, psutil, sys
#import matplotlib.pyplot as plt
alpha = dict()
alpha["A"] = dict()
alpha["C"] = dict()
alpha["T"] = dict()
alpha["G"] = dict()
alpha["A"]["A"] = 0
alpha["A"]["C"] = 110
alpha["A"]["G"] = 48 
alpha["A"]["T"] = 94

alpha["C"]["A"] = 110
alpha["C"]["C"] = 0
alpha["C"]["G"] = 118 
alpha["C"]["T"] = 48

alpha["G"]["A"] = 48
alpha["G"]["C"] = 118
alpha["G"]["G"] = 0 
alpha["G"]["T"] = 110

alpha["T"]["A"] = 94
alpha["T"]["C"] = 48
alpha["T"]["G"] = 110 
alpha["T"]["T"] = 0
delta=30
output_string=''

def generate_actual_string(parameter_string, op):
	r=parameter_string
	p=r
	for i in op:
		r=r[0:i+1]+p+r[i+1:]
		p=r
	return r

def output_result(A, X, Y, m, n):
	S1 = ""
	S2 = ""
	i, j = m, n
	while j > 0 and i > 0: 
		if A[i][j] == A[i-1][j-1] + alpha[X[i-1]][Y[j-1]]:
			S1 += X[i-1]
			S2 += Y[j-1]
			i -= 1
			j -= 1
		elif A[i][j] == delta+A[i-1][j]:
			S1 += X[i-1]
			S2 += "_"
			i -= 1
		elif A[i][j] == delta+A[i][j-1]:
			S1 += "_"
			S2 += Y[j-1]
			j -= 1
	while i > 0:
		S1 += X[i-1]
		S2 += "_"
		i -= 1
	while j > 0:
		S1 += "_"
		S2 += Y[j-1]
		j -= 1

	p = S1[::-1]
	q = S2[::-1]

	global output_string
	output_string=output_string+p[:50]+' '+p[-50:]+'\n'+q[:50]+' '+q[-50:]+'\n'+str(float(A[m][n]))+'\n'
	

def alignment(X,Y):
	m=len(X)
	n=len(Y)
	A=[[0 for c in range(n+1)] for r in range(m+1)]
	for i in range(m+1):
		A[i][0]=delta * i
	for j in range(n+1):
		A[0][j] = delta * j
	for j in range(1, n+1):
		for i in range(1, m+1):
			A[i][j]=min(alpha[X[i-1]][Y[j-1]]+A[i-1][j-1], delta+A[i-1][j], delta+A[i][j-1])
	output_result(A, X, Y, m, n)


if __name__ == "__main__":
	stime=time.time()
	with open(sys.argv[1]) as f:
		data=f.readlines()
	f.close()
	n=len(data)
	tempstr_1=data[0].rstrip('\r\n')
	lentemp1=len(tempstr_1)
	s1op=[]
	i=1
	
	while len(data[i])<5:
		s1op.append(int(data[i]))
		i+=1

	j=i-1

	tempstr_2=data[i].rstrip('\r\n')
	lentemp2=len(tempstr_2)
	i+=1
	s2op=[]
	while i<n:
		s2op.append(int(data[i].rstrip('\r\n')))
		i+=1

	s1=generate_actual_string(tempstr_1,s1op)
	s2=generate_actual_string(tempstr_2,s2op)
	
	alignment(s1,s2)
	
	f = open("output.txt", "w")
	output_string=output_string+str(format(time.time() - stime,".6f")+'\n'+str(float(psutil.Process(os.getpid()).memory_info().rss /1024))+'\n')
	f.write(output_string)
	f.close()




