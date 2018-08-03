
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

import numpy as np
dt = 0.01
x = np.arange(-50.0, 50.0, dt)
y = np.arange(0, 100.0, dt)

fig = plt.figure()

gs = GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
plt.plot(x,y)
plt.xscale('symlog')
plt.ylabel('symlogx')
plt.grid(True)

# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax2 = plt.subplot(gs[1, :-1],sharex=ax1)
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[-1, -2])

fig.suptitle("GridSpec")

plt.show()




