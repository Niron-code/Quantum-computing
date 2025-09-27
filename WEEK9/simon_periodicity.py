
# simon_periodicity.py
# This script collects a function table for Simon's problem, constructs the corresponding Uf matrix,
# and prints it with basis state labels for visualization and analysis.

def get_user_inputs():

    # Step 1: ask for n (number of qubits)
    n = int(input("Enter the number of qubits (n): ").strip())
    print(f"Selected n = {n}")

    # Step 2: ask for f(x) values
    # For n input qubits, we have 2^n possible x values
    num_x = 1 << n  # 2^n
    print(f"\nNow enter f(x) values for each of the {num_x} inputs.")
    print("Each f(x) should be an n-bit string (e.g., 00, 01, 10, 11 for n=2) or a 1-bit string (e.g., 0, 1).")

    f_map = {}  # Dictionary to store the function table: x_bits -> f(x)
    for x in range(num_x):
        x_bits = format(x, f"0{n}b")  # binary string padded to n bits
        fx_str = input(f"f({x_bits}) = ").strip()
        # Accept either n-bit or 1-bit binary string
        if (len(fx_str) != n and len(fx_str) != 1) or any(c not in "01" for c in fx_str):
            raise ValueError(f"Invalid entry for f({x_bits}). Must be {n}-bit or 1-bit binary string.")
        f_map[x_bits] = fx_str

    # Print the collected function table
    print("\nCollected function table:")
    for x_bits, fx_str in f_map.items():
        print(f"f({x_bits}) = {fx_str}")

    return n, f_map

if __name__ == "__main__":

    n, f_map = get_user_inputs()

    # Build and print the Uf matrix for Simon's problem
    import numpy as np
    num_bits = n * 2  # Total number of bits for |x, y> basis
    dim = 1 << num_bits  # Dimension of the Uf matrix: 2^(2n)
    Uf = np.zeros((dim, dim), dtype=int)  # Initialize the Uf matrix with zeros

    # For each basis state |x, y> (x, y are n-bit strings)
    for i in range(dim):
        # i encodes (x, y) as a 2n-bit string
        bits = format(i, f"0{num_bits}b")  # Convert i to a 2n-bit binary string
        x_bits = bits[:n]  # First n bits are x
        y_bits = bits[n:]  # Last n bits are y
        fx = f_map[x_bits]  # Get f(x) from the function table
        # Pad f(x) to n bits if needed (for 1-bit outputs)
        if len(fx) < n:
            fx = fx.zfill(n)
        # Compute y XOR f(x)
        y_fx = format(int(y_bits, 2) ^ int(fx, 2), f"0{n}b")
        # The output basis state is |x, y XOR f(x)>
        j_bits = x_bits + y_fx
        j = int(j_bits, 2)  # Convert the output basis to an integer index
        Uf[j, i] = 1  # Set the corresponding matrix element to 1

    # Set numpy print options to show the full matrix
    np.set_printoptions(threshold=np.inf, linewidth=200)
    print(f"\nUf matrix ({dim}x{dim}) ")

    # Prepare labels for basis states (2n-bit binary strings)
    labels = [format(i, f"0{num_bits}b") for i in range(dim)]
    col_width = max(num_bits, 4) + 2  # 2n bits + padding for alignment
    # Print header row with column labels
    print(" ".ljust(col_width), end="")
    for col_label in labels:
        print(col_label.ljust(col_width), end="")
    print()
    # Print each row with its label and matrix values
    for i, row in enumerate(Uf):
        print(labels[i].ljust(col_width), end="")
        for val in row:
            print(f"{val}".center(col_width), end="")
        print()
