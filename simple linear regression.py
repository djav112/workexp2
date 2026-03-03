x = [20, 25, 30, 35]
y = [50, 54, 61, 77]

#y = mx + c
m = 0
c = 0

p = len(x)
learning_rate = 0.00001

attempts = 1000

for i in range(attempts):
    dm = 0
    dc = 0

    for i in range(p):
        predicted_y = m * x[i] + c
        error = predicted_y - y[i] #error = prediction - real value

        dm += error * x[i] 
        dc += error


    m = m - learning_rate * (2/p) * dm 
    c = c - learning_rate * (2/p) * dc

print("gradient is", m)
print("y-intercept is", c)
