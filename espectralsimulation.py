import numpy as np
import matplotlib.pyplot as plt

# Definição dos parâmetros
fs = 10000  # Taxa de amostragem
T = 1  # Duração do sinal em segundos
t = np.linspace(0, T, fs*T, endpoint=False)  # Vetor de tempo

# Sinais de entrada
A1, A2 = 1, 1  # Amplitudes
f1, f2 = 440, 500  # Frequências dos sinais

g1 = A1 * np.cos(2 * np.pi * f1 * t)  # Sinal para (a)
g2 = A1 * np.cos(2 * np.pi * f1 * t) + A2 * np.cos(2 * np.pi * f2 * t)  # Sinal para (b)

# Modelo não linear cúbico
a1, a2, a3 = 1, 0.1, 0.05  # Coeficientes do sistema
y1 = a1 * g1 + a2 * g1**2 + a3 * g1**3  # Saída para (a)
y2 = a1 * g2 + a2 * g2**2 + a3 * g2**3  # Saída para (b)

# Transformada de Fourier
Y1 = np.fft.fft(y1)
Y2 = np.fft.fft(y2)
freqs = np.fft.fftfreq(len(t), 1/fs)

# Gráficos dos espectros
plt.figure(figsize=(12, 6))

plt.subplot(2,1,1)
plt.plot(freqs[:fs//2], np.abs(Y1[:fs//2]))
plt.title("Espectro de Y(f) para f1 = 440 Hz")
plt.xlabel("Frequência (Hz)")
plt.ylabel("|Y(f)|")

plt.subplot(2,1,2)
plt.plot(freqs[:fs//2], np.abs(Y2[:fs//2]))
plt.title("Espectro de Y(f) para f1 = 440 Hz e f2 = 500 Hz")
plt.xlabel("Frequência (Hz)")
plt.ylabel("|Y(f)|")

plt.tight_layout()
plt.show()
