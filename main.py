import pandas as pd
# import numpy as np
from create_files_list import get_image_list
from imageparams import get_image_params
from check_similarity_duplicity import check_similarity

'''
    List image files from given list of folders (search subfolders too)
    find image blur,brightness & hash values
    find duplicate/similar images using the hash
    '''

folders_list = [r'D:\My Documents\SkyDrive\images'
                # , r'C:\Users\nir-pc\Desktop\New folder'
                # , r'D:\My Documents\Pictures'
                # , r'C:\Users\nir-pc\Desktop\New folder (2)'
                # , r'D:\My Documents\SkyDrive\images', r'G:\My Drive\pics'
                ]

images = get_image_list('')  # folders_list or any other value for using existing file
print(f'received list of {len(images)} files')
# loop over the input images
image_params = pd.DataFrame(columns=['file', 'blur', 'brightness', 'hash'])
imp = []
for image in images[:]:
    try:
        imp = get_image_params(image)
        image_params.loc[image_params.shape[0],] = imp
    except Exception as e:
        # raise e
        pass

print(f'extracted files parameters')
similar = check_similarity(image_params[['file', 'hash']])
image_params = pd.merge(image_params, similar[['file','similar_images']], on='file')
print(f'similarity checked')

pd.DataFrame.to_csv(image_params, 'image_params.csv')
