import itertools
import math
import random
import time
import matplotlib.pyplot as plt
from threading import Thread as tH

start = time.perf_counter()


def odleglosc(x1, x2, y1, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def dlugosc_trasy(trasa):
    d = 0
    for i in range(1, len(trasa)):
        x1 = punkty[trasa[i - 1]][0]
        y1 = punkty[trasa[i - 1]][1]
        x2 = punkty[trasa[i]][0]
        y2 = punkty[trasa[i]][1]
        d += odleglosc(x1, x2, y1, y2)
    x1 = punkty[trasa[len(trasa) - 1]][0]
    y1 = punkty[trasa[len(trasa) - 1]][1]
    x2 = punkty[trasa[0]][0]
    y2 = punkty[trasa[0]][1]
    d += odleglosc(x1, x2, y1, y2)
    return d


def najlepsza_trasa_watek(trasy, garr, index):
    best = trasy[0]
    for trasa in trasy:
        length = dlugosc_trasy(trasa)
        if length < dlugosc_trasy(best):
            best = trasa
    garr[index] = best


def najlepsza_trasa(trasy):
    best = trasy[0]
    for i in trasy:
        length = dlugosc_trasy(i)
        if length < dlugosc_trasy(best):
            best = i
    return best


n = 9
punkty = [random.sample(range(100), 2) for i in range(n)]
droga = random.sample(range(n), n)

wszystkie_trasy = list(itertools.permutations(droga))
N = len(wszystkie_trasy) // 8  # takie dzielenie odrzuca wartość po przecinku
czesci_wszystkich = [wszystkie_trasy[i:i + N] for i in range(0, len(wszystkie_trasy), N)]

m = len(czesci_wszystkich)
BestTrasy = [None] * m
threads = []
for i, czesc in enumerate(czesci_wszystkich):
    t = tH(target=najlepsza_trasa_watek, args=[czesc, BestTrasy, i])
    threads.append(t)

for t in threads:
    t.start()
    print(threads)

for t in threads:
    t.join()

BestTrasa = najlepsza_trasa(BestTrasy)
BestDlugosc = dlugosc_trasy(BestTrasa)

print("Shortes distance:", round(BestDlugosc, 2))
print("Optimal route:", BestTrasa)
pustak = []
for i in BestTrasa:
    pustak.append(punkty[i])

x = [point[0] for point in pustak]
y = [point[1] for point in pustak]
point1 = pustak[0]
point2 = pustak[-1]
x_wartosc = [point1[0], point2[0]]
y_wartosc = [point1[-1], point2[-1]]
finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")

plt.fill(x, y, "-o", fill=False)
plt.plot(x, y, "o")
plt.show()
