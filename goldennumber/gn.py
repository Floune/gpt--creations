import matplotlib.pyplot as plt
import numpy as np

phi = (1 + np.sqrt(5)) / 2

x = np.linspace(-1, 1, 1000)
y = np.sqrt(1 - (x ** 2)) * np.sin(np.pi * phi * x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set_title('Courbe du nombre d\'or')
plt.show()

