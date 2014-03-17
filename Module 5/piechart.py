from pylab import *

figure(1, figsize=(6,6)) # w x h in inches
ax = axes()
labels = ['R1', 'R2', 'R3', 'R4']
fracs = [15, 30, 45, 10]
pie(fracs, labels=labels, autopct='%1.0f%%')
savefig('test.png')
