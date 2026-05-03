import numpy as np
import matplotlib.pyplot as plt

# Singularité pour r=0
r = np.linspace(0.15, 3, 500)

# Calcul des intensités des champs (normalisées pour la visualisation)
courbure_weyl_classique = 1 / (r**3)  # Divergence en 1/r^3 (non-intégrable)
champ_twistoriel_reduit = 1 / (r**2)  # Divergence en 1/r^2 (intégrable sur une sphère)

plt.figure(figsize=(8, 6))

plt.plot(r, courbure_weyl_classique, color='darkred', linewidth=2.5,
         label=r'Courbure classique ($\hat{\psi} \propto 1/r^3$)')
plt.plot(r, champ_twistoriel_reduit, color='navy', linewidth=2.5, linestyle='--',
         label=r'Champ réduit par twisteur ($\hat{\phi} \propto 1/r^2$)')

plt.fill_between(r, champ_twistoriel_reduit, courbure_weyl_classique,
                 where=(courbure_weyl_classique > champ_twistoriel_reduit),
                 color='red', alpha=0.1, label='Zone de divergence non-linéaire')

plt.title("Réduction twistorielle de la divergence gravitationnelle près de la singularité", fontsize=12)
plt.xlabel("Distance radiale $r$ à la singularité", fontsize=11)
plt.ylabel("Intensité du champ gravitationnel", fontsize=11)
plt.xlim(0.15, 3)
plt.ylim(0, 50)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right', fontsize=11)

plt.tight_layout()
plt.savefig('divergence_twistor.png', dpi=300)
plt.show()