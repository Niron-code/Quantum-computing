"""
This example demonstrates how to implement a custom quantum gate in Qiskit
using a unitary matrix and assign a custom label to it for clarity in circuit
diagrams.

- Define a 2x2 unitary matrix representing the Pauli-X operation.
- The matrix is wrapped in Qiskit's UnitaryGate class, which allows it to be
  appended to a quantum circuit like any other gate.
- A custom label ("Philip") is provided when creating the UnitaryGate so that
  the gate is displayed with this name in circuit drawings instead of the
  generic "unitary".

The resulting circuit prepares the Bell state |Ψ+> by applying a Hadamard,
CNOT, SWAP, the custom "Philip" gate, and a controlled-Z before measurement.
"""


from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector
import numpy as np

# --- Build circuit producing |Ψ+> = (|01> + |10>)/√2 ---
qc = QuantumCircuit(2, 2)

# Custom 1-qubit unitary (Pauli-X)
custom_unitary = np.array([[0, 1],
                           [1, 0]], dtype=complex)
custom_gate = UnitaryGate(custom_unitary, label="Philip")

qc.h(0)
qc.cx(0, 1)
qc.swap(0, 1)               # has no effect on |Φ+>, included for demo
qc.append(custom_gate, [0]) # X on qubit 0 → |Ψ+>
qc.cz(0, 1)                 # no |11> amplitude → no phase flip

# Measurements
qc.measure([0, 1], [0, 1])

print("Circuit:")
print(qc)

# --- Statevector (remove measurements first) ---
pure_qc = qc.remove_final_measurements(inplace=False)
sv_backend = Aer.get_backend("statevector_simulator")
sv_result = sv_backend.run(pure_qc).result()
sv = sv_result.get_statevector()

print("\nStatevector [|00>, |01>, |10>, |11>]:")
print(sv)

# --- Verify equals |Ψ+> ---

# Method A: using Qiskit's Statevector.equiv (phase-insensitive)
target_sv = Statevector([0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
assert sv.equiv(target_sv), "State is not |Ψ+> up to global phase"
print("\n✓ Verified with Statevector.equiv: final state is |Ψ+> (up to global phase)")

# Method B: manual phase-insensitive numeric check
sv_array = np.array(sv)  # convert to NumPy for element-wise ops
target_array = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0], dtype=complex)
phase = sv_array[np.argmax(np.abs(sv_array))] / target_array[np.argmax(np.abs(target_array))]
assert np.allclose(sv_array, phase * target_array, atol=1e-8), "Numeric check failed"
print("✓ Verified with numeric check: final state is |Ψ+> (up to global phase)")

# --- Shot-based simulation on qasm_simulator ---
qasm_backend = Aer.get_backend("qasm_simulator")
job = qasm_backend.run(qc, shots=2048, seed_simulator=1234)  # transpile happens internally
result = job.result()
counts = result.get_counts()

print("\nCounts (~50/50 for '01' and '10'):")
print(counts)
