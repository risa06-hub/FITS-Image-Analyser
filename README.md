# FITS Image Analysis Project

## 📖 Overview

This project performs analysis on astronomical FITS (Flexible Image Transport System) images using python, Astropy, Matplotlib, Photutils. It is designed to extract the data from the .fits file, plot the image, histogram and star detection.

## 🛠 Features

- Load and analysis the data of the file
- Analysis functions: photometry, star detection, histogram analysis
- Visualization: matplotlib-based display of FITS images 

## 🚀 Getting Started

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

## 🔧 How It Works

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

   
