from pathlib import Path
import nibabel
from fileformats.core import FileSet
from fileformats.medimage import MedicalImage, Nifti, NiftiGz, Nifti1, NiftiGzX, NiftiX
import medimages4tests.dummy.nifti


@FileSet.load_metadata.register
def nifti_load_metadata(nifti: Nifti):
    return dict(nibabel.load(nifti.fspath).header)


@MedicalImage.read_array.register
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


@FileSet.generate_test_data.register
def nifti_generate_test_data(nifti: Nifti1, dest_dir: Path):
    return medimages4tests.dummy.nifti.get_image(out_file=dest_dir / "nifti.nii")


@FileSet.generate_test_data.register
def nifti_gz_generate_test_data(nifti: NiftiGz, dest_dir: Path):
    return medimages4tests.dummy.nifti.get_image(
        out_file=dest_dir / "nifti.nii.gz", compressed=True
    )


@FileSet.generate_test_data.register
def nifti_gz_x_generate_test_data(nifti: NiftiGzX, dest_dir: Path):
    return medimages4tests.mri.neuro.t1w.get_image()


@FileSet.generate_test_data.register
def nifti_x_generate_test_data(nifti: NiftiX, dest_dir: Path):
    nifti_gz_x = NiftiGzX(medimages4tests.mri.neuro.t1w.get_image())
    return NiftiX.convert(nifti_gz_x)
