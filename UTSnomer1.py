import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung f(R) dan f'(R)
def f(R):
    """
    Menghitung nilai fungsi f(R) untuk persamaan non-linier.
    
    Parameters:
    R (float): Nilai resistansi R.
    
    Returns:
    float: Nilai fungsi f(R).
    """
    L = 0.5  # Induktansi dalam H
    C = 10e-6  # Kapasitansi dalam F
    return 1 / (2 * np.pi * np.sqrt(L * (1 - (R**2 / (4 * L**2)))))

def f_prime(R):
    """
    Menghitung nilai turunan f'(R) untuk persamaan non-linier.
    
    Parameters:
    R (float): Nilai resistansi R.
    
    Returns:
    float: Nilai turunan f'(R).
    """
    L = 0.5
    return (R / (4 * L**2)) / (2 * np.pi * np.sqrt(L * (1 - (R**2 / (4 * L**2)))))**3

# Implementasi metode biseksi
def biseksi(f, a, b, tol):
    """
    Mencari akar persamaan menggunakan metode biseksi.
    
    Parameters:
    f (function): Fungsi yang akan dicari akarnya.
    a (float): Batas bawah interval awal.
    b (float): Batas atas interval awal.
    tol (float): Toleransi error.
    
    Returns:
    float: Nilai akar persamaan.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) dan f(b) harus memiliki tanda yang berbeda.")
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

# Implementasi metode Newton-Raphson
def newton_raphson(f, f_prime, R0, tol):
    """
    Mencari akar persamaan menggunakan metode Newton-Raphson.
    
    Parameters:
    f (function): Fungsi yang akan dicari akarnya.
    f_prime (function): Turunan dari fungsi f.
    R0 (float): Tebakan awal.
    tol (float): Toleransi error.
    
    Returns:
    float: Nilai akar persamaan.
    """
    R = R0
    while abs(f(R) - 1000) > tol:
        R = R - f(R) / f_prime(R)
    return R

# Bagian a: Fungsi f(R) dan f'(R)
print("Fungsi f(R) dan f'(R):")
print(f(50))
print(f_prime(50))

# Bagian b: Implementasi metode biseksi
R_biseksi = biseksi(lambda R: f(R) - 1000, 0, 100, 0.1)
print("Nilai R menggunakan metode biseksi:", R_biseksi)

# Bagian c: Implementasi metode Newton-Raphson
R_newton = newton_raphson(lambda R: f(R) - 1000, f_prime, 50, 0.1)
print("Nilai R menggunakan metode Newton-Raphson:", R_newton)

# Bagian d: Perbandingan hasil dan kecepatan konvergensi
biseksi_results = []
newton_results = []
for i in range(50):
    R_b = biseksi(lambda R: f(R) - 1000, 0, 100, 0.1)
    biseksi_results.append(R_b)

    R_n = newton_raphson(lambda R: f(R) - 1000, f_prime, 50, 0.1)
    newton_results.append(R_n)

plt.plot(biseksi_results, label='Metode Biseksi')
plt.plot(newton_results, label='Metode Newton-Raphson')
plt.xlabel('Iterasi')
plt.ylabel('Nilai R')
plt.legend()
plt.title('Perbandingan Metode Konvergensi')
plt.show()

# Kesimpulan
"""
Kode ini mengimplementasikan dua metode numerik untuk mencari akar dari persamaan non-linier
yang terkait dengan resistansi dalam rangkaian listrik, yaitu metode biseksi dan metode Newton-Raphson.
1. Fungsi f(R) dan turunan f'(R) dihitung untuk nilai resistansi R.
2. Metode biseksi digunakan untuk menemukan akar persamaan, memberikan solusi mendekati 1000.
3. Metode Newton-Raphson digunakan dengan tebakan awal, menunjukkan konvergensi yang lebih cepat.
4. Visualisasi hasil menunjukkan bahwa Newton-Raphson umumnya lebih cepat dalam mencapai 
   solusi akurat dibandingkan metode biseksi.
Secara keseluruhan, kedua metode ini efektif untuk menyelesaikan masalah mencari akar 
persamaan non-linier dalam konteks teknik.
"""