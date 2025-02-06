import numpy as np
import matplotlib.pyplot as plt

# Load the data from the text file
data = np.loadtxt('emg_neuropathy.txt', delimiter=' ')

# Assuming the data has two columns: time and signal
time = data[:, 0]
signal = data[:, 1]

#PARTE 1 - GRÁFICA DE LA SEÑAL
# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(time, signal, label='EMG Signal')

#PARTE 2 - ESTADÍSTICOS DESCRIPTIVOS

#CON PYTHON
#Media de la señal
signal_mean = np.mean(signal)
#Add the mean value as text on the plot
plt.text(0.05, 0.95, f'Media de la señal: {signal_mean:.2f}', transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

#Mostrando la gráfica de la PARTE 1
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('EMG Neuropathy Signal')
plt.legend()
plt.grid(True)
plt.show()
