import nibabel
from fileformats.core import FileSet
from fileformats.medimage import MedicalImage
from fileformats.medimage.nifti import Nifti


@FileSet.load_metadata.register
def nifti_load_metadata(nifti: Nifti):
    return dict(nibabel.load(nifti.fspath).header)


@MedicalImage.read_data_array.register
def nifti_data_array(nifti: Nifti):
    return nibabel.load(nifti.fspath).get_data()


@MedicalImage.vox_sizes.register
def nifti_vox_sizes(nifti: Nifti):
    # FIXME: This won't work for 4-D files
    return nifti.metadata["pixdim"][1:4]


@MedicalImage.dims.register
def nifti_dims(nifti: Nifti):
    # FIXME: This won't work for 4-D files
    return nifti.metadata["dim"][1:4]
