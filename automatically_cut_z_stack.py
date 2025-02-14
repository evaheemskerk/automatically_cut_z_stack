import numpy as np
import shutil
import os
from scipy.signal import find_peaks
import imageio
import tifffile

#This definition is to smooth the curves
def smooth(data, number_of_points=7):
    return np.convolve(data, np.ones(number_of_points)/number_of_points, mode='valid')

def cut_z_stack(file_path, file_path_save, high_intensity):
    not_cut = []


    #This for loop goes trough all the files in the folder
    for item in os.listdir(file_path):
        file = f"{file_path}/{item}"
        segmented_array_cytoplasm = imageio.v2.imread(file)
        zero_count_list = []
        high_count_list = []

        for i, slice_2d in enumerate(segmented_array_cytoplasm):
            #count how many pixels with the intensity value of zero and higher than the high_intensity value
            zero_count = np.count_nonzero(slice_2d == 0)
            zero_count_list.append(zero_count)

            high_count = np.count_nonzero(slice_2d > high_intensity)
            high_count_list.append(high_count)

        #Smooth the data using a moving average
        #https://stackoverflow.com/questions/20618804/how-to-smooth-a-curve-for-a-dataset & chatGPT: https://chatgpt.com/share/678f80e5-4a70-8007-9dd7-a342762d73a7
        smoothed_zeros = smooth(np.array(zero_count_list))
        smoothed_high = smooth(np.array(high_count_list))

        #Find the derivatives of the smoothed curves
        derivative_zeros = np.gradient(smoothed_zeros)
        derivative_high = np.gradient(smoothed_high)

        #Find the peaks or valleys in the derivatives, these are the places where the cuts should be
        cut_end_zeros, _ = find_peaks(-derivative_zeros, height = 5000)
        cut_start_zeros, _ = find_peaks(derivative_zeros)

        cut_end_high, _ = find_peaks(-derivative_high, height = 5000)
        cut_start_high, _ = find_peaks(derivative_high)

        if item.endswith(".tif"):
            item = item[:-4]

        if len(cut_start_zeros) == 1 and len(cut_end_zeros) == 1 and cut_start_zeros[0]<cut_end_zeros[0]:
            cut_start_zeros = cut_start_zeros[0]
            cut_end_zeros = cut_end_zeros[0]
            tifffile.imwrite(f"{file_path_save}/{item}_{cut_start_zeros}_{cut_end_zeros}.tif",
                             segmented_array_cytoplasm[cut_start_zeros-1:cut_end_zeros,:,:],)


        elif len(cut_start_high) == 1 and len(cut_end_high) == 1 and cut_start_high[0]<cut_end_high[0]:
            cut_start_high = cut_start_high[0]
            cut_end_high = cut_end_high[0]
            tifffile.imwrite(f"{file_path_save}/{item}_{cut_start_high}_{cut_end_high}.tif",
                             segmented_array_cytoplasm[cut_start_high-1:cut_end_high, :, :])

        else:
            not_cut.append(item)
            print(f'For file {file}, the cutting did not work. '
                  f'It suggested: cut start {cut_start_zeros} and cut end {cut_end_zeros}. '
                  f'Or: cut start {cut_start_high} and cut end {cut_end_high}')



    while True:
        if len(not_cut)>0:

            print()
            print(f"There are images that need to be cut by eye.")
            go_on = input("Do you want to continue with cutting these images [Y/N]? ")

            if go_on == 'Y':
                for item in not_cut:
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


                        #hier nog iets toevoegen van als niet integer, geen error maar opnieuw!!

                        if item.endswith(".tif"):
                            item = item[:-4]

                        file = f"{file_path}/{item}.tif"
                        segmented_array_cytoplasm = imageio.v2.imread(file)

                        if start_stack < end_stack and start_stack>=0 and end_stack <= segmented_array_cytoplasm.shape[0]:
                            tifffile.imwrite(f"{file_path_save}/{item}_{start_stack}_{end_stack}.tif",
                                segmented_array_cytoplasm[start_stack-1:end_stack, :, :])
                            break

                        else:
                            print()
                            print('These stacks do not exist, try again.')
                            continue

                print()
                print(f'All the images in folder {file_path} have been cut and saved in the folder {file_path_save}')
                break

            if go_on == 'N':
                folder_path_not_cut = f"{file_path_save}/not_cut_yet"
                os.mkdir(folder_path_not_cut)
                for item in not_cut:
                    shutil.copyfile(f'{file_path}/{item}.tif', f'{folder_path_not_cut}/{item}.tif')
                if len(os.listdir(folder_path_not_cut)) == 0:
                    os.rmdir(folder_path_not_cut)
                print()
                print(f"All the images that still need to be cut are in the folder {folder_path_not_cut}")
                break

            else:
                print("Only the inputs 'Y' or 'N' are accepted")
                continue

        else:
            print(f'All the images in folder {file_path} have been cut and saved in the folder {file_path_save}')
            break

    return

#Input
#THE INPUT SHOULD BE TIF IMAGES IN 3D AND ALREADY B&C ADJUSTED (BLOW UP THE CONTRAST AND BRIGHTNESS)
file_path =f"F:/Eva/CY5_HuRKO/BandC/4H" #Add is the filepath with all the images that need cutting
file_path_save = (f"F:/Eva/CY5_HuRKO/cut/4H") #Add here the filepath where all the images need to be saved after cutting
high_intensity = 60000 #Add here the value of the highest intensity

cut_z_stack(file_path, file_path_save, high_intensity)
