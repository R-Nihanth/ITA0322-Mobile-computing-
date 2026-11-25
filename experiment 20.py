
import numpy as np
import matplotlib.pyplot as plt

num_users = 2

codes = np.array([
    [1, 1, 1, 1],
    [1, -1, 1, -1]
])

data = np.array([1, 0])

bpsk = 2 * data - 1

print("Original Data:", data)
print("BPSK Data:", bpsk)

spread_signals = []

for i in range(num_users):
    spread = bpsk[i] * codes[i]
    spread_signals.append(spread)

spread_signals = np.array(spread_signals)

print("Spread Signals:")
print(spread_signals)

combined_signal = np.sum(spread_signals, axis=0)

print("Combined CDMA Signal:")
print(combined_signal)

noise = np.random.normal(0, 0.1, len(combined_signal))

received_signal = combined_signal + noise

print("Received Signal:")
print(received_signal)

recovered_data = []

for i in range(num_users):
    despread = np.sum(received_signal * codes[i]) / len(codes[i])

    if despread > 0:
        recovered_data.append(1)
    else:
        recovered_data.append(0)

print("Recovered Data:")
print(recovered_data)

plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(spread_signals[0])
plt.title("User 1 Spread Signal")
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(spread_signals[1])
plt.title("User 2 Spread Signal")
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(received_signal)
plt.title("Combined Received Signal")
plt.grid()

plt.tight_layout()
plt.show()
