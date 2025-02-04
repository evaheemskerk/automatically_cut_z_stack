# automatically_cut_z_stack
This algorithm allows you to automatically crop images in a Z-stack by detecting and retaining only the sharpest regions. It identifies the starting and ending points where the images remain in focus, ensuring that only the sharpest slices are kept.

# Content
* Adjust_B_and_C_folder.ijm - ImageJ macro to adjust the brightness and contrast of all images in a folder.
* automatically_cut_z_stack.py - Script that processes all images in a folder, automatically cropping them based on sharpness. If automatic cutting fails for some images, the script prompts the user to continue with manual cutting.
* manual_cutting.py - Script for manually cutting images that could not be processed automatically.
  
# Pre-processing the images 
Before running the algorithm, it is important to pre-process the images by adjusting brightness and contrast. You can use the ImageJ macro called Adjust_B_and_C_folder.ijm to batch process the images.

## Using the ImageJ Macro
Save the ImageJ macro somewhere on your laptop. Open the macro in ImageJ using: Plugins -> Macros ->  Edit. Set the input and output directories:

```ImageJ
inputDir = "F:/Eva/CY5_HuRKO/4H/";
outputDir = "F:/Eva/CY5_HuRKO/BandC/4H/";
```

For my own images, I used the following Brightness & Contrast values:

```ImageJ
setMinAndMax(3254, 6020)
```
These values may vary depending on your images. Adjust them as needed to optimize the visibility of relevant structures. After changing them, you can press 'Run'. 

# Usage of automatically_cutting_z_stack

## Installation
Before using the python algorithm, ensure you have the following libraries installed in your local environment: numpy, scipy, imageio, tifffile. 
If not; use the package manager [pip](https://pip.pypa.io/en/stable/) to install these.

```bash
pip install numpy scipy imageio tifffile
```

## Inputs 
Change the inputs at the bottom of the script. 
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

Type 'N' to skip manual cutting. The unprocessed images will be stored in {file_path_saved}/not_cut_yet. You can continue automatically cutting on a later moment using the code 'manuel_cutting.py' <p>
Type 'Y' to proceed with manual cutting. You will be prompted with: <p>

```python
"Open the file {file-path}/{item} in ImageJ" 
"In the next two questions reply with an integer" 
"The first stack were the cut needs to be, is at: " 
"The last stack were the cut needs to be, is at: "  
```

Enter the corresponding slice indices where cuts should be applied. These slices will be included in the final processed Z-stack. The process will repeat for all images that required manual intervention, significantly speeding up the workflow.

# Usage of manual_cutting.py
If you want to continue manual cutting at a later time, this is possible because images that were not automatically cut are saved in {file_path_saved}/not_cut_yet.

## Installation
Before using the python algorithm, ensure you have the following libraries installed in your local environment: imageio, tifffile. 
If not; use the package manager [pip](https://pip.pypa.io/en/stable/) to install these.

```bash
pip install imageio tifffile
```

## Inputs 
To proceed, update the following inputs at the bottom of the manual_cutting.py script:

* file_path: Path to the folder containing images that still need to be cut manually. (This corresponds to {file_path_saved}/not_cut_yet from the automatically_cut_z_stack.py script.)
* file_path_save: Path to the folder where the manually cut images should be saved. (This should match {file_path_saved} from automatically_cut_z_stack.py.)
  
## Running and interactively cut the images
You will be prompted with: <p>

```python
"Open the file {file-path}/{item} in ImageJ" 
"In the next two questions reply with an integer" 
"The first stack were the cut needs to be, is at: " 
"The last stack were the cut needs to be, is at: "  
```

Enter the corresponding slice indices where cuts should be applied. These slices will be included in the final processed Z-stack. The process will repeat for all images that required manual intervention, significantly speeding up the workflow.

# FAQ

### Q: The code does not work for many images. What could be the cause?
This issue is likely due to improper brightness & contrast adjustments. Ensure that brightness and contrast are sufficiently enhanced, but avoid making the entire image too bright, as this can affect sharpness detection.

### Q: After automatic cutting, I pressed 'N' to skip manual cutting, but the process is still taking a long time. Why?
This happens because saving the images to a new folder takes some time. Please be patient while the process completes.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. <p>

Please make sure to update tests as appropriate.

