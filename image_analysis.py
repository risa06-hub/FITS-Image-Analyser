from astropy.io import fits
# Proceed with FITS operations
def info(file):
    hdul=fits.open(file)
    image_data=hdul[0].data
    print("FILE INFORMATION:")
    hdul.info()
    hdul.close()
    print()
    print("Header information of the file:")
    header=hdul[0].header
    for key,value in header.items():
        print(f"{key}\t={value}")
        print()
