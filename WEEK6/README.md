# WEEK6 Quantum Circuit Tools

This folder contains interactive tools for building and exporting quantum circuits in QASM format.

## Scripts and Classes

### InteractiveQASMBuilder (interactive_qasm_builder.py)
- An interactive Python class and script for building quantum circuits step-by-step.
- Prompts the user for the number of qubits and which gates to apply to each qubit (supports x, h, id, y, z, s, t, rx, ry, rz, cx).
- Allows multiple gates per qubit and supports custom rotation angles.
- Prints the generated QASM, saves it to `myfile.qasm`, and displays the circuit.
- Useful for learning, prototyping, and exporting QASM for general simulators.

### Quokka QASM Generator (quokka.qasm)
- An interactive script for building quantum circuits and exporting QASM files compatible with the Quokka simulator.
- Prompts for qubits and gates like the above, but only generates the QASM file (`quokka.qasm`) without the `include "qelib1.inc";` line (required by Quokka).
- Does not print the circuit diagram, focusing on QASM output for Quokka compatibility.

---

Use these tools to quickly create and export quantum circuits for simulation and experimentation.
