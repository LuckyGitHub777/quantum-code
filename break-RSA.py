#!/usr/bin/env python3
import sys
import qiskit

# Breaking RSA Encryption using Qiskit Aqua library to run Shor's algorithm
# Import Shor
from qiskit.aqua.algorithms import Shor

# Import QuantumInstance
from qiskit.aqua import QuantimInstance

# import Aer; a quantum  simulator 
from qiskit.aqua import QuantimInstance

# Set key as the number we want to factor
key = 21 

# Set a random base value that is not a factor of the key
base = 2

# Get the backend of the quantum simulator using Aer.get
# You can replace the 'qasm_simulator' with an actual quantum chip
backend = Aer.get_backend('qasm_simulator')


# Set up a Quantum Instance with a backend
# Set up the number of shots, or runs, of the algorithm
qi = QuantumInstance(backend=backend, shots=1024)

# Call shor with the key, base, and quantum_instance
shors = Shor(N=key, a=base, quantum_instance = qi)

# Call run on shors to get the results
results = shors.run()

# Print the results
print(results['factors'])

if __name__ == '__main__':
    main()