import matplotlib.pyplot as plt

class ComplexCalculator:
    def __init__(self, z1=None, z2=None):
        self.z1 = z1
        self.z2 = z2
        self.results = {}

    def get_complex(self, prompt):
        real = float(input(f"Enter real part of {prompt}: "))
        imag = float(input(f"Enter imaginary part of {prompt}: "))
        return complex(real, imag)

    def compute(self):
        self.results['add'] = self.z1 + self.z2
        self.results['sub'] = self.z1 - self.z2
        self.results['mul'] = self.z1 * self.z2
        self.results['div'] = self.z1 / self.z2 if self.z2 != 0 else None

    def display_results(self):
        print(f"\nAlgebraic Results:")
        print(f"z1 = {self.z1}")
        print(f"z2 = {self.z2}")
        print(f"z1 + z2 = {self.results['add']}")
        print(f"z1 - z2 = {self.results['sub']}")
        print(f"z1 * z2 = {self.results['mul']}")
        div = self.results['div']
        print(f"z1 / z2 = {div if div is not None else 'undefined (division by zero)'}")

    def plot_vectors(self):
        vectors = [self.z1, self.z2, self.results['add'], self.results['sub'], self.results['mul']]
        labels = ['z1', 'z2', 'z1+z2', 'z1-z2', 'z1*z2']
        colors = ['blue', 'green', 'orange', 'red', 'purple']

        if self.results['div'] is not None:
            vectors.append(self.results['div'])
            labels.append('z1/z2')
            colors.append('brown')

        plt.figure(figsize=(8, 8))
        ax = plt.gca()
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.set_aspect('equal')
        plt.grid(True, which='both')

        for v, label, color in zip(vectors, labels, colors):
            plt.arrow(0, 0, v.real, v.imag, head_width=0.3, head_length=0.5, fc=color, ec=color, length_includes_head=True)
            plt.text(v.real, v.imag, f' {label}', color=color, fontsize=12)

        plt.xlabel('Real')
        plt.ylabel('Imaginary')
        plt.title('Complex Number Operations')
        plt.legend(labels)
        plt.show()

def main():
    print("Enter two complex numbers (rectangular form: a + bj)")
    calc = ComplexCalculator()
    calc.z1 = calc.get_complex("z1")
    calc.z2 = calc.get_complex("z2")
    calc.compute()
    calc.display_results()
    calc.plot_vectors()

if __name__ == "__main__":
    main()