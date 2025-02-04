// Set the folder containing images
inputDir = "F:/Eva/CY5_HuRKO/4H/";
outputDir = "F:/Eva/CY5_HuRKO/BandC/4H/";

// Get list of all files in the folder
list = getFileList(inputDir);

// Loop through each file
for (i = 0; i < list.length; i++) {
    if (endsWith(list[i], ".tif")) { // Process only .tif files
        open(inputDir + list[i]);  // Open image
        
        // Adjust brightness and contrast (set your values)
        setMinAndMax(3254, 6020); // Adjust these values based on your images
        run("Apply LUT", "stack");
        
        // Save the modified image in the output directory
        saveAs("Tiff", outputDir + list[i]);

        close(); // Close the image to free memory
    }
}

print("Batch processing complete!");