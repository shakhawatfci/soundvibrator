Sound-to-Vibration Device for the Hearing Impaired
Project Overview

This project aims to create a tactile feedback system for individuals with hearing impairments, allowing them to perceive ambient sounds through vibrations. The device processes real-time audio input, analyzes its frequency components, and translates these into distinct vibrations on the user's body (e.g., via a bracelet or vest). By associating different frequency bands with specific vibration motors, the user can gain a sense of the sound environment around them, distinguishing between low-frequency sounds (like a door closing or footsteps), mid-range sounds (like speech), and high-frequency sounds (like alarms or bird chirps).

The core of this system is a Python script designed to run on a Raspberry Pi, leveraging its GPIO capabilities to control vibration motors based on audio analysis.
How It Works

    Audio Capture: A USB microphone connected to the Raspberry Pi captures real-time audio.

    Frequency Analysis (FFT): The captured audio data is transformed from the time domain to the frequency domain using a Fast Fourier Transform (FFT). This allows the system to identify the dominant frequencies present in the sound.

    Band Separation: The frequency spectrum is divided into three customizable bands:

        Low Frequencies: (e.g., 20 Hz - 250 Hz) - For bass sounds, rumbles, deep voices.

        Mid Frequencies: (e.g., 250 Hz - 2000 Hz) - For most human speech, music.

        High Frequencies: (e.g., 2000 Hz - 8000 Hz) - For alarms, whistles, higher-pitched sounds.

    Vibration Control: The script dynamically calculates a "magnitude" for each frequency band. This magnitude is then normalized to control the intensity (duty cycle) of a dedicated vibration motor for that band.

        A higher magnitude in a band results in a stronger vibration from its corresponding motor.

        Dynamic normalization ensures that the vibrations are noticeable across a wide range of sound volumes, adapting to both quiet and loud environments.

    Tactile Feedback: Each motor provides distinct feedback for its assigned frequency range, allowing the user to interpret the nature of the sound.

Features

    Real-time audio processing.

    Separation of sounds into low, mid, and high-frequency bands.

    Independent vibration control for each frequency band.

    Dynamic intensity adjustment for varied sound levels.

    Customizable frequency bands and motor thresholds.

    Raspberry Pi compatible for a compact and portable solution.

Hardware Requirements

To build this device, you will need:

    Raspberry Pi: Model 3, 4, or Zero 2 W recommended (with GPIO pins).

    USB Microphone: A standard omnidirectional USB microphone.

    Vibration Motors: At least three independent vibration motors (e.g., coin vibration motors, pager motors, or Linear Resonant Actuators (LRAs)).

    Motor Driver Board(s): Essential! Raspberry Pi GPIO pins cannot directly power motors. You will need a motor driver (e.g., DRV8833, L293D, or individual MOSFETs with flyback diodes) to control the motors. Ensure it can handle the voltage and current requirements of your chosen motors.

    Breadboard and Jumper Wires: For prototyping the circuit.

    Separate Power Supply for Motors: A 3V-5V power supply for your motors, distinct from the Raspberry Pi's power supply, to prevent brownouts or damage to the Pi.

    5V Power Supply for Raspberry Pi: Standard USB-C or Micro-USB power supply, depending on your Pi model.

    SD Card: For Raspberry Pi OS.

    Wearable Enclosure: A custom-designed bracelet, vest, or other comfortable enclosure to house the motors and electronics.
