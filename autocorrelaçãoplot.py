import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
a = 1
tau = np.linspace(-5, 5, 1000)

# Função de autocorrelação para g1(t)
R_g1 = np.exp(-a * np.abs(tau)) / (2 * a)

# Plot
plt.plot(tau, R_g1, label=r'$R_{g_1}(\tau)$')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{g_1}(\tau)$')
plt.title('Autocorrelação de $g_1(t)$')
plt.grid()
plt.legend()
plt.show()