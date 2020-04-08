from argparse import ArgumentParser

class Argument_parser:
    '''
    Parse arguments from a command line.
    '''

    __parser = ArgumentParser()
    __parser.add_argument('--compress', nargs='+', help='To comrpess: 1st argument - output file, other arguments - files to be compessed')
    __parser.add_argument('--decompress', nargs='+', help='To decomrpess: file to be decompressed' )

    def __init__(self):
        self.__parsed = Argument_parser.__parser.parse_args()

    @property
    def to_compress(self):
        return self.__parsed.compress

    @property
    def to_decompress(self):
        return self.__parsed.decompress


