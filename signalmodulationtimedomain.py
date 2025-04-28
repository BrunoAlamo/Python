import numpy as np
import matplotlib.pyplot as plt

# Dados
E0 = 1         # Amplitude da portadora
fm = 5e3       # Frequência do sinal modulante (5 kHz)
fc = 100e3     # Frequência da portadora (100 kHz)
beta = 0.2     # Índice de modulação (NBFM)

# Definições
Fs = 1e6       # Frequência de amostragem (1 MHz, para boa resolução)
t = np.arange(0, 1e-3, 1/Fs)  # Tempo de 0 a 1ms

# Frequências angulares
w0 = 2*np.pi*fc
wm = 2*np.pi*fm

# Sinal NBFM conforme aproximação
e_t = E0*np.cos(w0*t) - (beta*E0/2)*np.cos((w0 - wm)*t) + (beta*E0/2)*np.cos((w0 + wm)*t)

# Gráfico
plt.figure(figsize=(10,5))
plt.plot(t*1e3, e_t)
plt.title('Sinal FM de Faixa Estreita (NBFM)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.xlim(0, 1)  # mostra só o primeiro 1ms
plt.show()
