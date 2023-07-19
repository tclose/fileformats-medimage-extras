import numpy as np
from fileformats.medimage.diffusion import DwiEncoding, Bval, Bvec, Bfile


@Bval.read_array.register
def bval_read_array(bval: Bval):
    return np.asarray([float(ln) for ln in bval.read_contents().split()])


@DwiEncoding.read_array.register
def bvec_read_array(bvec: Bvec):
    bvals = bvec.b_values_file.read_array()
    directions = np.asarray(
        [[float(x) for x in ln.split()] for ln in bvec.read_contents().splitlines()]
    ).T
    return np.concatenate((directions, bvals.reshape((-1, 1))), axis=1)  # type: ignore


@DwiEncoding.read_array.register
def bfile_read_array(bfile: Bfile):
    return np.asarray(
        [[float(x) for x in ln.split()] for ln in bfile.read_contents().splitlines()]
    )
