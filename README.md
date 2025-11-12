# FITS Image Analysis Project

## Overview

This project performs analysis on astronomical FITS (Flexible Image Transport System) images using python, Astropy, Matplotlib, Photutils. It is designed to extract the data from the .fits file, plot the image, histogram and star detection.

# Features

- Load and analysis the data of the file
- Analysis functions: photometry, star detection, histogram analysis
- Visualization: matplotlib-based display of FITS images 

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- `astropy`
- `matplotlib`
- `numpy`
- `photutils`


Install dependencies with:

```bash
pip install -r requirements.txt
```

## How It Works

The project follows a step-by-step pipeline to analyze FITS images:

1. **Load FITS File**  
   The user can provide a FITS image, a sample FITS file has been included in the code. The program uses `astropy.io.fits` to read the file and extract image data.

3. **Preprocess Image**  
   - extract background information of the image like mean, median,std.
  
4. **Plotting**
    - Normalising
    - choose a prefered cmap
    - plot the image using matplotlib
5. **Histogram**
    - historgram analysis: frequency vs pixles
    - used .ravel() to convert 2D array into 1D array to plot the histogram 

4. **Star Detection**  
    - background information was analysed using sigma clipping and a threshold of 5*std was set to detect stars in the image
    - the data was subtracted from the median to obtain a source file

## 🔭 Sample FITS Files for Testing

To try this project, you can download sample `.fits` files using Python:

```python
from astropy.utils.data import download_file
from astropy.io import fits

url = "http://data.astropy.org/tutorials/FITS-images/HorseHead.fits"
file_path = download_file(url, cache=True)
hdul = fits.open(file_path)
hdul.info()
```
### More resources for FITS file 
- **Astropy Sample Data**  
  [http://data.astropy.org/tutorials/FITS-images/](http://data.astropy.org/tutorials/FITS-images/)  
  Hosted by the Astropy team, includes files used in official tutorials.

- **NASA SkyView Virtual Observatory**  
  [https://skyview.gsfc.nasa.gov/](https://skyview.gsfc.nasa.gov/)  
  Allows generation of custom FITS images from multiple surveys.

- **Sloan Digital Sky Survey (SDSS)**  
  [https://skyserver.sdss.org](https://skyserver.sdss.org)  
  Provides FITS images and spectra of millions of celestial objects.

- **Hubble Legacy Archive (HLA)**  
  [https://hla.stsci.edu/](https://hla.stsci.edu/)  
  Repository of processed images from the Hubble Space Telescope.

