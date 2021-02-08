import skfuzzy as fuzz
import numpy as np
from matplotlib import pyplot as plt

brzina = np.arange(60, 131, 1)
mogucnost_nesrece = np.arange(2, 20, 0.1)

# funkcije pripadnosti

b_spora = fuzz.trapmf(brzina, [60, 60, 70, 85])
b_umjerena = fuzz.trimf(brzina, [70, 90, 105])
b_brza = fuzz.trapmf(brzina, [85, 120, 130, 130])

mn_mala = fuzz.trapmf(mogucnost_nesrece, [0, 0, 5, 9])
mn_srednja = fuzz.trimf(mogucnost_nesrece, [3, 7, 15])
mn_velika = fuzz.trapmf(mogucnost_nesrece, [13, 17, 20, 20])

fig, ax = plt.subplots()

ax.plot(brzina, b_spora, 'g', brzina, b_umjerena, 'b', brzina, b_brza, 'r')
ax.set_ylabel('Fuzzy pripadnost')
ax.set_xlabel('Brzina km/h')
plt.show()

fig, ax = plt.subplots()

ax.plot(mogucnost_nesrece, mn_mala, 'g', mogucnost_nesrece, mn_srednja, 'b', mogucnost_nesrece, mn_velika, 'r')
ax.set_ylabel('Fuzzy pripadnost')
ax.set_xlabel('Mogucnost nesrece')
plt.show()

rel_1 = fuzz.relation_min(b_spora, mn_mala)
rel_2 = fuzz.relation_min(b_umjerena, mn_srednja)
rel_3 = fuzz.relation_min(b_brza, mn_velika)
rel_kombinovana = np.fmax(rel_1, np.fmax(rel_2, rel_3))

predvidjena_nesreca = np.zeros_like(brzina)

for i in range(len(predvidjena_nesreca)):
    predvidjena_nesreca[i] = fuzz.defuzz(mogucnost_nesrece, rel_kombinovana[i, :], 'centroid')

plt.plot(brzina, predvidjena_nesreca, 'k')
plt.vlines(100, 5, predvidjena_nesreca[brzina == 100], color='red', linestyle='dashed', lw=1)
plt.hlines(predvidjena_nesreca[brzina == 100], 30, 100, color='red', linestyle='dashed', lw=1)
plt.xlabel('Brzina')
plt.ylabel('Mogucnost nesrece')
plt.show()