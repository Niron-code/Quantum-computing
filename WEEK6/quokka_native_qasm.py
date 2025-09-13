"""
Quokka QASM Generator
---------------------
This script interactively builds a quantum circuit and generates a QASM file compatible with the Quokka simulator.

Features:
- Prompts the user for the number of qubits.
- For each qubit, allows entry of multiple gates (x, h, id, y, z, s, t, rx, ry, rz, cx) separated by commas.
- For rx, ry, rz gates, prompts for an angle in degrees and applies the rotation.
- For cx (CNOT), prompts for the target qubit.
- Generates a QASM file named 'quokka.qasm' WITHOUT the 'include "qelib1.inc";' line (for Quokka compatibility).

Usage:
    python quokka_native_qasm.py

Requirements:
    - qiskit
"""

import math
import qiskit.qasm2
from qiskit.circuit import QuantumCircuit

def main():
    print("Welcome to the Quokka QASM Generator!")
    n = int(input("How many qubits do you want? "))
    qc = QuantumCircuit(n, n)

    print("Available gates: x, h, id, y, z, s, t, rx, ry, rz, cx (CNOT)")
    for i in range(n):
        gates_input = input(f"Which gate(s) to apply to qubit {i}? (comma separated, e.g. x,h,rx): ").strip().lower()
        gates = [g.strip() for g in gates_input.split(',') if g.strip()]
        for gate in gates:
            if gate == 'x':
                qc.x(i)
            elif gate == 'h':
                qc.h(i)
            elif gate == 'id':
                qc.id(i)
            elif gate == 'y':
                qc.y(i)
            elif gate == 'z':
                qc.z(i)
            elif gate == 's':
                qc.s(i)
            elif gate == 't':
                qc.t(i)
            elif gate in ('rx', 'ry', 'rz'):
                try:
                    deg = float(input(f"Enter angle in degrees for {gate} on qubit {i}: "))
                    rad = math.radians(deg)
                    if gate == 'rx':
                        qc.rx(rad, i)
                    elif gate == 'ry':
                        qc.ry(rad, i)
                    elif gate == 'rz':
                        qc.rz(rad, i)
                except ValueError:
                    print("Invalid angle, skipping.")
            elif gate == 'cx':
                try:
                    target = int(input(f"You selected CNOT for qubit {i} as control. Enter target qubit (0 to {n-1}, not {i}): "))
                    if target != i and 0 <= target < n:
                        qc.cx(i, target)
                    else:
                        print("Invalid target qubit for CNOT.")
                except ValueError:
                    print("Invalid input for target qubit.")
            elif gate == 'none' or gate == '':
                continue
            else:
                print(f"Unknown gate '{gate}', skipping on qubit {i}.")

    qc.measure(range(n), range(n))
    qasm = qiskit.qasm2.dumps(qc)
    # Remove the include line for Quokka compatibility
    qasm = qasm.replace('include "qelib1.inc";\n', '')
    with open("quokka.qasm", "w") as f:
        f.write(qasm)
    print("QASM for Quokka saved to quokka.qasm (without include line)")

if __name__ == "__main__":
    main()
