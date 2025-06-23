import numpy as np
import sounddevice as sd
from scipy.fft import rfft, rfftfreq
import config

# Configuration
SAMPLE_RATE = 44100  # Sampling rate in Hz
DURATION = 0.1       # Duration to record (in seconds) for each sample
MIN_FREQ = getattr(config,'MIN_FREQ',50)      # Minimum frequency to consider (in Hz)

def get_dominant_freq(samples, samplerate):
    N = len(samples)
    yf = rfft(samples)
    xf = rfftfreq(N, 1 / samplerate)

    magnitude = np.abs(yf)
    peak_idx = np.argmax(magnitude)
    freq = xf[peak_idx]
    return freq

def audio_callback(indata, frames, time, status):
    global MIN_FREQ
    # stop previous running vibration and run new vibration 
    if status:
        print("Status:", status)
    samples = indata[:, 0]
    freq = get_dominant_freq(samples, SAMPLE_RATE)
    # Assuming 'freq' is the dominant frequency or a relevant frequency component
    # within your audio analysis loop.
    if freq < MIN_FREQ:
        # print(f"Frequency {freq:.2f} Hz is below the minimum threshold of {MIN_FREQ} Hz. Ignoring.")
        return
    # Low Frequencies: (50 Hz - 250 Hz) - For deep sounds, rumbles, and bass.
    # This band often covers the feeling of vibrations from heavy objects, footsteps,
    # large vehicles, or the low end of male voices.
    if freq >= 50 and freq < 250:
        print(f"Low Frequency Detected: (e.g., deep voice, rumble, thump) - {freq:.2f} Hz")

    # Mid Frequencies: (250 Hz - 2000 Hz) - For most human speech and common environmental sounds.
    # This is a crucial band for understanding speech presence and everyday interactions.
    if freq >= 250 and freq < 2000:
        print(f"Mid Frequency Detected: (e.g., human speech, general conversations, music) - {freq:.2f} Hz")

    # High Frequencies: (2000 Hz - 8000 Hz) - For alarms, alerts, and piercing sounds.
    # These often indicate important warnings or distinct environmental cues like birds or breaking glass.
    if freq >= 2000 and freq < 8000:
        print(f"High Frequency Detected: (e.g., alarm, whistle, glass breaking, bird chirps) - {freq:.2f} Hz")

    # Very High Frequencies: (8000 Hz and above) - For very sharp or subtle high-pitched sounds.
    # Energy in this range can indicate specific electronic noises, very distant or faint high-pitched sounds,
    # or even ultrasonic noise depending on the microphone. Useful for detecting very sharp or subtle cues.
    if freq >= 8000:
        print(f"Very High Frequency Detected: (e.g., very sharp squeak, subtle high-pitch, electronic noise) - {freq:.2f} Hz")        
        

def main():
    with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE, blocksize=int(SAMPLE_RATE * DURATION)):
        print("Listening... Press Ctrl+C to stop.")
        while True:
            sd.sleep(100)

if __name__ == "__main__":
    main()
