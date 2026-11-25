
import numpy as np
import matplotlib.pyplot as plt

i0 = 6
n = 4
R = 1
total_channels = 420

cluster_sizes = [1, 3, 4, 7, 9, 12, 13, 16, 19]

print("Cluster Size\tReuse Distance\tS/I (dB)\tCapacity")

for N in cluster_sizes:

    D = R * np.sqrt(3 * N)

    SI = (np.sqrt(3 * N) ** n) / i0

    SI_dB = 10 * np.log10(SI)

    capacity = total_channels / N

    print(N, "\t\t", round(D, 2),
          "\t\t", round(SI_dB, 2),
          "\t\t", round(capacity, 2))

si_values = []

for N in cluster_sizes:
    SI = (np.sqrt(3 * N) ** n) / i0
    si_values.append(10 * np.log10(SI))

plt.plot(cluster_sizes, si_values, 'bo-')
plt.xlabel("Cluster Size")
plt.ylabel("S/I Ratio (dB)")
plt.title("S/I Ratio vs Cluster Size")
plt.grid()
plt.show()

capacities = [total_channels / N for N in cluster_sizes]

plt.plot(cluster_sizes, capacities, 'ro-')
plt.xlabel("Cluster Size")
plt.ylabel("Channels per Cell")
plt.title("System Capacity vs Cluster Size")
plt.grid()
plt.show()
