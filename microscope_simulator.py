import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.special import j1  # Correct Bessel function for Airy disk

# Function to calculate diffraction pattern using Airy disk model
def airy_disk(wavelength, na, size=512):
    # Define the spatial range in micrometers
    x = np.linspace(-5, 5, size)
    y = np.linspace(-5, 5, size)
    X, Y = np.meshgrid(x, y)
    r = np.sqrt(X**2 + Y**2)

    # Calculate the radius of Airy disk
    k = 2 * np.pi / wavelength
    alpha = na / wavelength
    kr = k * r * na

    # Avoid divide-by-zero at center
    kr[kr == 0] = 1e-10

    # Airy pattern intensity using first-order Bessel function
    intensity = (2 * j1(kr) / kr) ** 2
    return intensity, x, y

# Streamlit UI
st.title("Microscope Resolution Enhancement through Diffraction Simulation")

# Input parameters
wavelength = st.slider("Wavelength (in micrometers)", 0.4, 1.2, 0.55, step=0.01)
na = st.slider("Numerical Aperture (NA)", 0.1, 1.5, 1.2, step=0.05)
noise_level = st.slider("Noise Level", 0.0, 0.3, 0.0, step=0.01)

# Compute pattern
intensity, x, y = airy_disk(wavelength, na)

# Add noise
if noise_level > 0:
    noise = np.random.normal(0, noise_level, intensity.shape)
    intensity += noise
    intensity = np.clip(intensity, 1e-6, None)  # Avoid log(0)

# Plotting
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(intensity, extent=[x.min(), x.max(), y.min(), y.max()],
               norm=LogNorm(vmin=1e-6, vmax=1), cmap='inferno', origin='lower')
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Intensity (log scale)')
ax.set_xlabel("X (μm)")
ax.set_ylabel("Y (μm)")
ax.set_title(f"Wavelength = {wavelength*1000:.0f} nm, NA = {na}")

# Show in Streamlit
st.pyplot(fig)
