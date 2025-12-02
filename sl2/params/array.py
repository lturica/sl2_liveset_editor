import numpy as np


class ParamArray(np.ndarray):
    """An array subclass
    handles inputs that are in hex string format (e.g. "0A", "FF") or integer format (0-255)
    the object is stored in uint8 format for compactness

    Provides methods to export to json (hex string format) or to a list of integers"""

    def __new__(cls, arr):
        if any(type(x) != int for x in arr):
            hex_arr = [int(x, 16) for x in arr]
        else:
            hex_arr = arr
        obj = np.asarray(hex_arr, dtype=np.uint8).view(
            cls
        )  # returns it a ParamArray or as the head
        return obj

    def json(self):
        # hexadecimal has a 0x prefix that is stripped off
        # pad before with 0 to ensure two characters
        # no negative values appear so no need to handle that
        return [hex(x).replace("0x", "").rjust(2, "0").upper() for x in self]

    def to_db_list(self) -> list:
        return self.tolist()
