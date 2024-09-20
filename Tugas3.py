import math

# Fungsi f(x) = x * e^(-x) + cos(2x)
def f(x):
    return x * math.exp(-x) + math.cos(2 * x)

# Turunan dari f(x), yaitu f'(x)
def df(x):
    return math.exp(-x) * (1 - x) - 2 * math.sin(2 * x)

# Metode Newton-Raphson
def newton_raphson(x0, tol, max_iter=100):
    iterasi = 0
    while iterasi < max_iter:
        iterasi += 1
        f_x0 = f(x0)
        df_x0 = df(x0)
        
        # Periksa jika turunan mendekati nol, untuk menghindari pembagian dengan nol
        if abs(df_x0) < 1e-10:
            print("Turunan mendekati nol, metode gagal.")
            return None
        
        # Newton-Raphson iterasi
        x1 = x0 - f_x0 / df_x0
        
        # Print proses setiap iterasi
        print(f"Iterasi {iterasi}: x0 = {x0:.6f}, f(x0) = {f_x0:.6f}, df(x0) = {df_x0:.6f}, x1 = {x1:.6f}")
        
        # Periksa jika sudah konvergen
        if abs(x1 - x0) < tol:
            return x1
        
        x0 = x1  # Update nilai x0 untuk iterasi berikutnya

    print("Metode Newton-Raphson tidak konvergen setelah jumlah iterasi maksimal.")
    return None

# Parameter awal
x0 = 0.176281  # Nilai awal yang diberikan
tolerance = 1e-6  # Toleransi untuk solusi yang diinginkan

# Menjalankan metode Newton-Raphson
akar = newton_raphson(x0, tolerance)

if akar is not None:
    print(f"\nAkar yang ditemukan adalah: {akar:.6f}")
else:
    print("\nTidak ditemukan akar yang konvergen.")
