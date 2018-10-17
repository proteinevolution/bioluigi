import luigi
import enum
from os.path import abspath, islink, isfile, exists
from .util import value_error_if
from Bio import SeqIO


class FileExistence(enum.Enum):
    EXISTING = enum.auto()
    NON_EXISTING = enum.auto()


class FileParameter(luigi.Parameter):
    """
    Parameter whose value is a file path. The File might either be required to be
    present or absent. Currently, the file needs to be a regular file. Directories
    are not supported. Also, currently, links are not supported
    """
    def __init__(self, existence: FileExistence, *args, **kwargs):
        super(FileParameter, self).__init__(*args, **kwargs)
        self.existence = existence
        self.absolute_path = None

    def parse(self, x):
        absolute_path = abspath(x)

        # Disallow Links
        value_error_if(islink(absolute_path), "File {} is a symbolic link. This is currently not supported")

        # Check file existence
        value_error_if(self.existence is FileExistence.EXISTING and not isfile(absolute_path),
                       "File {} does not exist or it is not a regular file!".format(absolute_path))

        value_error_if(self.existence is FileExistence.NON_EXISTING and exists(absolute_path),
                       "File {} exists, but it must not!".format(absolute_path))
        self.absolute_path = absolute_path
        return self.absolute_path


class SequenceFileParameter(FileParameter):
    """
    Specialization of the File Parameter where the value refers to files that contain
    sequences. Such a file must always exist, otherwise the parameter cannot be instantiated.

    Currently, the file must be encoded as FASTA file in the sense of BiopPythons 'fasta' format
    """
    def __init__(self, *args, **kwargs):
        super(SequenceFileParameter, self).__init__(existence = FileExistence.EXISTING, *args, **kwargs)

    def number_of_sequences(self):
        # Just count the number of sequences via SeqIO
        result = 0
        for _ in SeqIO.parse(self.absolute_path, 'fasta'):
            result += 1
        return result


