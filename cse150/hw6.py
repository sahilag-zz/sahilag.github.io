import math
with open('hw6_x.txt') as f:
    x = []
    for line in f: # read rest of lines
        x.append([int(w) for w in line.split()])
        
print x[1][0:4]

with open('hw6_y.txt') as f:
    y = [int(w) for w in f]
    
#print len(y),len(x)

n = 23
T = 267
Ti = []
for i in range(n):
	temp = 0
	for t in range(T):
		temp= temp + x[t][i]
	Ti.append(temp)
print len(Ti)
p = [1.0/(2*n) for i in range(n)]

for it in range(512):
	L = 0.0
	py = []
	for t in range(T):

		temp = 0.0
		for i in range(n):
			temp = temp + x[t][i]*math.log(1.0-p[i])
		temp = 1-math.exp(temp)	
		py.append(temp)
		#print py
		if y[t]==0: L = L + math.log(1-temp)
		else: L = L + math.log(temp)

	
	
	temp_p = []
	for i in range(n):
		temp = 0
		for t in range(T):
			temp = temp + y[t]*x[t][i]*p[i]/py[t]
		temp = temp/Ti[i]
		temp_p.append(temp)
		
	p = temp_p

	if (it == 0 or it == 1 or it == 2 or it == 4 or it == 8 or it == 16 or it == 32 or it == 64 or it == 128 or it == 256): 
		print L/T
		print p		
			
			
			
			
