import numpy as np

def gauss_eliminasi(A, b):
    """
    Fungsi untuk menyelesaikan sistem persamaan linier menggunakan metode eliminasi Gauss.
    
    Parameters:
    A (list): Matriks koefisien.
    b (list): Vektor konstanta.
    
    Returns:
    np.ndarray: Solusi dari sistem persamaan.
    """
    n = len(b)
    for i in range(n):
        # Mencari pivot dan menukarnya jika diperlukan
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[i][i]):
                A[i], A[k] = A[k], A[i]
                b[i], b[k] = b[k], b[i]
        
        # Eliminasi
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]

    # Menghitung solusi dengan substitusi balik
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i + 1:], x[i + 1:])) / A[i][i]
    return x

# Matriks koefisien dan vektor konstanta
A = np.array([[4, -1, -1], [-1, 3, -1], [-1, -1, 5]], dtype=float)
b = np.array([5, 3, 4], dtype=float)

# Menyelesaikan sistem persamaan menggunakan metode eliminasi Gauss
solusi_gauss = gauss_eliminasi(A.tolist(), b.tolist())
print("Solusi menggunakan metode eliminasi Gauss:", solusi_gauss)

def determinan(A):
    """
    Fungsi untuk menghitung determinan matriks.
    
    Parameters:
    A (np.ndarray): Matriks yang akan dihitung determinannya.
    
    Returns:
    float: Nilai determinan dari matriks A.
    """
    return np.linalg.det(A)

# Menghitung determinan matriks A
det_A = determinan(A)
print("Determinan matriks A:", det_A)

def gauss_jordan(A, b):
    """
    Fungsi untuk menyelesaikan sistem persamaan linier menggunakan metode Gauss-Jordan.
    
    Parameters:
    A (np.ndarray): Matriks koefisien.
    b (np.ndarray): Vektor konstanta.
    
    Returns:
    np.ndarray: Solusi dari sistem persamaan.
    """
    n = len(b)
    A = np.hstack([A, b.reshape(-1, 1)])  # Gabungkan A dan b
    for i in range(n):
        # Normalisasi pivot
        A[i] = A[i] / A[i][i]
        for j in range(n):
            if i != j:
                A[j] -= A[j][i] * A[i]
    return A[:, -1]

# Menyelesaikan sistem persamaan menggunakan metode Gauss-Jordan
solusi_gauss_jordan = gauss_jordan(A.copy(), b.copy())
print("Solusi menggunakan metode Gauss-Jordan:", solusi_gauss_jordan)

def invers_matriks(A):
    """
    Fungsi untuk menghitung invers matriks.
    
    Parameters:
    A (np.ndarray): Matriks yang akan dihitung inversnya.
    
    Returns:
    np.ndarray: Invers dari matriks A.
    """
    return np.linalg.inv(A)

# Menghitung invers matriks A
invers_A = invers_matriks(A)
print("Invers matriks A:\n", invers_A)

# Kesimpulan
"""
Kode ini menyelesaikan sistem persamaan linier menggunakan tiga metode: eliminasi Gauss, Gauss-Jordan,
dan menghitung invers matriks. Metode eliminasi Gauss dan Gauss-Jordan memberikan solusi yang konsisten
untuk sistem persamaan yang diberikan. Selain itu, determinan dan invers matriks dihitung, yang berguna
untuk analisis lebih lanjut dalam konteks sistem persamaan. Ketiga metode ini merupakan alat penting dalam
aljabar linier untuk memecahkan masalah yang melibatkan sistem persamaan.
"""