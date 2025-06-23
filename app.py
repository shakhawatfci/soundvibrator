import numpy as np
import sounddevice as sd
from scipy.fft import rfft, rfftfreq

# Configuration
SAMPLE_RATE = 44100  # Sampling rate in Hz
DURATION = 0.1       # Duration to record (in seconds) for each sample

def get_dominant_freq(samples, samplerate):
    N = len(samples)
    yf = rfft(samples)
    xf = rfftfreq(N, 1 / samplerate)

    magnitude = np.abs(yf)
    peak_idx = np.argmax(magnitude)
    freq = xf[peak_idx]
    return freq

def audio_callback(indata, frames, time, status):
    # stop previous running vibration and run new vibration 
    if status:
        print("Status:", status)
    samples = indata[:, 0]
    freq = get_dominant_freq(samples, SAMPLE_RATE)
    if freq > 0 and freq < 20:
        print("Low Frequency Detected:", freq)
    
    if freq > 20 and freq < 200:    
       print(f"low taling  Frequency: {freq:.2f} Hz")
    if freq > 200 and freq < 500:
        print(f"Medium Frequency Detected: {freq:.2f} Hz")
    if freq > 500 and freq < 900:
        print(f"Mid High Frequency Detected: {freq:.2f} Hz")      
    if freq > 900 and freq < 1200:
        print(f"High Frequency Detected: {freq:.2f} Hz")
    if freq > 1200:
        print(f"Very High Frequency Detected: {freq:.2f} Hz")         
        

def main():
    with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE, blocksize=int(SAMPLE_RATE * DURATION)):
        print("Listening... Press Ctrl+C to stop.")
        while True:
            sd.sleep(10)

if __name__ == "__main__":
    main()
