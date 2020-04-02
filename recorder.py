import numpy as np
import sounddevice as sd
import soundfile as sf
import time
import queue

sd.default.device = 0
FS = 16000
CHANNELS = 1

q = queue.Queue()

def audioCallback(inData, frames, time, status):
    if status:
        print(status)
    q.put(inData.copy())

def main():
    try:
        data = np.array([])
        with sd.InputStream(samplerate = FS, channels = CHANNELS, callback = audioCallback):
            print('Recording...')
            print('Press Ctrl + C to stop recording!')
            while True:
                data = np.append(data,q.get())
    except KeyboardInterrupt:
       print('Stop recording')
       filename = input('Enter filename to save record: ')
       sf.write(filename + '.wav', data, FS)
       print('Save successfully')

if __name__ == '__main__':
    main()
