from astropy.io import fits
from astropy.stats import sigma_clipped_stats

def background(data):
    #to get the background info of the image
    mean,median,std=sigma_clipped_stats(data,sigma=3.00)
    print(f"Background : mean={mean}\nmedian={median}\nstd={std}")
