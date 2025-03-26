import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter

# Configurações
fc = 10000  # Portadora (fc >> 440 Hz)
fs = 44100  # Taxa de amostragem

# (d) Efeito da fase θ
def demodulate_with_phase(theta):
    t = np.linspace(0, 1, fs)
    m_t = 0.4 * np.cos(2*np.pi*440*t)
    modulated = m_t * np.cos(2*np.pi*fc*t)
    demodulated = modulated * np.cos(2*np.pi*fc*t + theta)
    
    # Filtro passa-baixas
    b, a = butter(4, 500/(fs/2), 'low')
    recovered = lfilter(b, a, demodulated)
    
    plt.plot(t, m_t, label='Original')
    plt.plot(t, recovered, label=f'Recuperado (θ={theta:.2f})')
    plt.legend()
    plt.show()

# (e) Potência vs Fase
thetas = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi]
powers = []
for theta in thetas:
    # [...] (implementação similar à anterior)
    power = np.mean(recovered**2)
    powers.append(power)

plt.plot(thetas, powers, 'o-')
plt.xlabel('Fase θ (rad)')
plt.ylabel('Potência recuperada')
plt.show()

# (f-i) Processamento de áudio
rate, data = wavfile.read('musica.wav')
# [...] (implementação completa conforme descrito)