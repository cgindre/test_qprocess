# -*- coding: utf-8 -*-
import time

n = 10e+05

start = time.time()
fib = [0, 1]

while len(fib) < n:
    fib.append(fib[-1] + fib[-2])

print("Le ", n, "-ème élement de la suite de Fibonacci vaut :", fib[-1])
end = time.time()
elapsed = end - start
print("Temps de calcul :", elapsed, " s")



start = time.time()
a = 0
b = 1


iter = 2
while iter < n:
    c = b
    b = b + a
    a = c
    iter += 1

# print("Le ", iter, "-ème élement de la suite de Fibonacci vaut :", b)
end = time.time()
elapsed = end - start
print("Temps de calcul :", elapsed, " s")
