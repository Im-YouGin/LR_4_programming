import sys
from collections import defaultdict


class Argument_parser(object):
    def __init__(self):
        self.__files = {}
        self.parsing()

    def parsing(self):
        self.files = sys.argv[1::]

    @property
    def output_files(self):
        return self.__files

    @property
    def to_compress(self):
        self.__files = {'input_file': self.files[1],
                        'output_file': self.files[-1]}

    @property
    def to_decompress(self):
        self.__files = {'input_file': self.files[1],
                        'output_file': self.files[-1]}

    def main(self):
        if '--comptress' in self.files:
            self.to_compress

        elif '--decomptress' in self.files:
            self.to_decompress


c = Argument_parser()
c.main()

print(c.output_files)
