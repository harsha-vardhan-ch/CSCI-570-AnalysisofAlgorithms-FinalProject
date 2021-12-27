
import time, os, psutil, sys
delta=30
alpha= {'AA': 0, 'AC':110, 'CA': 110, 'AG': 48, 'GA': 48, 'CC':0, 'AT': 94, 'TA': 94, 'CG':118, 'GC': 118, 'GG': 0, 'TG':110, 'GT':110, 'TT':0, 'CT': 48, 'TC':48}
    
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
		if A[i][j] == A[i-1][j-1] + alpha[X[i-1]+Y[j-1]]:
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
	return p, q

def alignment(X, Y):
	m=len(X)
	n=len(Y)
	A=[[0 for c in range(n+1)] for r in range(m+1)]
	for i in range(m+1):
		A[i][0]=delta * i
	for j in range(n+1):
		A[0][j] = delta * j
	for j in range(1, n+1):
		for i in range(1, m+1):
			A[i][j]=min(alpha[X[i-1]+Y[j-1]]+A[i-1][j-1], delta+A[i-1][j], delta+A[i][j-1])
	p, q = output_result(A, X, Y, m, n)	
	return p, q, A[m][n]


def space_efficient_alignment(X, Y):
	n=len(X)
	m=len(Y)
	B = [[0 for i in range(m+1)] for j in range(2)]
	for i in range(m+1):
		B[0][i]=i*delta
	for i in range(1, n+1):
		B[1][0] = B[0][0]+ delta
		for j in range(1, m+1):

			B[1][j] = min(B[0][j-1] + alpha[X[i-1] + Y[j-1]],
                            B[0][j] + delta,
                            B[1][j-1] + delta )
		for i in range(0, m+1):
			B[0][i] = B[1][i]

	return B[1]


def backward_space_efficient_alignment(X, Y):
	n=len(X)
	m=len(Y)
	B = [[0 for i in range(m+1)] for j in range(2)]
	for i in range(m+1):
		B[0][i]=i*delta
	for i in range(1, n+1):
		B[1][0] = B[0][0]+ delta
		for j in range(1, m+1):
			B[1][j] = min(alpha[X[n-i]+Y[m-j]]+B[0][j-1] , delta + B[0][j], delta + B[1][j-1])
		for i in range(0, m+1):
			B[0][i] = B[1][i]

	return B[1]


def divide_and_conquer(X, Y):
	n = len(X)
	m = len(Y)
	if m <= 2 or n <= 2:
		return alignment(X, Y)
	else:
		yL = space_efficient_alignment(X[:n//2], Y)
		yR = backward_space_efficient_alignment(X[n//2:], Y)

		mid_partition=[yL[j]+yR[m-j] for j in range(m+1)]
		cut=mid_partition.index(min(mid_partition))

		yL,yR,mid_partition=[],[],[]

		res_left = divide_and_conquer(X[:n//2], Y[:cut])
		res_right = divide_and_conquer(X[n//2:], Y[cut:])

		return [res_left[i] + res_right[i] for i in range(3)]


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

	r=divide_and_conquer(s1,s2)
	f = open("output.txt", "w")
	output_string=r[0][:50]+' '+r[0][-50:]+'\n'+r[1][:50]+' '+r[1][-50:]+'\n'+str(r[2])+'\n'+str(format(time.time() - stime,".6f")+'\n'+str(float(psutil.Process(os.getpid()).memory_info().rss /1024))+'\n')
	f.write(output_string)
	f.close()





