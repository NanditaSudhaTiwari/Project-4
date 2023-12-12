import numpy as np
import matplotlib.pyplot as plt

# Parameters
length = 14   # Length of the rod
time_total = 3600   # Total simulation time
num_points_space = 100  # Number of spatial points
num_points_time = 2000   # Number of time points

# Thermal diffusivities
alpha_one = #Look at the thermal diffusivity table and choose a coefficient of a material you like
alpha_two = #Look at the thermal diffusivity table and choose a second coefficient of a material you like

# Discretize space and time
dx = length / (num_points_space - 1)
dt = time_total / (num_points_time - 1)

# Initialize temperature arrays
temperature_one = np.zeros((num_points_space, num_points_time))
temperature_two = np.zeros((num_points_space, num_points_time))

# Set initial condition (e.g., a different heat pulse)
temperature_one[:, 0] = np.sin(np.linspace(0, length, num_points_space))
temperature_two[:, 0] = np.cos(np.linspace(0, length, num_points_space))

# Finite Difference Method for Material 1
for n in range(0, num_points_time - 1):
    for i in range(1, num_points_space - 1):
        '''
        We have given you a hint on how to iterate through the problem, now, write the code that will correctly solve the heat equation
        temperature_one is an array that should have all the values of temperature over all values of space and time
        '''
# Finite Difference Method for Material 2
for n in range(0, num_points_time - 1):
    for i in range(1, num_points_space - 1):
        '''
        Can you repeat the procedure again?
        '''
        

# Plot the temperature distribution over time in 2D for both Materials 1 and 2
#If you are correctly changing the temperature arrays, then there should be no problem with the plotting
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(temperature_one, aspect='auto', extent=[0, time_total, 0, length], cmap='hot', origin='lower')
plt.colorbar(label='Temperature')
plt.title('1D Heat Eq. - ') #Please change to show the element you chose
plt.xlabel('Time')
plt.ylabel('Space')


plt.subplot(1, 2, 2)
plt.imshow(temperature_two, aspect='auto', extent=[0, time_total, 0, length], cmap='hot', origin='lower')
plt.colorbar(label='Temperature')
plt.title('1D Heat Eq. - ') #Please change to show the element you chose
plt.xlabel('Time')
plt.ylabel('Space')

plt.tight_layout()
plt.show()

# Choose a spatial point for the waveform
spatial_point_index = 50  # Adjust as needed

# Plot the temperature waveform over time for both Aluminum and Silver
plt.figure(figsize=(10, 5))
plt.plot(np.linspace(0, time_total, num_points_time), temperature_one[spatial_point_index, :], label='Element 1', linestyle='--')
plt.plot(np.linspace(0, time_total, num_points_time), temperature_two[spatial_point_index, :], label='Element 2', linestyle='-')
plt.title('Temperature Waveform at Spatial Point ' + str(spatial_point_index))
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()


