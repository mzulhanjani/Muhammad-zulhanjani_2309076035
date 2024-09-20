import math
def f(x):
    return x * math.exp(-x) + 1
def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Metode biseksi gagal. f(a) dan f(b) harus bertanda berbeda.")
        return None

    iterasi = 0
    print(f"{'Iterasi':<10} {'a':<10} {'b':<10} {'midpoint':<15} {'f(midpoint)':<15}")
    while (b - a) / 2.0 > tol:
        iterasi += 1
        midpoint = (a + b) / 2.0
        f_mid = f(midpoint)
        print(f"{iterasi:<10} {a:<10.6f} {b:<10.6f} {midpoint:<15.6f} {f_mid:<15.6f}")
        if f_mid == 0:  
            return midpoint
        elif f(a) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2.0
a = -1
b = 0
tolerance = 1e-6
root = bisection_method(a, b, tolerance)

if root is not None:
    print(f"\nAkar persamaan adalah: {root:.6f}")
else:
    print("\nTidak ditemukan akar dalam interval yang diberikan.")
