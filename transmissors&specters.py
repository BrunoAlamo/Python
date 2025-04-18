import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

# Parâmetros
fs = 500000  # taxa de amostragem (500 kHz)
t = np.arange(0, 5e-3, 1/fs)  # 5 ms de sinal

# Sinais de mensagem
f1 = 440
f2 = 554
m1 = np.sin(2 * np.pi * f1 * t)
m2 = np.sin(2 * np.pi * f2 * t)

# Portadora
fc = 100000  # 100 kHz
Ac = 1

# Sinal transmitido s(t)
s = Ac * m1 * np.cos(2 * np.pi * fc * t) + Ac * m2 * np.sin(2 * np.pi * fc * t)

# FFT
def plot_fft(signal, fs, title):
    N = len(signal)
    freqs = fftshift(fftfreq(N, 1/fs))
    S = fftshift(fft(signal))
    plt.figure(figsize=(12, 4))
    plt.plot(freqs, np.abs(S)/N)
    plt.title(f'Espectro de Amplitude - {title}')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.xlim(-200000, 200000)
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(freqs, np.angle(S))
    plt.title(f'Espectro de Fase - {title}')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Fase (rad)')
    plt.grid(True)
    plt.xlim(-200000, 200000)
    plt.show()

# Plot s(t)
plt.figure(figsize=(12, 4))
plt.plot(t*1000, s)
plt.title('Sinal Transmitido s(t)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, 1)  # zoom nos primeiros 1 ms
plt.show()

# Plot espectros
plot_fft(s, fs, "s(t)")
