import numpy as np
import matplotlib.pyplot as plt

def polar_to_rectangular(r, theta):
    """Convert from polar (r, theta) to rectangular (x, y) coordinates."""
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def rectangular_to_polar(x, y):
    """Convert from rectangular (x, y) to polar (r, theta) coordinates."""
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

def plot_vector(x, y, r=None, theta=None, title="Complex Number Representation"):
    """Plot the vector in both rectangular and polar form."""
    plt.figure(figsize=(8, 8))
    
    # Create the plot
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    # Plot the vector
    plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='blue',
              label=f'Vector: ({x:.2f}, {y:.2f})')
    
    # Add circle if polar coordinates are provided
    if r is not None:
        circle = plt.Circle((0, 0), r, fill=False, linestyle='--', color='gray')
        ax.add_artist(circle)
    
    # Add angle arc if polar coordinates are provided
    if theta is not None:
        angle = np.linspace(0, theta, 100)
        arc_x = 0.5 * np.cos(angle)
        arc_y = 0.5 * np.sin(angle)
        plt.plot(arc_x, arc_y, 'r--', label=f'θ = {np.degrees(theta):.2f}°')
    
    # Set equal aspect ratio and add grid
    plt.axis('equal')
    plt.grid(True)
    
    # Add labels and title
    plt.xlabel('Real (x)')
    plt.ylabel('Imaginary (y)')
    plt.title(title)
    plt.legend()
    
    # Show the plot
    plt.show()

def main():
    while True:
        print("\nComplex Number Conversion")
        print("1. Polar to Rectangular")
        print("2. Rectangular to Polar")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            print("Exiting the program.")
            break
            
        elif choice == '1':
            r = float(input("Enter magnitude (r): "))
            theta_deg = float(input("Enter angle in degrees (θ): "))
            theta_rad = np.radians(theta_deg)
            
            x, y = polar_to_rectangular(r, theta_rad)
            print(f"\nRectangular form: ({x:.2f}, {y:.2f})")
            plot_vector(x, y, r, theta_rad, "Polar to Rectangular Conversion")
            
        elif choice == '2':
            x = float(input("Enter x coordinate: "))
            y = float(input("Enter y coordinate: "))
            
            r, theta = rectangular_to_polar(x, y)
            print(f"\nPolar form: (r = {r:.2f}, θ = {np.degrees(theta):.2f}°)")
            plot_vector(x, y, r, theta, "Rectangular to Polar Conversion")
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()