import numpy as np
import matplotlib.pyplot as plt

# Curva 1 - Parametrização 2D
t = np.linspace(0, 2 * np.pi, 1000)  # t de 0 a 2pi com 1000 pontos
x = np.sin(t) + 0.5 * np.cos(5*t) + 0.25 * np.sin(13*t)  # fórmula de x
y = np.cos(t) + 0.5 * np.sin(5*t) + 0.25 * np.cos(13*t)  # fórmula de y

plt.figure(figsize=(8, 6))  # cria a figura 2D
plt.plot(x, y, label="Curva Parametrizada")  # plota a curva
plt.xlabel("x")
plt.ylabel("y")
plt.title("Curva Parametrizada")
plt.legend()  # adiciona legenda
plt.grid(True)  # ativa o grid

# Curva 2 - Hélice Circular (tipo mola)
t_helix = np.linspace(0, 20 * np.pi, 1000)  # t pra 10 voltas (0 a 20pi)
x_helix = np.cos(t_helix)  # componente x
y_helix = np.sin(t_helix)  # componente y
z_helix = t_helix / (2 * np.pi)  # componente z: sobe 1 cm por volta

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')  # subplot 3D
ax.plot(x_helix, y_helix, z_helix, label="Hélice Circular")  # plota a hélice
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z (cm)")
ax.set_title("Hélice Circular (10 voltas, 10 cm de altura)")
ax.legend()  # legenda 3D
ax.grid(True)  # ativa o grid no 3D

plt.show()  # mostra os gráficos
