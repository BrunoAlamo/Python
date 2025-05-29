import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

# Parâmetros
N = 1000  # número de bits
Tb = 1    # tempo de bit
fs = 100  # frequência de amostragem (100 amostras por bit)
dt = Tb / fs
t = np.arange(0, N * Tb, dt)

# Geração de bits aleatórios
bits = np.random.randint(0, 2, N)

# Funções de codificação RZ
def rz_onoff(bits, fs):
    signal = np.zeros(len(bits) * fs)
    for i, bit in enumerate(bits):
        if bit == 1:
            signal[i*fs:i*fs + fs//2] = 1
    return signal

def rz_polar(bits, fs):
    signal = np.zeros(len(bits) * fs)
    for i, bit in enumerate(bits):
        if bit == 1:
            signal[i*fs:i*fs + fs//2] = 1
        else:
            signal[i*fs:i*fs + fs//2] = -1
    return signal

def rz_bipolar(bits, fs):
    signal = np.zeros(len(bits) * fs)
    polarity = 1
    for i, bit in enumerate(bits):
        if bit == 1:
            signal[i*fs:i*fs + fs//2] = polarity
            polarity *= -1
    return signal

# Sinais codificados
x_onoff = rz_onoff(bits, fs)
x_polar = rz_polar(bits, fs)
x_bipolar = rz_bipolar(bits, fs)

# Função para calcular a PSD usando FFT
def compute_psd(signal, fs):
    N = len(signal)
    f = fftfreq(N, d=1/fs)
    S = fft(signal)
    PSD = (1/N) * np.abs(S)**2
    return fftshift(f), fftshift(PSD)

# Cálculo das PSDs
f_onoff, psd_onoff = compute_psd(x_onoff, fs)
f_polar, psd_polar = compute_psd(x_polar, fs)
f_bipolar, psd_bipolar = compute_psd(x_bipolar, fs)

# Plot das PSDs
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(f_onoff, psd_onoff, color='orange')
plt.title('PSD - Código RZ On-Off')
plt.xlabel('Frequência (Hz)')
plt.ylabel('PSD')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(f_polar, psd_polar, color='green')
plt.title('PSD - Código RZ Polar')
plt.xlabel('Frequência (Hz)')
plt.ylabel('PSD')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(f_bipolar, psd_bipolar, color='blue')
plt.title('PSD - Código RZ Bipolar')
plt.xlabel('Frequência (Hz)')
plt.ylabel('PSD')
plt.grid(True)

plt.tight_layout()
plt.show()
