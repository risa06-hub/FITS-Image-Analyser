import matplotlib.pyplot as plt
import numpy as np

def plot(data):
    #make  data better
    data=np.nan_to_num(data)
    data= data - np.min(data)
    data=data/np.ptp(data)
    plt.imshow(data,cmap="grey",origin="lower") #you can change cmap to inferno, hot, plasma
    plt.title("IMAGE PLOT")
    plt.colorbar()
    plt.show()
