import numpy as np
import pandas as pd
from tqdm import tqdm
from PIL import Image

from Model.rtree import index
from image_viewer import ImageViewer

# Constants
IMAGES_DIR = 'Data/Images/'

#load the data
points = np.load('Data/features.npy')
insert_count = min(1000, len(points))
dim = points.shape[2]   ##
print(f'Dimension: {dim}')

img_files = pd.read_csv('Data/mapping.csv')

# Create the rtree index for dim-dimensional data
idx = index.Index(properties=index.Property(dimension=dim))

# Insert some points into the index
for i in tqdm(range(insert_count)):
    idx.insert(i, tuple(points[i][0]))
    



# # Find the M nearest point to a given point
M = 4
while True:
    query_indx = int(input('Enter a index: '))
    if query_indx==-1: 
        print("Bye!")
        break
    query_point = points[query_indx][0]
    nearest = list(idx.nearest(tuple(query_point), M))
  
    
    query_img = IMAGES_DIR+img_files.iloc[query_indx]['filename']
    matched_imgs = []
    
    for i in range(M):
        matched_imgs.append(IMAGES_DIR+img_files.iloc[nearest[i]]['filename'])
    
    ImageViewer(query_img, matched_imgs)
        
        
    print("\n")