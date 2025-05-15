

# Microscope Resolution Enhancement through Diffraction Simulation

This Streamlit application simulates the diffraction pattern of a microscope using the Airy disk model. It allows users to explore how varying the wavelength of light, numerical aperture (NA), and noise levels affect the resolution of a microscope. The simulation provides an interactive visualization of the Airy disk pattern, aiding in the understanding of diffraction limits in optical systems.

## Features

* **Interactive Sliders**: Adjust the wavelength (in micrometers), numerical aperture (NA), and noise level to observe their impact on the diffraction pattern.
* **Real-time Visualization**: The application generates and displays the Airy disk intensity pattern using Matplotlib, updating in real-time as parameters change.
* **Noise Simulation**: Add Gaussian noise to the intensity pattern to simulate real-world imperfections in imaging systems.
* **Logarithmic Intensity Scale**: Visualize intensity on a logarithmic scale to capture a wide dynamic range.

## Installation

To run this application locally, ensure you have Python 3.7 or later installed. Follow the steps below:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/N-AVTEJ/microsopy_steamlit_.git
   cd microsopy_steamlit_
   ```



2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```



If `requirements.txt` is not provided, install the necessary packages manually:

```bash
pip install streamlit numpy matplotlib scipy
```



## Usage

To launch the Streamlit application, run the following command in the project directory:

```bash
streamlit run microscope_simulator.py
```



This will open the application in your default web browser. If it doesn't open automatically, navigate to `http://localhost:8501` in your browser.

## Application Overview

Upon launching, you'll see sliders to adjust the following parameters:

* **Wavelength (μm)**: Set the wavelength of light used in the simulation (0.4 to 1.2 μm).
* **Numerical Aperture (NA)**: Adjust the NA of the microscope objective (0.1 to 1.5).
* **Noise Level**: Introduce Gaussian noise to the intensity pattern (0.0 to 0.3).

As you modify these parameters, the application will update the Airy disk intensity pattern accordingly. The visualization helps in understanding how these factors influence the resolution and quality of microscopic images.

## File Structure

```plaintext
microsopy_steamlit_/
├── microscope_simulator.py  # Main Streamlit application script
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies (if provided)
```



## Dependencies

* [Streamlit](https://streamlit.io/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [SciPy](https://www.scipy.org/)([Streamlit][1])

Ensure all dependencies are installed as per the instructions in the Installation section.([Medium][2])

## Contributing

Contributions are welcome! If you'd like to enhance the application or fix any issues:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request detailing your changes.([Toolify][3])

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.([GitHub][4])

## Acknowledgments

This application was developed to aid in the visualization and understanding of diffraction patterns in microscopy. Special thanks to the developers of Streamlit, NumPy, Matplotlib, and SciPy for their invaluable tools.
