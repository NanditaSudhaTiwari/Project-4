import numpy as np
import matplotlib.pyplot as plt

# Parameters
length = 14   # Length of the rod
time_total = 3600   # Total simulation time
num_points_space = 100  # Number of spatial points
num_points_time = 20000  # Number of time points

# Thermal diffusivities for Aluminum and Silver
alpha_aluminum = 9.71e-5   # Thermal diffusivity for Aluminum (calculated)
alpha_silver = 1.74e-4      # Thermal diffusivity for Silver (calculated)

# Discretize space and time
dx = length / (num_points_space - 1)
dt = time_total / (num_points_time - 1)

# Initialize temperature arrays
temperature_aluminum = np.zeros((num_points_space, num_points_time))
temperature_silver = np.zeros((num_points_space, num_points_time))

# Set initial condition (e.g., a different heat pulse)
temperature_aluminum[:, 0] = np.sin(np.linspace(0, length, num_points_space))
temperature_silver[:, 0] = np.cos(np.linspace(0, length, num_points_space))

# Finite Difference Method for Aluminum
for n in range(0, num_points_time - 1):
    for i in range(1, num_points_space - 1):
        temperature_aluminum[i, n + 1] = temperature_aluminum[i, n] + alpha_aluminum * (temperature_aluminum[i + 1, n] - 2 * temperature_aluminum[i, n] + temperature_aluminum[i - 1, n]) * dt / dx**2

# Finite Difference Method for Silver
for n in range(0, num_points_time - 1):
    for i in range(1, num_points_space - 1):
        temperature_silver[i, n + 1] = temperature_silver[i, n] + alpha_silver * (temperature_silver[i + 1, n] - 2 * temperature_silver[i, n] + temperature_silver[i - 1, n]) * dt / dx**2

# Plot the temperature distribution over time in 2D for both Aluminum and Silver
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(temperature_aluminum, aspect='auto', extent=[0, time_total, 0, length], cmap='hot', origin='lower')
plt.colorbar(label='Temperature')
plt.title('1D Heat Eq. - Aluminum')
plt.xlabel('Time')
plt.ylabel('Space')


plt.subplot(1, 2, 2)
plt.imshow(temperature_silver, aspect='auto', extent=[0, time_total, 0, length], cmap='hot', origin='lower')
plt.colorbar(label='Temperature')
plt.title('1D Heat Eq. - Silver')
plt.xlabel('Time')
plt.ylabel('Space')

plt.tight_layout()
plt.show()

# Choose a spatial point for the waveform
spatial_point_index = 50  # Adjust as needed

# Plot the temperature waveform over time for both Aluminum and Silver
plt.figure(figsize=(10, 5))
plt.plot(np.linspace(0, time_total, num_points_time), temperature_aluminum[spatial_point_index, :], label='Aluminum', linestyle='--')
plt.plot(np.linspace(0, time_total, num_points_time), temperature_silver[spatial_point_index, :], label='Silver', linestyle='-')
plt.title('Temperature Waveform at Spatial Point ' + str(spatial_point_index))
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()