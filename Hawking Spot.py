import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Génération du fond diffus avec un bruit gaussien
np.random.seed(42) # Pour la reproductibilité
taille = 500
cmb_noise = np.random.normal(0, 1, (taille, taille))
cmb_smooth = gaussian_filter(cmb_noise, sigma=3) # Lissage pour imiter le CMB réel

# Hawking spot en utilisant des anneaux concentriques
x, y = np.meshgrid(np.arange(taille), np.arange(taille))
centre_x, centre_y = 250, 250
rayon = np.sqrt((x - centre_x)**2 + (y - centre_y)**2)

# Création d'une onde d'atténuation qui seront les anneaux de température
frequence = 0.1
amortissement = 0.02
anneaux = np.sin(frequence * rayon) * np.exp(-amortissement * rayon) * 1.5

# On ajoute l'anomalie au CMB de fond
cmb_final = cmb_smooth + anneaux

plt.figure(figsize=(8, 6))
plt.imshow(cmb_final, cmap='RdBu_r', extent=[-10, 10, -10, 10])
plt.colorbar(label=r'Fluctuations de température ($\Delta T / T$)')
plt.title('Simulation des Hawking Spots (Anomalies concentriques dans le CMB)')
plt.xlabel('Angle galactique')
plt.ylabel('Angle galactique')

plt.savefig('hawking_spots.png', dpi=300, bbox_inches='tight')
plt.show()