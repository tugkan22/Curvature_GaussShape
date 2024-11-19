import sympy as sp

# Define variables
t = sp.Symbol('t')  # Parameter for curve
u, v = sp.symbols('u v')  # Parameters for surface

def calculate_curve_curvature():
    print("Eğriyi tanımlayın (x(t), y(t), z(t)):")
    x = sp.sympify(input("x(t): "))
    y = sp.sympify(input("y(t): "))
    z = sp.sympify(input("z(t): "))

    # Define the curve
    r = sp.Matrix([x, y, z])
    r_prime = r.diff(t)
    r_double_prime = r_prime.diff(t)
    r_cross = r_prime.cross(r_double_prime)

    # Calculate curvature
    curvature = sp.simplify(r_cross.norm() / r_prime.norm()**3)
    print("\nEğrinin Eğriliği (k(t)): ")
    print(curvature)

def calculate_surface_curvatures():
    print("Yüzeyi tanımlayın (z = f(u, v)):")
    f = sp.sympify(input("f(u, v): "))

    # First derivatives
    fx = sp.diff(f, u)
    fy = sp.diff(f, v)

    # First fundamental form coefficients
    E = 1 + fx**2
    F = fx * fy
    G = 1 + fy**2

    # Second derivatives
    fxx = sp.diff(fx, u)
    fyy = sp.diff(fy, v)
    fxy = sp.diff(fx, v)

    # Second fundamental form coefficients
    L = fxx / sp.sqrt(E)
    M = fxy / sp.sqrt(E)
    N = fyy / sp.sqrt(G)

    # Gauss and mean curvature
    gauss_curvature = sp.simplify((L * N - M**2) / (E * G - F**2))
    mean_curvature = sp.simplify((E * N + G * L - 2 * F * M) / (2 * (E * G - F**2)))

    print("\nGauss Eğriliği (K): ")
    print(gauss_curvature)
    print("\nOrtalama Eğrilik (H): ")
    print(mean_curvature)

# Main program
def main():
    print("Hangi hesaplamayı yapmak istersiniz?")
    print("1. Eğrinin Eğriliği")
    print("2. Yüzeyin Gauss ve Ortalama Eğriliği")
    choice = input("Seçiminizi yapın (1/2): ")

    if choice == '1':
        calculate_curve_curvature()
    elif choice == '2':
        calculate_surface_curvatures()
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
