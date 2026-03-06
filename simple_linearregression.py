x = [1, 2, 3, 4, 5]
y = [3, 4, 2, 4, 5]

meanofx = sum(x)/len(x)
meanofy = sum(y)/len(y)

#m = sum of (x-meanofx)(y-meanofy)/sum of (x-meanofx)

numx = 0
demy = 0

for i in range(len(x)):
    numx += (x[i] - meanofx) * (y[i]- meanofy)
    demy += (x[i]- meanofx) ** 2


m = numx/demy

c = meanofy - m*meanofx

print(m)
print(c)


numr = 0
demr = 0

for i in range(len(x)):
    numr +=((m*x[i]+c)-meanofy)**2
    demr +=(y[i] - meanofy)**2

    
rsquared = numr/demr
print(rsquared)