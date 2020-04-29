import matplotlib.pyplot as plt
import numpy as np
import serial
import time

N = 400
data = np.arange(0, N, 1.0)
x = np.arange(0, N, 4.0)
y = np.arange(1, N, 4.0)
z = np.arange(2, N, 4.0)
Displacement = np.arange(3, N, 4.0)
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200)

for i in range(N):
    line = s.readline()
    data[i] = float(line)

for i in range(100):
    x[i] = data[4*i]
    y[i] = data[4*i + 1]
    z[i] = data[4*i + 2]
    Displacement[i] = data[4*i + 3]

Time = np.arange(0.1, 10.1, 0.1)

plt.subplot(211)
plt.plot(Time, x, color = "blue", label = "x")
plt.ylim(-1.5, 1.5)
plt.plot(Time, y, color = "red", label = "y")
plt.plot(Time, z, color = "green", label = "z")
plt.xlabel("Time")
plt.ylabel("Acc Vector")
plt.legend(loc = 'lower left')

plt.subplot(212)
plt.plot(Time, Displacement, "o")
plt.ylim(0, 1)
plt.xlabel("Time")
plt.ylabel("Displacement")

plt.show()
s.close