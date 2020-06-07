from Compressor import Compressor
from Decompressor import Decompressor
from Bit_unpacker import Bit_unpacker
from Bit_packer import Bit_packer
from Argument_parser import Argument_parser
from helper_functions import *


class Archiving_service:
    """
    The main service for file archiving.
    """

    def __init__(self):
        self.__compressor = Compressor()
        self.__decompressor = Decompressor()

        self.__bit_unpacker = Bit_unpacker(
            initial_length=self.__decompressor.table_size)

    def encode(self, output_file, files_to_compress):
        with open(output_file, 'wb') as out_file:
            for fpath in files_to_compress:
                _bytes = readbytes(fpath)
                _compressed = self.__compressor.compress(_bytes)
                print(_compressed)
                # self.__bit_packer = Bit_packer(
                #     initial_lenght=self.__compressor.table_size)
                # _packed = self.__bit_packer.pack(_bytes)
                # out_file.write(_packed)
    def decode(self):
        pass


if __name__ == '__main__':
    service = Archiving_service()
    arg_parser = Argument_parser()
    if arg_parser.to_compress:
        output_file, *files_to_compress = arg_parser.to_compress
        service.encode(output_file, files_to_compress)
    elif arg_parser.to_decompress:
        file_to_decompress = arg_parser.to_decompress
    else:
        print('Sth went wrong :(')