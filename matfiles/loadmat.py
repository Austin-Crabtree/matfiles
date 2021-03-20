# TODO implement a loadmat function that will check if a file is a mat == 7.3 or is < 7.3. If 7.3 uses h5py to read
#  the data, but if < 7.3 uses scipy.io.loadmat function

import h5py
import numpy as np

from pathlib import Path
from typing import Union, Optional, Dict, List


def _parse_group(group: Union[h5py._hl.group.Group, h5py._hl.dataset.Dataset], skip: List = ['#refs#']) -> Union[Dict, np.ndarray]:
    """
    parse members of the hdf5 group and add to contents to return
    Parameters
    ----------
    group : Union[h5py._hl.group.Group, h5py._hl.dataset.Dataset]
        either a HDF5 group or dataset
    skip : List
        list of groups or datasets to ignore while parsing. In the case of this module we will always skip #refs#

    Returns
    -------
    contents : Union[Dict, np.ndarray]
        contents of the current group can either be a dictionary or array
    """
    if isinstance(group, h5py._hl.group.Group):
        # Since this is a group I will loop through its children
        contents = {}
        groups = group.keys()
        for group_name in groups:
            # name = group_name.split('/')[-1]
            if group_name in skip:
                continue
            _group = group[group_name]
            contents[group_name] = _parse_group(_group)
    elif isinstance(group, h5py._hl.dataset.Dataset):
        contents = group[()]
    return contents


def loadmat(filename: Union[str, Path]) -> Optional[Dict]:
    """
    loads a v7.3 mat file and returns a dictionary with the contents

    Parameters
    ----------
    filename : Optional[str, Path]
        name or path to of a v7.3 mat file. Which is a HDF5 file format.

    Returns
    -------
    contents : Optional[Dict]
        contents of the mat file in a format to easily use as is or to reset the global namespace with.

    Raises
    -------
    TypeError
        if filename is not a hdf5 formatted file. Which implies it is not a v7.3 mat file.
    """
    # Check if the file given is an hdf5 file or not
    if h5py.is_hdf5(filename):
        contents = {}
        matfile = h5py.File(filename, mode='r')
        # So in the file there are at least 2 groups #refs# and a variable that was saved
        # you can ignore #refs# since it is what the other group(s) reference and just worry about the
        # contents in the other groups.

        # TODO grab all the groups and start building the keys in my dictionary
        contents = _parse_group(matfile)
        return contents
    else:
        raise TypeError('File provided is not an HDF5 file. Please make sure you providing a v7.3 mat file.')
