"""
Interactive QASM Builder
-----------------------
This script allows users to build a quantum circuit interactively from the command line.

Features:
- Prompts the user for the number of qubits.
- For each qubit, allows entry of multiple gates (x, h, id, y, z, s, t, rx, ry, rz, cx) separated by commas.
- For rx, ry, rz gates, prompts for an angle in degrees and applies the rotation.
- For cx (CNOT), prompts for the target qubit.
- Builds the circuit, prints the generated QASM, saves it to 'myfile.qasm', and displays the loaded circuit.

Usage:
	python interactive_qasm_builder.py

Requirements:
	- qiskit

Example:
	How many qubits do you want? 2
	Which gate(s) to apply to qubit 0? (comma separated, e.g. x,h,rx): x,h,rx
	Enter angle in degrees for rx on qubit 0: 90
	Which gate(s) to apply to qubit 1? (comma separated, e.g. x,h,rx): cx
	You selected CNOT for qubit 1 as control. Enter target qubit (0 to 1, not 1): 0

The script will then output the QASM and show the circuit.
"""

import math
import qiskit.qasm2
from qiskit.circuit import QuantumCircuit


class InteractiveQASMBuilder:
	"""
	Class to interactively build a quantum circuit and QASM file from user input.
	"""
	def __init__(self):
		self.qc = None
		self.n = 0

	def prompt_qubits(self):
		self.n = int(input("How many qubits do you want? "))
		self.qc = QuantumCircuit(self.n, self.n)

	def prompt_gates(self):
		print("Available gates: x, h, id, y, z, s, t, rx, ry, rz, cx (CNOT)")
		for i in range(self.n):
			gates_input = input(f"Which gate(s) to apply to qubit {i}? (comma separated, e.g. x,h,rx): ").strip().lower()
			gates = [g.strip() for g in gates_input.split(',') if g.strip()]
			for gate in gates:
				if gate == 'x':
					self.qc.x(i)
				elif gate == 'h':
					self.qc.h(i)
				elif gate == 'id':
					self.qc.id(i)
				elif gate == 'y':
					self.qc.y(i)
				elif gate == 'z':
					self.qc.z(i)
				elif gate == 's':
					self.qc.s(i)
				elif gate == 't':
					self.qc.t(i)
				elif gate in ('rx', 'ry', 'rz'):
					try:
						deg = float(input(f"Enter angle in degrees for {gate} on qubit {i}: "))
						rad = math.radians(deg)
						if gate == 'rx':
							self.qc.rx(rad, i)
						elif gate == 'ry':
							self.qc.ry(rad, i)
						elif gate == 'rz':
							self.qc.rz(rad, i)
					except ValueError:
						print("Invalid angle, skipping.")
				elif gate == 'cx':
					try:
						target = int(input(f"You selected CNOT for qubit {i} as control. Enter target qubit (0 to {self.n-1}, not {i}): "))
						if target != i and 0 <= target < self.n:
							self.qc.cx(i, target)
						else:
							print("Invalid target qubit for CNOT.")
					except ValueError:
						print("Invalid input for target qubit.")
				elif gate == 'none' or gate == '':
					continue
				else:
					print(f"Unknown gate '{gate}', skipping on qubit {i}.")

	def finalize_and_save(self):
		self.qc.measure(range(self.n), range(self.n))
		qasm = qiskit.qasm2.dumps(self.qc)
		print("\nGenerated QASM:\n")
		print(qasm)

		qiskit.qasm2.dump(self.qc, "myfile.qasm")
		print("QASM saved to myfile.qasm")

		circuit = qiskit.qasm2.load("myfile.qasm")
		print("\nLoaded circuit from QASM:")
		print(circuit)

	def run(self):
		print("Welcome to the Interactive QASM Builder!")
		self.prompt_qubits()
		self.prompt_gates()
		self.finalize_and_save()

if __name__ == "__main__":
	builder = InteractiveQASMBuilder()
	builder.run()