import sounddevice
from scipy.io.wavfile import write

fs = 44100
secs = 10
print('recording...')
recordVoice = sounddevice.rec(int(secs * fs), samplerate = fs, channels = 2)
sounddevice.wait();
write("output.wav", fs, recordVoice)
