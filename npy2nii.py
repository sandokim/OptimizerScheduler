import numpy as np
import nibabel as nib

converted_array = numpy.array(normal_array, dtype=numpy.float32) # You need to replace normal array by yours
affine = numpy.eye(4)
nifti_file = nibabel.Nifti1Image(converted_array, affine)

nibabel.save(nifti_file, path_to_save) # Here you put the path + the extionsion 'nii' or 'nii.gz'
