import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import zipfile
import os

# Configurações
fc = 10000  # Frequência da portadora
fs = 44100  # Taxa de amostragem padrão
thetas = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi]  # Fases para teste

# Carregar áudio enviado pelo usuário
audio_path = "/mnt/data/WhatsApp Ptt 2025-03-26 at 20.28.45.ogg"
output_wav_path = "/mnt/data/audio_original.wav"

# Converter o áudio para WAV (se necessário)
import subprocess
subprocess.run(["ffmpeg", "-i", audio_path, output_wav_path], capture_output=True, text=True)

# Ler o áudio convertido
rate, data = wavfile.read(output_wav_path)
data = data.astype(float) / np.max(np.abs(data))  # Normalizar

# Determinar a largura de banda do sinal de áudio
frequencies, times, Sxx = spectrogram(data, fs=rate, nperseg=1024)
bandwidth = frequencies[np.where(Sxx.mean(axis=1) > np.max(Sxx.mean(axis=1)) * 0.01)][-1]  # Largura de banda estimada

# Função para modulação AM
def modulate_am(signal, fc, fs):
    t = np.arange(len(signal)) / fs
    return signal * np.cos(2 * np.pi * fc * t)

# Função para demodulação AM com variação de fase
def demodulate_am(signal, fc, fs, theta):
    t = np.arange(len(signal)) / fs
    demodulated = signal * np.cos(2 * np.pi * fc * t + theta)
    
    # Filtro passa-baixas para recuperação do sinal
    b, a = butter(4, bandwidth/(fs/2), 'low')
    return lfilter(b, a, demodulated)

# Modulação do áudio
modulated_audio = modulate_am(data, fc, fs)

# Demodulação para diferentes fases e cálculo de potência
powers = []
demodulated_signals = []
for theta in thetas:
    recovered = demodulate_am(modulated_audio, fc, fs, theta)
    powers.append(np.mean(recovered**2))
    demodulated_signals.append(recovered)

# Exportar o áudio demodulado com θ = 0
output_demod_wav_path = "/mnt/data/audio_demodulado.wav"
wavfile.write(output_demod_wav_path, rate, np.int16(demodulated_signals[0] * 32767))

# Criar gráficos
plt.figure(figsize=(10, 4))
plt.plot(thetas, powers, 'o-')
plt.xlabel('Fase θ (rad)')
plt.ylabel('Potência recuperada')
plt.title('(e) Potência da Mensagem Recuperada vs Fase')
plt.savefig("/mnt/data/q4e_potencia_vs_fase.png")

plt.figure(figsize=(10, 4))
plt.plot(data[:fs], label="Original")
plt.plot(demodulated_signals[0][:fs], label=f"Demodulado (θ=0)")
plt.legend()
plt.title("(d) Comparação da Mensagem Original e Demodulada")
plt.savefig("/mnt/data/q4d_comparacao_mensagem.png")

# Calcular espectro da música original (item f)
segment_duration = 5  # segundos
num_samples = segment_duration * rate  # Número de amostras a considerar
data_segment = data[:num_samples]
frequencies_audio = np.fft.fftfreq(len(data_segment), d=1/rate)
spectrum_audio = np.abs(np.fft.fft(data_segment))

plt.figure(figsize=(10, 4))
plt.plot(frequencies_audio[:len(frequencies_audio)//2], spectrum_audio[:len(spectrum_audio)//2])
plt.title("(f) Espectro da Música Original")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.savefig("/mnt/data/q4f_espectro_original.png")

# Adicionar ruído ao sinal modulado (item g)
alpha = 0.8  # Atenuação do canal
noise_power = 0.01 * np.var(modulated_audio)  # Potência do ruído
noise = np.random.normal(scale=np.sqrt(noise_power), size=modulated_audio.shape)
received_signal = alpha * modulated_audio + noise

# Considerando apenas um segmento para FFT
received_segment = received_signal[:num_samples]
frequencies_received = np.fft.fftfreq(len(received_segment), d=1/rate)
spectrum_received = np.abs(np.fft.fft(received_segment))

plt.figure(figsize=(10, 4))
plt.plot(frequencies_received[:len(frequencies_received)//2], spectrum_received[:len(spectrum_received)//2])
plt.title("(g) Espectro do Sinal Recebido no Demodulador")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.savefig("/mnt/data/q4g_espectro_recebido.png")

# Demodulação do sinal recebido (item h)
demodulated_noisy = demodulate_am(received_signal, fc, fs, 0)

# Considerando apenas um segmento para FFT
demodulated_segment = demodulated_noisy[:num_samples]
frequencies_demod = np.fft.fftfreq(len(demodulated_segment), d=1/rate)
spectrum_demod = np.abs(np.fft.fft(demodulated_segment))

plt.figure(figsize=(10, 4))
plt.plot(frequencies_audio[:len(frequencies_audio)//2], spectrum_audio[:len(spectrum_audio)//2], label="Original")
plt.plot(frequencies_demod[:len(frequencies_demod)//2], spectrum_demod[:len(spectrum_demod)//2], label="Demodulado")
plt.legend()
plt.title("(h) Comparação dos Espectros: Original vs Demodulado")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.savefig("/mnt/data/q4h_comparacao_espectros.png")

# Criar novo arquivo ZIP organizado
zip_path = "/mnt/data/resultados.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.write(output_wav_path, "q4_audio_original.wav")
    zipf.write(output_demod_wav_path, "q4_audio_demodulado.wav")
    zipf.write("/mnt/data/q4d_comparacao_mensagem.png", "q4d_comparacao_mensagem.png")
    zipf.write("/mnt/data/q4e_potencia_vs_fase.png", "q4e_potencia_vs_fase.png")
    zipf.write("/mnt/data/q4f_espectro_original.png", "q4f_espectro_original.png")
    zipf.write("/mnt/data/q4g_espectro_recebido.png", "q4g_espectro_recebido.png")
    zipf.write("/mnt/data/q4h_comparacao_espectros.png", "q4h_comparacao_espectros.png")

print(f"Arquivo ZIP gerado: {zip_path}")
