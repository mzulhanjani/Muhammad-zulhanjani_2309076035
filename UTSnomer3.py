import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung nilai R(T)
def R(T):
    """
    Menghitung nilai R(T) berdasarkan persamaan yang diberikan.
    
    Parameters:
    T (float): Temperatur dalam Kelvin.
    
    Returns:
    float: Nilai R(T).
    """
    return 5000 * np.exp(3500 * (1/T - 1/298))

# Fungsi untuk menghitung diferensiasi maju
def diferensiasi_maju(R, T, h):
    """
    Menghitung nilai turunan dR/dT menggunakan metode diferensiasi maju.
    
    Parameters:
    R (function): Fungsi untuk menghitung nilai R(T).
    T (float): Temperatur dalam Kelvin.
    h (float): Perubahan temperatur.
    
    Returns:
    float: Nilai dR/dT menggunakan metode diferensiasi maju.
    """
    return (R(T + h) - R(T)) / h

# Fungsi untuk menghitung diferensiasi mundur
def diferensiasi_mundur(R, T, h):
    """
    Menghitung nilai turunan dR/dT menggunakan metode diferensiasi mundur.
    
    Parameters:
    R (function): Fungsi untuk menghitung nilai R(T).
    T (float): Temperatur dalam Kelvin.
    h (float): Perubahan temperatur.
    
    Returns:
    float: Nilai dR/dT menggunakan metode diferensiasi mundur.
    """
    return (R(T) - R(T - h)) / h

# Fungsi untuk menghitung diferensiasi tengah
def diferensiasi_tengah(R, T, h):
    """
    Menghitung nilai turunan dR/dT menggunakan metode diferensiasi tengah.
    
    Parameters:
    R (function): Fungsi untuk menghitung nilai R(T).
    T (float): Temperatur dalam Kelvin.
    h (float): Perubahan temperatur.
    
    Returns:
    float: Nilai dR/dT menggunakan metode diferensiasi tengah.
    """
    return (R(T + h) - R(T - h)) / (2 * h)

# Contoh penggunaan
T = 300
h = 0.01

dR_dT_maju = diferensiasi_maju(R, T, h)
dR_dT_mundur = diferensiasi_mundur(R, T, h)
dR_dT_tengah = diferensiasi_tengah(R, T, h)

print("dR/dT (maju):", dR_dT_maju)
print("dR/dT (mundur):", dR_dT_mundur)
print("dR/dT (tengah):", dR_dT_tengah)

# Fungsi untuk menghitung dR/dT secara eksak
def dR_dT_eksak(T):
    """
    Menghitung nilai turunan dR/dT secara eksak.
    
    Parameters:
    T (float): Temperatur dalam Kelvin.
    
    Returns:
    float: Nilai dR/dT secara eksak.
    """
    return -3500 * 5000 * np.exp(3500 * (1/T - 1/298)) / (T**2)

dR_dT_eksak_value = dR_dT_eksak(T)
print("dR/dT (eksak):", dR_dT_eksak_value)

# Menghitung error relatif untuk setiap metode diferensiasi
temperatures = np.arange(250, 360, 10)
errors_maju, errors_mundur, errors_tengah = [], [], []

for T in temperatures:
    dR_maju = diferensiasi_maju(R, T, h)
    dR_mundur = diferensiasi_mundur(R, T, h)
    dR_tengah = diferensiasi_tengah(R, T, h)
    
    errors_maju.append(abs(dR_maju - dR_dT_eksak(T)) / dR_dT_eksak(T))
    errors_mundur.append(abs(dR_mundur - dR_dT_eksak(T)) / dR_dT_eksak(T))
    errors_tengah.append(abs(dR_tengah - dR_dT_eksak(T)) / dR_dT_eksak(T))

print("Error relatif (maju):", errors_maju)
print("Error relatif (mundur):", errors_mundur)
print("Error relatif (tengah):", errors_tengah)

# Plot error relatif
plt.plot(temperatures, errors_maju, label='Error Relatif Maju')
plt.plot(temperatures, errors_mundur, label='Error Relatif Mundur')
plt.plot(temperatures, errors_tengah, label='Error Relatif Tengah')
plt.xlabel('Temperatur (K)')
plt.ylabel('Error Relatif')
plt.legend()
plt.title('Error Relatif Metode Diferensiasi')
plt.show()

# Fungsi untuk menghitung dR/dT dengan ekstrapolasi Richardson
def richardson_extrapolation(R, T, h):
    """
    Menghitung nilai turunan dR/dT menggunakan metode ekstrapolasi Richardson.
    
    Parameters:
    R (function): Fungsi untuk menghitung nilai R(T).
    T (float): Temperatur dalam Kelvin.
    h (float): Perubahan temperatur.
    
    Returns:
    float: Nilai dR/dT dengan ekstrapolasi Richardson.
    """
    dR_h = diferensiasi_tengah(R, T, h)
    dR_h2 = diferensiasi_tengah(R, T, h / 2)
    return (4 * dR_h2 - dR_h) / 3

dR_richardson = richardson_extrapolation(R, T, h)
print("dR/dT dengan extrapolasi Richardson:", dR_richardson)