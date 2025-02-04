import os
import imageio
import tifffile


def cutting_by_eye(file_path, file_path_save):
    for item in os.listdir(file_path):
        file = f"{file_path}/{item}"
        segmented_array_cytoplasm = imageio.v2.imread(file)
        while True:
            print()
            print(f'Open the file {file_path}/{item} in ImageJ')
            print('In the next two questions reply with an integer')
            start_stack = (input("The first stack were the cut needs to be, is at: "))
            end_stack = (input("The last stack were the cut needs to be, is at: "))

            try:
                start_stack = int(start_stack)
                end_stack = int(end_stack)

            except ValueError:
                print('\nYou did not put in an integer, try again.')
                continue


            if item.endswith(".tif"):
                item = item[:-4]

            file = f"{file_path}/{item}.tif"
            segmented_array_cytoplasm = imageio.v2.imread(file)

            if start_stack < end_stack and start_stack >= 0 and end_stack <= segmented_array_cytoplasm.shape[0]:
                tifffile.imwrite(f"{file_path_save}/{item}_{start_stack}_{end_stack}.tif",
                                    segmented_array_cytoplasm[start_stack:end_stack, :, :])
                os.remove(f"{file_path}/{item}.tif")
                break

            else:
                print()
                print('These stacks do not exist, try again.')
                continue

    if len(os.listdir(file_path)) == 0:
        os.rmdir(file_path)
    print()
    print(f'All the images in folder {file_path} have been cut and saved in the folder {file_path_save}')

    return

#Input
#THE INPUT SHOULD BE TIF IMAGES IN 3D AND ALREADY B&C ADJUSTED (BLOW UP THE CONTRAST AND BRIGHTNESS)
file_path =f"F:/Eva/CY5_HuRKO/cut/4H/not_cut_yet" #Add the filepath with all the images that need cutting by eye (file_path_save/not_cut_yet)
file_path_save = f"F:/Eva/CY5_HuRKO/cut/4H" #Add here the filepath where all the images need to be saved after cutting

cutting_by_eye(file_path, file_path_save)