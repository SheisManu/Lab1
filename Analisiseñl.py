import numpy as np
import matplotlib.pyplot as plt

# Load the data from the text file
data = np.loadtxt('emg_neuropathy.txt', delimiter=' ')

# Assuming the data has two columns: time and signal
time = data[:, 0]
signal = data[:, 1]

#PARTE 1 - GRÁFIICA DE LA SEÑAL
# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(time, signal, label='EMG Signal')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('EMG Neuropathy Signal')
plt.legend()
plt.grid(True)
plt.show()

#PARTE  