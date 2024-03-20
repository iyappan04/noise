from scipy.io import wavfile
import noisereduce as nr
# load data
rate, data = wavfile.read("/home/iyappan/Music/noise_audio/long_audio_2.wav")
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write("output/long_2_output.wav", rate, reduced_noise)