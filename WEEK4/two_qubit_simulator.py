# Quantum Simulator Deep Explanation
# -------------------------------------------------------------
# This script simulates a 2-qubit quantum system and applies three quantum gates:
# 1. Hadamard (H) on the first qubit
# 2. Pauli-X (NOT) on the second qubit
# 3. CNOT (Controlled-NOT) on both qubits
#
# Qubit States:
# - Single qubit |0> = [1, 0], |1> = [0, 1] (column vectors)
# - Two qubits: tensor product, e.g., |00> = kron([1,0], [1,0]) = [1,0,0,0]
#
# Quantum Gates:
# - Hadamard (H): (1/sqrt(2)) * [[1, 1], [1, -1]]
#   - Creates superposition: |0> -> (|0>+|1>)/sqrt(2), |1> -> (|0>-|1>)/sqrt(2)
# - Pauli-X (X): [[0, 1], [1, 0]]
#   - Flips qubit: |0> <-> |1>
# - Identity (I): [[1, 0], [0, 1]]
#   - Used for targeting specific qubits in multi-qubit gates
# - CNOT (4x4): Flips second qubit if first is |1>
#
# Gate Application:
# - Hadamard on first qubit: kron(H, I)
# - Pauli-X on second qubit: kron(I, X)
# - CNOT: 4x4 matrix acting on both qubits
# - State updated by matrix multiplication (@)
#
# Matrix Sizes:
# - All matrices are 4x4 (feasible, <6x6)
#
# Output:
# - Final state vector after all operations
# - Matrix shapes for verification
# -------------------------------------------------------------

# Quantum Simulator for 2 Qubits with 3 Operations
import numpy as np

class TwoQubitSimulator:
	"""
	Simulates a 2-qubit quantum system and applies Hadamard, Pauli-X, and CNOT gates.
	"""
	def __init__(self):
		# --- Qubit States ---
		self.zero = np.array([[1], [0]])  # |0> state
		self.one = np.array([[0], [1]])   # |1> state
		# Initial state |00>
		self.state = np.kron(self.zero, self.zero)  # 4x1 vector

		# --- Quantum Gates ---
		self.H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])  # Hadamard
		self.X = np.array([[0, 1], [1, 0]])  # Pauli-X
		self.I = np.eye(2)  # Identity
		self.CNOT = np.array([
			[1, 0, 0, 0],
			[0, 1, 0, 0],
			[0, 0, 0, 1],
			[0, 0, 1, 0]
		])  # CNOT

	def apply_gates(self):
		# --- Gate Application ---
		# Hadamard on first qubit
		self.H1 = np.kron(self.H, self.I)
		self.state = self.H1 @ self.state
		# Pauli-X on second qubit
		self.X2 = np.kron(self.I, self.X)
		self.state = self.X2 @ self.state
		# CNOT
		self.state = self.CNOT @ self.state

	def print_state(self):
		print("\nFinal state vector after H, X, CNOT:")
		print("[[{0: .8f}]".format(self.state[0][0]))
		for i in range(1, len(self.state)):
			if i == len(self.state) - 1:
				print(" [{0: .8f}]]".format(self.state[i][0]))
			else:
				print(" [{0: .8f}]".format(self.state[i][0]))

	def print_matrix_shapes(self):
		print("\nMatrix shapes:")
		print(f"  Hadamard ⊗ I : {self.H1.shape}")
		print(f"  I ⊗ X       : {self.X2.shape}")
		print(f"  CNOT         : {self.CNOT.shape}")

	def check_feasibility(self):
		feasible = all(m.shape[0] <= 6 and m.shape[1] <= 6 for m in [self.H1, self.X2, self.CNOT])
		print()
		if feasible:
			print("All matrices are feasible (do not exceed 6x6). Quantum simulation is possible.")
		else:
			print("One or more matrices exceed 6x6. Quantum simulation is NOT feasible.")

	def run(self):
		self.apply_gates()
		self.print_state()
		self.print_matrix_shapes()
		self.check_feasibility()

if __name__ == "__main__":
    twoQubitSimulator = TwoQubitSimulator()
    twoQubitSimulator.run()