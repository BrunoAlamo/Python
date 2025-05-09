import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
fc = 150e3             # frequência central (Hz)
delta_f = 50e3         # desvio de frequência (Hz)
fm = 5e3               # frequência da mensagem (Hz)
fs = 5e6               # taxa de amostragem
t = np.linspace(0, 1e-3, int(1e-3 * fs))  # 1 ms de sinal

# Frequência instantânea
f_inst = fc + delta_f * np.cos(2 * np.pi * fm * t)

# Amplitude modulada pela resposta do filtro (simplificada como gaussiana em torno de fc)
H = np.exp(-((f_inst - 118.7e3)**2) / (2*(15e3)**2))  # filtro centrado em 118,7 kHz

# Sinal resultante
v2 = H * np.cos(2 * np.pi * f_inst * t)

# Plot
plt.figure(figsize=(10,4))
plt.plot(t * 1e3, v2)
plt.title("Sinal no ponto 2 (v2(t)) - Resposta teórica")
plt.xlabel("Tempo (ms)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
