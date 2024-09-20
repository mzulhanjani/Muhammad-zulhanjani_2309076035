import matplotlib.pyplot as plt # type: ignore

# Data dari tabel
x = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0]
f_x = [-0.63212, -0.54881, -0.44933, -0.33287, -0.19738, 0.0, 0.19738, 0.33287, 0.44933, 0.54881, 1.0]

# Membuat plot
plt.plot(x, f_x, marker='o')

# Menambahkan judul dan label
plt.title('Plot dari Data Tabel')
plt.xlabel('x')
plt.ylabel('f(x)')

# Menampilkan plot
plt.grid(True)
plt.show()
