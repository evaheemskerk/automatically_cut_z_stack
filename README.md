# automatically_cut_z_stack
This algorithm allows you to automatically crop images in a Z-stack by detecting and retaining only the sharpest regions. It identifies the starting and ending points where the images remain in focus, ensuring that only the sharpest slices are kept.

# Installation
Before using the algorithm please make sure that you have the following libraries in your local environment: 
numpy, os, shutil, scipy.signal, imageio

# Usage 

## Inputs 
file_path: The path to the folder were the images are saved. The images should be .tif images and are thus 2D images with a Z-direction. IMPORTANT: The images should already been pre-processed, so the brightness & contrast needs to be adjusted. Preferably the brightness and contrast should be blown up. 
file_path_save: The path to the folder were the cutted images should be saved. 
high_intensity: Fill in the value where intensity of the cells in high. You can check this by opening your image in ImageJ and go over the cells and check the intensity. In my case this was around 60000. 

## Running and interactively cut the images
Then run the code. If the code finds the cuts well it will save the images in the stored place. If the code worked for all the images, they are stored in the folder {file_path_saved} However, in some cases the images do not work for the current code. The code then asks you: 

"There are images that need to be cut by eye."
"Do you want to continue with cutting these images [Y/N]?" 

Type 'N' if you do not want to cut the other images at the moment. The not cutted images are then stored in a folder with the path {file_path_saved}/not_cut_yet. 
Type 'Y' if you want to continue cutting. Then you will get the following question: 

"Open the file {file-path}/{item} in ImageJ"
"In the next two questions reply with an integer"
"The first stack were the cut needs to be, is at: "
"The last stack were the cut needs to be, is at: " 

For both questions type an integer were the cuts need to be. The slices of the integers your put in are also taken into the Z-stacks of the cutes. This will go through all the images for which the code did not work and cut these images by eye. Hopefully, this would speed up the process. 

# Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

