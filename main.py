from astropy.io import fits
from astropy.utils.data import download_file

image_file='sample.fits'   #enter the file_name

#OR you can download file from astropy.org webiste. sample link is provided in this code.

# image_file=download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits',cache=True)


hdul= fits.open(image_file)
image_data=hdul[0].data

print("****************************FILE INFOMATION********************************")
hdul.info()
hdul.close()
print()
print("Header information of the file:")
header=hdul[0].header
for key,value in header.items():
    print(f"{key}\t={value}")
    print()

print("*************************BACKGROUND INFORMATION****************************")
from image_background_data import background
background(image_data)

print("********************************PLOT***************************************")
from image_plot import plot
plot(image_data)

print("******************************HISTOGRAM************************************")
from image_histogram import histo
histo(image_data)


print("*****************************STAR DETECTION********************************")
from image_star_detection import star_detect
star_detect(image_data)
