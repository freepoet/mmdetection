import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

cor=[
 [0.17],
 [0.18],
 [0.18],
 [0.15],
 [0.15],
 [0.23],
 [0.23],
 [0.26],
 [0.26],
 [0.30],
 [0.39],
 [0.39],
 [0.46],
 [0.46],
 [0.62],
 [0.62],
 [0.66],
 [0.79],
 [0.79],
 [0.88],
 [0.88],
 [0.94],
 [0.94],
 [0.95],
 [0.95],
 [0.97],
 [0.97],
 [0.97],
 [0.92],
 [0.92],
 [0.90],
 [0.90],
 [0.78],
 [0.78],
 [0.67],
 [0.58],
 [0.58],
 [0.51],
 [0.51],
 [0.45],
 [0.45],
 [0.43],
 [0.34],
 [0.34],
 [0.29],
 [0.29],
 [0.26],
 [0.26],
 [0.22],
 [0.22],
 [0.20],
 [0.19],
 [0.19],
 [0.15],
 [0.15],
 [0.16],
 [0.16],
 [0.14],
 [0.14],
 [0.12],
 [0.12],
 [0.12],
 [0.11],
 [0.11],
 [0.12],
 [0.12],
 [0.12],
 [0.14],
 [0.14],
 [0.15],
 [0.15],
 [0.15],
 [0.15],
 [0.12],
 [0.12]
]
cor=np.array(cor)
cor=np.squeeze(cor)
s=0.5
x=np.arange(s,2,0.02)
func = interpolate.interp1d(x, cor, kind='cubic')
x_new=np.arange(s,2-0.02+0.005,0.005)
y_new=func(x_new)


plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#
# font1 = {'family': 'Times New Roman',
#          'weight': 'normal',
#          'size': 20,
#          }
plt.xlabel('R',fontsize=14)
# plt.ylabel('CC',font1)
plt.ylabel('CC',fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.plot(x_new,y_new,color=(0,0.5,1), linewidth=1.5)
plt.grid(True)
plt.xticks(np.arange(s,2+0.1, 0.1))
plt.yticks(np.arange(0,1+0.1,0.1))
plt.xlim([s,2])
plt.ylim([0,1])


