import numpy as np
import matplotlib.pyplot as plt

# Du Big Bang au futur
t = np.linspace(0, 10, 500)

# Entropie de la matière qui monte vite à cause du plasma thermique puis stagne
S_matiere = 8 * (1 - np.exp(-2 * t)) + 2

# Entropie gravitationnelle (Weyl) qui est quasi nulle au début puis augmente de façon exponentielle à cause des trous noirs
S_gravitationnelle = 0.05 * np.exp(0.8 * t)

plt.figure(figsize=(9, 6))

plt.plot(t, S_matiere, color='darkorange', linewidth=2.5,
         label=r'Entropie de la Matière ($S_{mat}$)')
plt.plot(t, S_gravitationnelle, color='purple', linewidth=2.5,
         label=r'Entropie Gravitationnelle ($S_{grav} \propto C_{abcd}C^{abcd}$)')

plt.axvline(x=0, color='gray', linestyle='--')
plt.text(0.2, 10, 'Big Bang\n(WCH: Weyl $\\to 0$)', fontsize=10, verticalalignment='center')
plt.text(8, 25, 'Formation des\nTrous Noirs', fontsize=10, color='purple')

plt.title("Évolution divergente des composantes de l'entropie cosmique", fontsize=12)
plt.xlabel("Temps cosmique $t$ (unités arbitraires)", fontsize=11)
plt.ylabel("Entropie $S$", fontsize=11)
plt.xlim(-0.5, 10)
plt.ylim(0, 40)
plt.yticks([]) # On enlève les valeurs numériques de l'axe y car c'est conceptuel
plt.grid(True, alpha=0.2)
plt.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig('paradoxe_entropie.png', dpi=300)
plt.show()