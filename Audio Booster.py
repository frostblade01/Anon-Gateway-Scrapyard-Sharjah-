import numpy as np
import sounddevice as sd
import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

CHUNK = 1024
THRESHOLD = 500
SAMPLE_RATE = 44100

audiodevices = AudioUtilities.GetSpeakers()
interface = audiodevices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volume_range = volume.GetVolumeRange()
minvol = volume_range[0]
maxvol = volume_range[1]

def get_microphone_volume():
    """Capture audio from the microphone and calculate the RMS volume."""
    duration = 1.0
    recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    
    rms = np.sqrt(np.mean(np.square(recording)))
    
    return rms

def set_system_volume(volume_level):
    """Set the system volume to the specified level."""
    volume_level = max(min(volume_level, maxvol), minvol)
    
    volume.SetMasterVolumeLevel(volume_level, None)

try:
    print("Volume control script is running. Press Ctrl+C to exit.")
    while True:
        mic_volume = get_microphone_volume()
        print(f"Microphone Volume: {mic_volume}")
        if mic_volume > THRESHOLD:
            set_system_volume(minvol)  # Mute when loud
        else:
            set_system_volume(maxvol)  # Max volume when quiet
        time.sleep(0.5)  # Add a short delay
except KeyboardInterrupt:
    print("Exiting...")
