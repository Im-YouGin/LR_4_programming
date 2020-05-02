from Compressor import Compressor
from Bit_packer import Bit_packer
from helper_functions import get_bytes


class Archiving_service:
    """
    The main service for file archiving.
    """

    def __init__(self, input_files):
        self.__target_path, *self.__files_to_compress = input_files
        self.__compressor = Compressor()
        self.__bit_packer = Bit_packer(
            initial_lenght=self.__compressor.table_size)

    def encode(self):
        pass

    def decode(self):
        pass


if __name__ == '__main__':
    a = "gabba gabba yo gabba"
    comp = Compressor()
    print(comp.compress(a))
