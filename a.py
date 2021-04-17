from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import csv
def read_csv(fname):
    time = []
    x = []
    y = []
    z = []
    init = False
    n = 0
    t0 = 0
    with open(fname, newline = '') as csvfile:
        datareader = csv.reader(csvfile)
        
        for row in datareader:
            if (len(row) >= 4):
                if init:
                    n += 1
                    if t0 == 0:
                        t0 = float(row[0])
                    time.append((float(row[0]) - t0) / 10e9)
                    x.append(float(row[4]))
                    y.append(float(row[3]))
                    z.append(float(row[2]))
                else:
                    init = True
    return time, x, y, z, n

t, ax, ay, az, n  = read_csv("Accelerometer.csv")
pyplot.plot(t, ax)
pyplot.plot(t, ay)
pyplot.plot(t, az)
pyplot.show()

t, ax, ay, az, n  = read_csv("A2.csv")
pyplot.plot(t, az)
pyplot.plot(t, ax)
pyplot.show()
V = [0]
Z = [0]
fig = pyplot.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
l = (n // 2)
t0 = [t[l]]
Z0 = [0]
for i in range(n - 1):
    V.append(V[i] + az[i] *(t[i + 1] - t[i]))
    Z.append(Z[i] + V[i] *(t[i + 1] - t[i]) + 0.5 * az[i] * ((t[i + 1] - t[i]) ** 2))
Z0 = Z[l:]
t0 = t[l:]      
ax1.plot(t0, Z0, 'b-')
ax2.plot(t, Z,'r-')
ax1.set_xlabel("t/2")
ax1.set_ylabel('Z')
ax2.set_xlabel('t')
ax2.set_ylabel('Z')
pyplot.show()
t, ax, ay, az, n = read_csv("P4.csv")
Vz = [0]
Z = [0]
Vy = [0]
Y = [0]
Vx = [0]
X = [0]
for i in range(n - 1):
    Vz.append(Vz[i] + az[i] *(t[i + 1] - t[i]))
    Z.append(Z[i] + Vz[i] *(t[i + 1] - t[i]) + 0.5 * az[i] * ((t[i + 1] - t[i]) ** 2))
    Vy.append(Vy[i] + ay[i] *(t[i + 1] - t[i]))
    Y.append(Y[i] + Vy[i] *(t[i + 1] - t[i]) + 0.5 * ay[i] * ((t[i + 1] - t[i]) ** 2))
    Vx.append(Vx[i] + ax[i] *(t[i + 1] - t[i]))
    X.append(X[i] + Vx[i] *(t[i + 1] - t[i]) + 0.5 * ax[i] * ((t[i + 1] - t[i]) ** 2))
fig = pyplot.figure()
a = fig.add_subplot(111, projection='3d')
a.scatter(X, Y, Z, c='r', marker='o')
a.set_xlabel('X Label')
a.set_ylabel('Y Label')
a.set_zlabel('Z Label')
pyplot.show()
