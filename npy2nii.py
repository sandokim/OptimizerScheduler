import numpy as np
import nibabel as nib

path_to_save = '../..nii'

converted_array = np.array(normal_array, dtype=np.float32) # You need to replace normal array by yours
affine = np.eye(4)
nifti_file = nib.Nifti1Image(converted_array, affine)

nib.save(nifti_file, path_to_save) # Here you put the path + the extionsion 'nii' or 'nii.gz'
