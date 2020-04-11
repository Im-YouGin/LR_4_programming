from Compressor import Compressor
from Bit_packer import Bit_packer


class Archiving_service:
    """
    The main service for file archiving.
    """

    def __init__(self, input_files):
        self.__target_path, *self.__files_to_compress = input_files
        self.__compressor = Compressor()
        self.__bit_packer = Bit_packer()


if __name__ == '__main__':
   pass