import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

n = 4
t = np.linspace(0, 5 * pi, 1000)
n_bar = n + 1 - np.cos(2 * t)
plt.plot(t, n_bar)

plt.yticks([n, n + 1, n + 2], ["$n$", "$n+1$", "$n+2$"])
plt.xlabel("$\sqrt{(n+1)(n+2)}\lambda t$")
plt.ylabel("$\langle n\\rangle$")
plt.show()