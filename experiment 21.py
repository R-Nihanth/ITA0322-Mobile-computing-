
import numpy as np
import matplotlib.pyplot as plt

num_users = 5
num_RBs = 100
num_slots = 1000

np.random.seed(42)

channel = np.random.exponential(
    scale=1.0,
    size=(num_slots, num_users, num_RBs)
)

rate = np.log2(1 + channel)

rr_throughput = np.zeros(num_users)

for slot in range(num_slots):
    for rb in range(num_RBs):
        user = (slot * num_RBs + rb) % num_users
        rr_throughput[user] += rate[slot, user, rb]

pf_throughput = np.zeros(num_users)

average_rate = np.ones(num_users) * 0.01

alpha = 0.01

for slot in range(num_slots):
    for rb in range(num_RBs):

        metric = rate[slot, :, rb] / average_rate

        user = np.argmax(metric)

        allocated_rate = rate[slot, user, rb]

        pf_throughput[user] += allocated_rate

        average_rate *= (1 - alpha)
        average_rate[user] += alpha * allocated_rate

def jains_fairness(values):
    return (np.sum(values) ** 2) / (
        len(values) * np.sum(values ** 2)
    )

rr_fairness = jains_fairness(rr_throughput)
pf_fairness = jains_fairness(pf_throughput)

print("OFDMA Scheduler Results")

print("\nRound Robin Throughput:")
for i in range(num_users):
    print("User", i + 1, ":", round(rr_throughput[i], 2))

print("\nProportional Fair Throughput:")
for i in range(num_users):
    print("User", i + 1, ":", round(pf_throughput[i], 2))

print("\nFairness Comparison")
print("Round Robin Fairness:", round(rr_fairness, 4))
print("Proportional Fair Fairness:", round(pf_fairness, 4))

x = np.arange(num_users)
width = 0.35

plt.figure(figsize=(9, 5))

plt.bar(x - width/2, rr_throughput, width,
        label="Round Robin")

plt.bar(x + width/2, pf_throughput, width,
        label="Proportional Fair")

plt.xlabel("Users")
plt.ylabel("Total Throughput")
plt.title("OFDMA User Throughput Comparison")
plt.xticks(x, [f"User {i+1}" for i in range(num_users)])
plt.legend()
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(7, 5))

plt.bar(
    ["Round Robin", "Proportional Fair"],
    [rr_fairness, pf_fairness],
    color=["blue", "green"]
)

plt.ylabel("Jain's Fairness Index")
plt.title("OFDMA Scheduler Fairness Comparison")
plt.ylim(0, 1.1)
plt.grid(axis='y')
plt.show()
