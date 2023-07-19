import pydicom
import numpy as np
from fileformats.core import FileSet
from fileformats.medimage import MedicalImage, DicomCollection


@MedicalImage.read_array.register
def dicom_read_array(collection: DicomCollection):
    image_stack = []
    for dcm_file in collection.contents:
        image_stack.append(pydicom.dcmread(dcm_file).pixel_array)
    return np.asarray(image_stack)


@FileSet.load_metadata.register
def dicom_load_metadata(collection: DicomCollection, index=0, specific_tags=None):
    # TODO: Probably should collate fields that vary across the set of
    #       files in the set into lists
    return pydicom.dcmread(list(collection.contents)[index], specific_tags=specific_tags)


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
    return int(collection.load_metadata(specific_tags=[SERIES_NUMBER_TAG])[0])


SERIES_NUMBER_TAG = ("0020", "0011")
