import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq
from scipy.signal import square

# Parâmetros fornecidos
B = 40e3  # 40 kHz
Td = 500e-9  # 500 ns
k = 0.3
T = 8e-6  # 8 μs
fs = 10 * B  # Taxa de amostragem (10x a banda)
N = 4096  # Número de pontos
f = np.linspace(-fs/2, fs/2, N)  # Eixo de frequências

# Definição de H(f)
H = (1 + k * np.cos(2 * np.pi * f * T)) * np.exp(-1j * 2 * np.pi * f * Td)
H[np.abs(f) > B] = 0  # Zerar frequências fora da banda

# Plotando módulo e fase de H(f)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(f / 1e3, np.abs(H))
plt.title("Espectro de Amplitude |H(f)|")
plt.xlabel("Frequência (kHz)")
plt.ylabel("|H(f)|")
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(f / 1e3, np.angle(H))
plt.title("Espectro de Fase θ_H(f)")
plt.xlabel("Frequência (kHz)")
plt.ylabel("Fase (radianos)")
plt.grid()
plt.show()

# Gerando a onda quadrada de 20 kHz
t = np.linspace(0, 1 / 20e3, N, endpoint=False)  # Janela de tempo
gt = square(2 * np.pi * 20e3 * t)  # Onda quadrada de 20 kHz

# Transformada de Fourier de g(t)
Gf = fft(gt, N)
freqs = fftfreq(N, 1 / fs)

# Aplicando H(f)
Yf = Gf * H

# Transformada inversa para obter y(t)
yt = np.real(ifft(Yf))

# Plotando g(t) e y(t)
plt.figure(figsize=(10, 5))
plt.plot(t * 1e6, gt, label='Sinal de Entrada g(t)')
plt.plot(t * 1e6, yt, label='Sinal de Saída y(t)', linestyle='dashed')
plt.xlabel("Tempo (μs)")
plt.ylabel("Amplitude")
plt.title("Comparação entre g(t) e y(t) para 20 kHz")
plt.legend()
plt.grid()
plt.show()

# Repetindo para 30 kHz
gt_30 = square(2 * np.pi * 30e3 * t)  # Onda quadrada de 30 kHz
Gf_30 = fft(gt_30, N)
Yf_30 = Gf_30 * H
yt_30 = np.real(ifft(Yf_30))

# Plotando para 30 kHz
plt.figure(figsize=(10, 5))
plt.plot(t * 1e6, gt_30, label='Sinal de Entrada g(t) - 30 kHz')
plt.plot(t * 1e6, yt_30, label='Sinal de Saída y(t) - 30 kHz', linestyle='dashed')
plt.xlabel("Tempo (μs)")
plt.ylabel("Amplitude")
plt.title("Comparação entre g(t) e y(t) para 30 kHz")
plt.legend()
plt.grid()
plt.show()
