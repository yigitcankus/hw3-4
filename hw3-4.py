import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation





populasyon1_ortalama=[]
populasyon2_ortalama=[]

for i in range(0,51):
    populasyon = np.random.normal(100, 1, 1000)
    populasyon1_ortalama.append(np.mean(populasyon))

for i in range(0, 1001):
    populasyon2 = np.random.normal(100, 10, 1000)
    populasyon2_ortalama.append(np.mean(populasyon2))

plt.subplot(121)
plt.hist(populasyon1_ortalama)
plt.ylabel("populasyon1")

plt.subplot(122)
plt.hist(populasyon2_ortalama)
plt.ylabel("populasyon2")

plt.tight_layout()

plt.show()

###neden +1e2 oluyor ve standart sapma değerleri ondalık etki ediyor


######

#Bu soruda büyük sayılar yasası hileli para mı hilesiz para mı olduğunu bize anlatır.
#Çok deneme yapıldığında eğer hileli ise turalar daha çok olucaktır, hilesizse
#eşit gelicektir.