import sounddevice
from scipy.io.wavfile import write
def savefile(sec):
    print("Start Recording")
    record = sounddevice.rec((sec*44100),samplerate=44100,channels=1)
    sounddevice.wait()
    write("recording.wav",44100,record)
    print("End Recording")

savefile(20)
