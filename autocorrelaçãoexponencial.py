import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
A = 1.0  # Amplitude do pulso
tau = 10  # Largura do pulso (amostras)
fc = 77e9  # Frequência do radar (77 GHz)
c = 3e8  # Velocidade da luz (m/s)
d = 50  # Distância do objeto (m)
sigma = 1.0  # Seção transversal de radar (m²)
lambda_ = c / fc  # Comprimento de onda (m)
alpha = (A * lambda_**2 * sigma) / ((4 * np.pi)**3 * d**4)  # Fator de atenuação

# Sinal transmitido x[n]
n = np.arange(0, 100)  # Vetor de tempo discreto
x = A * np.exp(-((n - 50) ** 2) / (2 * tau**2))  # Pulso Gaussiano

# Atraso em amostras
Delta_t = int(2 * d / c * fc)  # Atraso em amostras

# Sinal recebido y[n]
y = alpha * np.roll(x, Delta_t)  # Sinal atrasado e atenuado
w = np.random.normal(0, 0.1, len(n))  # Ruído Gaussiano branco
y += w  # Adiciona ruído ao sinal recebido

# Correlação entre x[n] e y[n]
correlation = np.correlate(x, y, mode='full')

# Encontra o pico da correlação
peak_index = np.argmax(correlation)
estimated_Delta_t = peak_index - len(n) + 1

# Distância estimada
estimated_distance = (estimated_Delta_t * c) / (2 * fc)

# Plot dos sinais e correlação
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(n, x, label='Sinal transmitido x[n]')
plt.legend()
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(n, y, label='Sinal recebido y[n]')
plt.legend()
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(correlation, label='Correlação entre x[n] e y[n]')
plt.axvline(peak_index, color='r', linestyle='--', label=f'Pico em k = {peak_index}')
plt.legend()
plt.grid()

plt.show()

print(f"Tempo de voo estimado: {estimated_Delta_t} amostras")
print(f"Distância estimada: {estimated_distance:.2f} metros")