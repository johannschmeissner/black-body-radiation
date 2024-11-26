import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.constants import h, c, k, sigma

# Constants
h = 6.626e-34  # Planck constant (J·s)
c = 3.0e8  # Speed of light (m/s)
k = 1.38e-23  # Boltzmann constant (J/K)

# Planck's law function
def planck(frequency, T):
    return (2 * h * frequency**3 / c**2) / (np.exp(h * frequency / (k * T)) - 1)

# Rayleigh-Jeans law function with truncation
def rayleigh_jeans_truncated(frequency, T, y_max):
    rj = (2 * frequency**2 * k * T) / c**2
    rj[rj > y_max] = np.nan  # Mask values exceeding the specified maximum
    return rj

# Wien's approximation
def wien(frequency, T):
    return (2 * h * frequency**3 / c**2) * np.exp(-h * frequency / (k * T))

# Frequency range (Hz)
freq = np.linspace(1e12, 1e15, 500)  # Frequencies from 10^12 to 10^15 Hz

# Initial temperature
T_init = 3000  # Initial temperature in Kelvin

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
plt.grid()
# Initial maximum y-level for truncation
y_max_factor = 1.2

# Plot initial data
p_line, = ax.plot(freq, planck(freq, T_init), label="Planck's Law", lw=2)
rj_line, = ax.plot(freq, rayleigh_jeans_truncated(freq, T_init, y_max_factor * np.max(planck(freq, T_init))), 
                   label="Rayleigh-Jeans Law (Truncated)", lw=2)
w_line, = ax.plot(freq, wien(freq, T_init), label="Wien's Approximation", lw=2)

# Set axis labels and title
ax.set_title('Black Body Radiation')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Spectral Radiance')
ax.legend()

# Adjust y-axis dynamically based on the peaks
def adjust_y_limits(T):
    y_max = max(np.max(planck(freq, T)), np.max(wien(freq, T))) * y_max_factor
    ax.set_ylim(0, y_max)  # Add some margin above the peak
    return y_max

# Initial y-limit adjustment
y_max = adjust_y_limits(T_init)

# Stefan-Boltzmann luminosity display
def stefan_boltzmann(T):
    return sigma * T**4

l_text = ax.text(0.05, 0.95, f"Stefan-Boltzmann Luminosity: {stefan_boltzmann(T_init):.2e} W/m²",
                 transform=ax.transAxes, fontsize=10, verticalalignment='top')

# Slider for temperature
ax_temp = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
temp_slider = Slider(ax_temp, 'Temperature (K)', 1000, 10000, valinit=T_init, valstep=100)

# Update function
def update(val):
    T = temp_slider.val
    p_line.set_ydata(planck(freq, T))
    w_line.set_ydata(wien(freq, T))
    y_max = adjust_y_limits(T)
    rj_line.set_ydata(rayleigh_jeans_truncated(freq, T, y_max))
    l_text.set_text(f"Stefan-Boltzmann Luminosity: {stefan_boltzmann(T):.2e} W/m²")
    fig.canvas.draw_idle()

temp_slider.on_changed(update)

# Show the plot
plt.show()


