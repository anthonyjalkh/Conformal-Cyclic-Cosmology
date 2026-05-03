import numpy as np
import matplotlib.pyplot as plt


def plot_conformal_grid(ax, omega_factor, title):
    x = np.linspace(-5, 5, 11)
    y = np.linspace(-5, 5, 11)

    # Redimensionnement conforme
    x_scaled = x * omega_factor
    y_scaled = y * omega_factor

    # Grille
    for i in x_scaled:
        ax.plot([i, i], [min(y_scaled), max(y_scaled)], color='blue', alpha=0.3)
    for j in y_scaled:
        ax.plot([min(x_scaled), max(x_scaled)], [j, j], color='blue', alpha=0.3)

    # Ajout d'une perturbation qui est le cercle représentant un Hawking Point
    theta = np.linspace(0, 2 * np.pi, 100)
    radius = 2 * omega_factor
    circle_x = radius * np.cos(theta)
    circle_y = radius * np.sin(theta)
    ax.plot(circle_x, circle_y, color='red', linewidth=2, label='Onde Gravitationnelle')

    # Angle droit pour prouver la conservation des angles
    center_x, center_y = x_scaled[5], y_scaled[5]  # Centre
    ax.plot([center_x, center_x + omega_factor], [center_y, center_y], color='black', lw=2)
    ax.plot([center_x, center_x], [center_y, center_y + omega_factor], color='black', lw=2)
    ax.text(center_x + 0.2, center_y + 0.2, '90°', fontsize=12, fontweight='bold')

    ax.set_aspect('equal')
    ax.set_title(title, pad =  15)
    ax.legend(loc='upper right')


# Avant et après
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

plot_conformal_grid(ax1, omega_factor=1.0, title="Métrique Physique (Avant singularité)")
plot_conformal_grid(ax2, omega_factor=2.5, title=r"Transformation conforme dans un cas homogène où $\Omega = cste$")
# pour mieux voir l'expansion
ax1.set_xlim(-15, 15)
ax1.set_ylim(-15, 15)
ax2.set_xlim(-15, 15)
ax2.set_ylim(-15, 15)
plt.suptitle("Illustration d'un cas simple de l'invariance conforme : Expansion de l'échelle et conservation de la géométrie locale",
             fontsize=14)
plt.savefig('invariance_conforme.png', dpi=300, bbox_inches='tight')
plt.show()