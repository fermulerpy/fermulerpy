from fermulerpy.analytic import *
import cmath
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

real_val = []
img_val = []
i_val = []

i = 0

while(i<=50):
    i_val.append(i)
    inp = complex(0.5,i)
    value = zeta_function(inp)
    real_val.append(value.real)
    img_val.append(value.imag)
    i = i + 0.02


plt.plot(real_val , img_val,color='aqua')

plt.fill(real_val[0:100],img_val[0:100],color='blue')
plt.fill(real_val[1600:3000],img_val[1600:3000],color='navy')
plt.fill(real_val[100:1600],img_val[100:1600],color='mediumblue')
plt.fill(real_val[300:1200],img_val[300:1200],color='darkslateblue')
plt.fill(real_val[300:900],img_val[300:900],color='midnightblue')
#ax = plt.axes()
#ax.set_facecolor('black')
#plt.title("zeta")
#plt.savefig(fname='logo0.png',transparent=True,dpi=1500)
plt.show()

