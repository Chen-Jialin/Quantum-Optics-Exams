import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

alpha = pi / 4
t = np.linspace(0, 20 * pi / np.sqrt(30), 1000)
P_e = np.cos(alpha)**2 * np.cos(np.sqrt(56) * t) + np.sin(alpha)**2 * np.cos(np.sqrt(30) * t)
plt.plot(t, P_e)

plt.xlabel("$gt$")
plt.ylabel("$P_e$")
plt.show()