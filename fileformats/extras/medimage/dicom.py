from pathlib import Path
import pydicom
import numpy as np
from fileformats.core import FileSet
from fileformats.medimage import MedicalImage, DicomCollection, DicomDir, DicomSet
import medimages4tests.dummy.dicom.mri.t1w.siemens.skyra.syngo_d13c


@MedicalImage.read_array.register
def dicom_read_array(collection: DicomCollection):
    image_stack = []
    for dcm_file in collection.contents:
        image_stack.append(pydicom.dcmread(dcm_file).pixel_array)
    return np.asarray(image_stack)


@FileSet.read_metadata.register
def dicom_read_metadata(collection: DicomCollection, index=0, specific_tags=None):
    # TODO: Probably should collate fields that vary across the set of
    #       files in the set into lists
    return pydicom.dcmread(
        list(collection.contents)[index], specific_tags=specific_tags
    )


@MedicalImage.vox_sizes.register
def dicom_vox_sizes(collection: DicomCollection):
    return tuple(
        collection.metadata["PixelSpacing"] + [collection.metadata["SliceThickness"]]
    )


@MedicalImage.dims.register
def dicom_dims(collection: DicomCollection):
    return tuple(
        (
            collection.metadata["Rows"],
            collection.metadata["DataColumns"],
            len(list(collection.contents)),
        ),
    )


@DicomCollection.series_number.register
def dicom_series_number(collection: DicomCollection):
    return int(collection.read_metadata(specific_tags=[SERIES_NUMBER_TAG])[0])


@FileSet.generate_sample_data.register
def dicom_dir_generate_sample_data(dcmdir: DicomDir, dest_dir: Path):
    return medimages4tests.dummy.dicom.mri.t1w.siemens.skyra.syngo_d13c.get_image(dest_dir / "dicom_dir")


@FileSet.generate_sample_data.register
def dicom_set_generate_sample_data(dcmdir: DicomSet, dest_dir: Path):
    dicom_dir = dicom_dir_generate_sample_data(dest_dir)
    return list(dicom_dir.iterdir())


SERIES_NUMBER_TAG = ("0020", "0011")
