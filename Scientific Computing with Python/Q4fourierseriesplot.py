import numpy as np
import matplotlib.pyplot as plt

def fourier_series(t, N):
    """ Aproximação da série de Fourier para t^2 """
    a0 = 1/3
    sum_series = np.full_like(t, a0)
    for n in range(1, N+1):
        an = (4 * (-1)**n) / (n**2 * np.pi**2)
        sum_series += an * np.cos(n * np.pi * t)
    return sum_series

# Intervalo de tempo
t = np.linspace(-1, 1, 400)
gt = t**2  # Função original

# Plot para diferentes números de harmônicos
harmonicos = [10, 20, 30]
plt.figure(figsize=(10, 6))
for N in harmonicos:
    plt.plot(t, fourier_series(t, N), label=f'N = {N}')

plt.plot(t, gt, 'k--', label='Original t²', linewidth=2)
plt.xlabel('t')
plt.ylabel('g(t)')
plt.title('Aproximação da Série de Fourier para g(t) = t²')
plt.legend()
plt.grid()
plt.show()
