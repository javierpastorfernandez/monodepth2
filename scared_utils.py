#!/usr/bin/env python3
# Import dependencies
import numpy as np
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.axes_grid1 import ImageGrid
import math
import matplotlib.pyplot as plt
verbose=False

# UTILS
def image_analizer(img):
    if isinstance(img,(np.ndarray)):
        print("-----------------------------------------------")
    else:
        if isinstance(img,(list)):
            print("Converting list to numpy array...")
            img = np.array(img)
        else:
            raise Exception('Wrong type')      
            
    print("Type: ",type(img))
    print("Shape: ",img.shape)
    print("Min value: ",np.amin(img))
    print("Max value: ",np.amax(img))
    
    
#SktLearnt different sscalers:
    # Ref 01: https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py
    
def image_normalizer(img,option):
    #np.ptp (peak to peak -> Max - min of an array)
    if option==1:
        # Normalize to [0,1] --> Preserves the data type
        img_norm= (img - np.min(img))/(np.ptp(img))
        
    elif option==2:
        # Normalize to [0,255] --> Image to int
        img_norm= (255*(img - np.min(img))/(np.ptp(img))).astype(int)
        
    elif option==3:
        # Normalize to [-1,1] -> Conserves the same data type
        img_norm = 2.*(img - np.min(img))/np.ptp(img)-1
    
    elif option==4:
        # Subtracting by the mean and dividing by the standard deviation
        # Zero centered
        scaler = StandardScaler()
        img_norm=scaler.fit(img)
    return img_norm


def grid_plot(img_list,fig,num_images):
    n_rows=math.ceil(math.sqrt(num_images))
    n_cols=math.ceil(num_images/n_rows)


    grid = ImageGrid(fig, 111,  # similar to subplot(111)
                     nrows_ncols=(n_rows, n_cols),  # creates 2x2 grid of axes
                     axes_pad=0.1,  # pad between axes in inch.
                     )
    for index_,(ax, im) in enumerate(zip(grid,img_list)):
        if verbose:
            print(index_)
        # Iterating over the grid returns the Axes.
        ax.imshow(im)
        ax.axis('off')
    plt.show()
   