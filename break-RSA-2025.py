#!/usr/bin/env python3

from qiskit_algorithms import Shor
from qiskit_aer import AerSimulator
from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit import Aer

# Optional: Seed for reproducibility
algorithm_globals.random_seed = 123

# Set the number to factor (same as your original 'key')
N = 21

# Get backend simulator (same as 'qasm_simulator')
backend = Aer.get_backend('aer_simulator')

# Set up the quantum instance with the backend
qi = QuantumInstance(backend=backend, shots=1024)

# Initialize Shor's algorithm and run it
shor = Shor(N)
result = shor.run(qi)

# Print the result (factors)
print("Factors found:", result.factors)
