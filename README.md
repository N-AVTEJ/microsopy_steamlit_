---

# Microscope Resolution Enhancement via Diffraction Simulation

This Streamlit application simulates the diffraction-limited resolution of a microscope using the Airy disk model. It allows users to interactively explore how wavelength, numerical aperture (NA), and noise affect the point spread function (PSF) and resulting image intensity.

## 🔬 Features

* **Airy Disk Simulation**: Computes the diffraction pattern using the first-order Bessel function (J₁) to model the PSF of an optical system.
* **Interactive Controls**:

  * **Wavelength**: Adjustable between 0.4 µm and 1.2 µm.
  * **Numerical Aperture (NA)**: Adjustable between 0.1 and 1.5.
  * **Noise Level**: Adjustable between 0.0 and 0.3 to simulate measurement noise.
* **Log-Scaled Visualization**: Displays the intensity distribution on a logarithmic scale to highlight both central and peripheral features of the Airy pattern.

## 📸 Example Output

![Airy Disk Simulation](./example_output.png)

*Note: Replace with an actual screenshot of the application output.*

## 🚀 Getting Started

### Prerequisites

* Python 3.7 or higher
* pip package manager

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/N-AVTEJ/microsopy_steamlit_.git
   cd microsopy_steamlit_
   ```

2. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

   *If `requirements.txt` is not provided, install the dependencies manually:*

   ```bash
   pip install streamlit numpy matplotlib scipy
   ```

3. **Run the application**:

   ```bash
   streamlit run microscope_simulator.py
   ```

4. **Access the application**:

   Open your web browser and navigate to `http://localhost:8501` to interact with the simulation.

## 🧠 How It Works

The application calculates the intensity distribution of light diffracted through a circular aperture, which is fundamental in understanding the resolution limits of optical systems. The Airy pattern is computed using the formula:

$$
I(r) = \left( \frac{2 J_1(k r \cdot \text{NA})}{k r \cdot \text{NA}} \right)^2
$$

Where:

* $J_1$ is the first-order Bessel function of the first kind.
* $k = \frac{2\pi}{\lambda}$ is the wave number.
* $r$ is the radial distance from the center.
* $\lambda$ is the wavelength of light.
* $\text{NA}$ is the numerical aperture of the system.

By adjusting the wavelength and NA, users can observe changes in the diffraction pattern, illustrating the trade-offs in optical resolution.

## 📁 Project Structure

```
microsopy_steamlit_/
├── microscope_simulator.py  # Main Streamlit application
├── requirements.txt         # Python dependencies (if provided)
└── README.md                # Project documentation
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## 🙌 Acknowledgments

Developed by [N-AVTEJ](https://github.com/N-AVTEJ) as an educational tool to demonstrate the principles of optical diffraction and resolution.

---

*For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/N-AVTEJ/microsopy_steamlit_).*

---
