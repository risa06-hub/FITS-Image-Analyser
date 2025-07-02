import matplotlib.pyplot as plt
import numpy as np
def histo(data):
    data_1d=data.ravel()
    plt.hist(data_1d,bins="auto",fc="k",ec="b")
    plt.title("HISTOGRAM")
    plt.ylabel("frequency")
    plt.xlabel("pixles")
    plt.show()

