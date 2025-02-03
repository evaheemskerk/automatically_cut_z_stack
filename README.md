# automatically_cut_z_stack
This algorithm allows you to automatically crop images in a Z-stack by detecting and retaining only the sharpest regions. It identifies the starting and ending points where the images remain in focus, ensuring that only the sharpest slices are kept.

# Installation
Before using the algorithm, ensure you have the following libraries installed in your local environment: numpy, scipy, imageio. 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these.

```bash
pip install numpy scipy imageio
```


# Usage 

## Inputs 
* **file_path**: The path to the folder were the images are saved. The images should be .tif images and are thus 2D images with a Z-direction. 
    * IMPORTANT: The images should be pre-processed (brightness & contrast adjusted). Preferably, brightness and contrast should be enhanced for better performance. <p>
* **file_path_save**: Path to the folder where the cropped images should be saved. <p>
* **high_intensity**: The intensity value representing bright regions in the images. You can check this by opening an image in ImageJ and inspecting pixel intensities. In my case, this was around 60.000. 

## Running and interactively cut the images
Run the script, and if it correctly detects the cuts, the processed images will be saved in {file_path_save}. However, if the automatic detection fails for some images, the script will prompt you with: <p>


```python
"There are images that need to be cut by eye."
"Do you want to continue with cutting these images [Y/N]?" 
```

Type 'N' to skip manual cutting. The unprocessed images will be stored in {file_path_saved}/not_cut_yet.<p>
Type 'Y' to proceed with manual cutting. You will be prompted with: <p>

```python
"Open the file {file-path}/{item} in ImageJ" 
"In the next two questions reply with an integer" 
"The first stack were the cut needs to be, is at: " 
"The last stack were the cut needs to be, is at: "  
```

Enter the corresponding slice indices where cuts should be applied. These slices will be included in the final processed Z-stack. The process will repeat for all images that required manual intervention, significantly speeding up the workflow.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. <p>

Please make sure to update tests as appropriate.

