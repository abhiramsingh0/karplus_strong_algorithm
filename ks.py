import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
from playsound import playsound as ps

def KS_1(x, N):
    # given the initial buffer x, produce a N-sample output
    #  by concatenating identical copies of the buffer
    y = x

    while len(y) < N:
        # keep appending until we reach or exceed the required length
        y = np.append(y, x)
    # trim the excess
    y = y[0:N+1]
    return y

Fs = 16000 # 16 KHz sampling rate

b = np.random.randn(50)
plt.stem(b);

y = KS_1(b, Fs * 1)

# we can look at a few periods:
plt.stem(y[0:500]);
scaled = np.int16(y/np.max(np.abs(y)) * 32767)
write('test.wav', 44100, scaled)
ps('test.wav')
