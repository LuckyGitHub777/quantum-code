#!/usr/bin/env python3
import sys
from qiskit.algorithms import Shor
from qiskit_aer import Aer
from qiskit.utils import QuantumInstance, algorithm_globals

# Optional: Seed for reproducibility
algorithm_globals.random_seed = 123

# Number to factor (same as 'key')
key = 21

# Base (not required in modern API but keeping for parity)
base = 2  

# Get backend (same as old qasm_simulator)
backend = Aer.get_backend('aer_simulator')

# Set up a Quantum Instance with the backend
qi = QuantumInstance(backend=backend, shots=1024)

# Initialize Shor's algorithm (no need to pass base anymore)
shors = Shor()

# Run factoring with QuantumInstance
results = shors.factor(N=key, quantum_instance=qi)

# Print the factors (same as old Aqua output style)
if hasattr(results, "factors"):
    print("Factors found:", results.factors)
elif isinstance(results, dict) and "factors" in results:
    print("Factors found:", results["factors"])
else:
    print("Result object:", results)
