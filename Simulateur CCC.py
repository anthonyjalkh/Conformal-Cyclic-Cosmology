import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.ndimage import gaussian_filter

np.random.seed(42)
taille = 300
cmb_noise = np.random.normal(loc=0, scale=1, size=(taille, taille))
cmb_smooth = gaussian_filter(cmb_noise, sigma=3)

x, y = np.meshgrid(np.linspace(-10, 10, taille), np.linspace(-10, 10, taille))
rayon = np.sqrt(x ** 2 + y ** 2)

r_div = np.linspace(0.15, 3, 500)

fig, (ax_cmb, ax_div) = plt.subplots(2, 1, figsize=(8, 10))
plt.subplots_adjust(bottom=0.25, hspace=0.4)

M_init = 15.0
omega_init = 1.0  


def calculer_spot(M_log, omega):
    """Calcule l'intensité de l'onde sur le CMB en fonction de la masse et du facteur conforme"""
    # L'amplitude dépend de la masse qui, elle, est normalisée autour de 10^15
    amplitude = (10 ** (M_log - 15)) * omega
    frequence = 0.8
    amortissement = 0.3
    anneaux = np.sin(frequence * rayon) * np.exp(-amortissement * rayon) * amplitude * 1.5
    return cmb_smooth + anneaux


img = ax_cmb.imshow(calculer_spot(M_init, omega_init), cmap='RdBu_r', extent=[-10, 10, -10, 10], vmin=-3, vmax=3)
ax_cmb.set_title("Simulation du CMB : Apparition du Hawking Spot", fontsize=11)
ax_cmb.set_xlabel("Angle galactique")
ax_cmb.set_ylabel("Angle galactique")
cbar = fig.colorbar(img, ax=ax_cmb)
cbar.set_label(r'Fluctuations $\Delta T / T$')


# Graphique du bas et qui montre la divergence twistorielle)
def calculer_divergence(M_log):
    """Calcule les courbes de divergence 1/r^3 et 1/r^2"""
    echelle = 10 ** (M_log - 15)
    c_weyl = (1 / r_div ** 3) * echelle
    c_twist = (1 / r_div ** 2) * echelle
    return c_weyl, c_twist


c_w, c_t = calculer_divergence(M_init)
ligne_weyl, = ax_div.plot(r_div, c_w, color='darkred', lw=2, label=r'Courbure classique ($\propto 1/r^3$)')
ligne_twist, = ax_div.plot(r_div, c_t, color='navy', lw=2, linestyle='--',
                           label=r'Champ réduit par twisteur ($\propto 1/r^2$)')

ax_div.set_ylim(0, 50)
ax_div.set_xlim(0.15, 3)
ax_div.set_title("Réduction twistorielle à l'approche de la singularité", fontsize=11)
ax_div.set_xlabel("Distance radiale r")
ax_div.set_ylabel("Intensité du champ")
ax_div.grid(True, alpha=0.3)
ax_div.legend()


# Création des sliders

couleur_axe = 'lightgray'
ax_M = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=couleur_axe)
ax_omega = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=couleur_axe)

slider_M = Slider(ax_M, r'Log(Masse) $M_\odot$', 13.0, 16.0, valinit=M_init, valstep=0.1)
slider_omega = Slider(ax_omega, r'Facteur Conforme $\omega$', 0.1, 3.0, valinit=omega_init)



# Fonction de mise à jour dynamique
def update(val):
    M_actuelle = slider_M.val
    omega_actuel = slider_omega.val

    # Mise à jour de l'image CMB
    img.set_data(calculer_spot(M_actuelle, omega_actuel))

    # Mise à jour des courbes de divergence
    c_w, c_t = calculer_divergence(M_actuelle)
    ligne_weyl.set_ydata(c_w)
    ligne_twist.set_ydata(c_t)
    fig.canvas.draw_idle()

slider_M.on_changed(update)
slider_omega.on_changed(update)

plt.show()
