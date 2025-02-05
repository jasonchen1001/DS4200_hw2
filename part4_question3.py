import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# left: dark background
ax[0].set_facecolor('black')
ax[0].add_patch(plt.Circle((0.5, 0.5), 0.2, color='gray'))
ax[0].set_title("Dark Background")

# right: light background
ax[1].set_facecolor('white')
ax[1].add_patch(plt.Circle((0.5, 0.5), 0.2, color='gray'))
ax[1].set_title("Light Background")

plt.show()
