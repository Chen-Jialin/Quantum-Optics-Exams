import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt
pi = np.pi

alpha = 1
t = np.linspace(0, 20, 10000)
P_g = np.exp(-np.abs(alpha)**2) * (1 + alpha + np.sum([alpha**(2 * n) / factorial(n, exact=False) * np.cos(np.sqrt((n - 1) * n) * t)**2 for n in range(2, 50)], 0))
plt.plot(t, P_g)
plt.xlabel("$\lambda t$")
plt.ylabel("$P_g$")
plt.show()