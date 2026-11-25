
import numpy as np
import matplotlib.pyplot as plt

def erlang_b(A, C):
    B = 1.0

    for i in range(1, C + 1):
        B = (A * B) / (i + A * B)

    return B

channels = [5, 10, 15, 20, 25, 30]

traffic = np.arange(1, 31, 1)

for C in channels:
    blocking = [erlang_b(A, C) for A in traffic]
    plt.plot(traffic, blocking, label=str(C) + " Channels")

plt.xlabel("Traffic Intensity (Erlangs)")
plt.ylabel("Call Blocking Probability")
plt.title("Erlang B Call Blocking Probability")
plt.legend()
plt.grid()
plt.show()

print("Traffic\tChannels\tBlocking Probability")

for C in channels:
    A = 15
    B = erlang_b(A, C)
    print(A, "\t", C, "\t\t", round(B, 6))
