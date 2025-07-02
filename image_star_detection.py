import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder


def star_detect(data):
    data=np.nan_to_num(data)
    mean,median,std=sigma_clipped_stats(data,sigma=3.00)
    print(f"Background:\nmean:{mean}\nmedian:{median}\nstd:{std}\n")

    daofind=DAOStarFinder(fwhm=3.00,threshold=5*std)
    source=daofind(data-median)

    from astropy.visualization import simple_norm
    flux=source['flux']
    norm=simple_norm(data,"sqrt",percent=99)
    plt.imshow(data,cmap="gray",norm=norm) #norm=normalization done above
    plt.scatter(source['xcentroid'],source['ycentroid'],s=30,c=flux,cmap="plasma",ec="red")
    plt.colorbar(label="flux")
    plt.title(f"star detection. no of star={len(source)} ")
    plt.show()
