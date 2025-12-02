from .array import ParamArray


class ComParamArray(ParamArray):
    # Max length for PATCH%COM is 16.
    _LENGTH = 16

    # convert int8 to string to see the name in com
    @property
    def string(self):
        tmp_s = "".join([chr(x) for x in self])
        return tmp_s.rstrip()

    # convert string to int8 array for storage in com
    @string.setter
    def string(self, v: str):
        if not v.isascii():
            return
        # Cut down to 16 characters, then pad with spaces up to 16 characters.
        tmp_s = v[: self._LENGTH].ljust(self._LENGTH)
        # tmp_s = v[:self._LENGTH].upper().ljust(self._LENGTH) # removed necessity for uppercase
        self[: self._LENGTH] = [ord(s) for s in tmp_s]
