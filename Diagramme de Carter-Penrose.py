import numpy as np
import matplotlib.pyplot as plt

def penrose_transform(t, r):
    """Applique la transformation conforme d'écrasement avec arctan"""
    u = t + r
    v = t - r
    U = np.arctan(u)
    V = np.arctan(v)
    T = (U + V) / 2
    R = (U - V) / 2
    return R, T

plt.figure(figsize=(7, 7))

# Tracé des lignes à temps constant mais pour r qui varie
valeurs_t = np.linspace(-10, 10, 15)
r_line = np.linspace(0, 20, 200) # pour uniquement tracer la moitié droite du diamant où r > 0
for t_val in valeurs_t:
    R, T = penrose_transform(t_val, r_line)
    plt.plot(R, T, color='royalblue', alpha=0.5, linewidth=1)

# Tracé des lignes à rayon constant mais pour t qui varie
valeurs_r = np.linspace(0.1, 10, 15)
t_line = np.linspace(-20, 20, 200)
for r_val in valeurs_r:
    R, T = penrose_transform(t_line, r_val)
    plt.plot(R, T, color='firebrick', alpha=0.5, linewidth=1)

R_boundary, T_boundary = penrose_transform(t_line, 0) # Origine r=0
plt.plot(R_boundary, T_boundary, color='black', linewidth=2)

plt.plot([0, np.pi/4], [np.pi/4, 0], color='black', linewidth=2, linestyle='--', label=r'Infini futur $\mathscr{I}^+$ (Surface $\mathcal{X}$)')
plt.plot([0, np.pi/4], [-np.pi/4, 0], color='black', linewidth=2)

plt.title("Diagramme de Carter-Penrose (Diamant de Minkowski)", fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.axis('equal')
plt.axis('off')

plt.tight_layout()
plt.savefig('diagramme_penrose.png', dpi=300)
plt.show()