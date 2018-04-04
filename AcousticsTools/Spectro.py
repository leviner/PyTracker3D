'''
This is example code for reading and plotting a spectrogram
from a .wav file using only scipy and matplotlib

'''

from scipy import signal
from scipy.io import wavefile

# First, read in a file, getting sampling rate (in Hz) and data (wavefile intensity as a vector)
sampling_rate, data = wavefile.read("940302-1222.WAV")

#Extract sample bins, time, and data matrix viae a spectrogram object
# not sure what amplitude units are (linear?)
freq, time, amplitude = signal.spectrogram(data,sampling_rate)

# Amplitude is now a "freq by time" dimension matrix
print(amplitude)

#Use matplotlib and make a spectrogram image
import matplotlib.pyplot as plt
import numpy as np
log_amplitude = np.log(amplitude)
# create a pcolor plot object of the log transformed amplitude data
plt.pcolormesh(time, freq,log_amplitude, cmap='Greys')
plt.show()
