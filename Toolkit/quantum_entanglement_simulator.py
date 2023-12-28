import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Define the Pauli matrices
sx = sigmax()
sy = sigmay()
sz = sigmaz()

# Create the Bell state (entangled state)
bell_state = (tensor(basis(2, 0), basis(2, 0)) + tensor(basis(2, 1), basis(2, 1))).unit()

# Define measurement operators for each qubit
measure_op_1 = tensor(identity(2), identity(2))  # Measurement operator for qubit 1
measure_op_2 = tensor(identity(2), identity(2))  # Measurement operator for qubit 2

# Bell inequality parameters
bell_operator = measure_op_1 * tensor(sx, sx) + measure_op_1 * tensor(sy, sy) + measure_op_2 * tensor(sx, sx) - measure_op_2 * tensor(sy, sy)

# Number of runs
num_runs = 1000

# Simulate measurements
results = []
for _ in range(num_runs):
    # Apply Bell state to the measurement operators
    bell_measurement = bell_state.dag() * bell_operator * bell_state

    # Perform measurement and store the result
    measurement_result = np.random.choice([-1, 1], p=[(1 + result) / 2 for result in bell_measurement.eigenstates()[1][0]])
    results.append(measurement_result)

# Display results
print("Results:", results)
correlation = sum(results) / num_runs
print("Correlation:", correlation)

# Visualization (optional)
fig, ax = plt.subplots()
ax.bar(["Measurement 1", "Measurement 2"], [sum(results[:num_runs//2]), sum(results[num_runs//2:])])
ax.set_ylabel("Frequency")
ax.set_title("Bell State Measurement Results")
plt.show()
