import matplotlib.pyplot as plt

bandwidth = [900, 1024, 200, 150]
time = [0, 5, 10, 15]
plt.plot(time, bandwidth)
plt.savefig('line.png')
