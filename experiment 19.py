
import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 101, 1)

BS1 = -50 - 0.4 * time + 5 * np.sin(time / 5)
BS2 = -90 + 0.4 * time + 5 * np.cos(time / 5)

hysteresis = 5

serving_BS = 1

handoffs = []
serving_history = []

for t in range(len(time)):

    if serving_BS == 1:

        if BS2[t] > BS1[t] + hysteresis:
            serving_BS = 2
            handoffs.append(time[t])

    else:

        if BS1[t] > BS2[t] + hysteresis:
            serving_BS = 1
            handoffs.append(time[t])

    serving_history.append(serving_BS)

print("Handoff Simulation Results")
print("Total handoffs:", len(handoffs))
print("Handoff times:", handoffs)

plt.figure(figsize=(10, 5))

plt.plot(time, BS1, label="Base Station 1")
plt.plot(time, BS2, label="Base Station 2")

plt.xlabel("Time")
plt.ylabel("Signal Strength (dBm)")
plt.title("Signal Strength of Two Base Stations")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))

plt.step(time, serving_history, where='post', color='green')

plt.xlabel("Time")
plt.ylabel("Serving Base Station")
plt.title("Handoff Simulation with Hysteresis")
plt.yticks([1, 2], ["BS1", "BS2"])
plt.grid()
plt.show()
