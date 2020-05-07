class Decompressor:
    '''
    Decompression using Lempel–Ziv–Welch (LZW) Algorithm.
    '''

    __INIT_TABLE_LENGTH = 256
    __NEW_POINT_INDEX = 257

    def __init__(self):
        self.__table_length = 256
        self.__decoded = ""
        self.__string = ""
        self.table()

    @property
    def table_size(self):
        return self.__table_length

    @table_size.setter
    def table_size(self, value):
        self.__table_length = value

    @property
    def init_table_length(self):
        return Decompressor.__INIT_TABLE_LENGTH

    @property
    def new_point_id(self):
        return Decompressor.__NEW_POINT_INDEX

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value

    def table_id(self, value):
        return self.__table[value]

    def set_table_value(self, value):
        self.__table[self.table_size] = value

    @property
    def decompressed(self):
        return self.__decoded + self.string[::-1]

    def table(self):
        self.__table = {idk: chr(idk) for idk in range(self.table_size)}

    def decompress(self, compressed):
        for code in compressed:
            if not (code in self.__table):
                self.set_table_value(self.string + self.string[0])
            self.__decoded += self.table_id(code)

            if not(len(self.string) == 0):
                self.set_table_value(self.string + self.table_id(code)[0])
                self.table_size += 1
            self.string = self.table_id(code)

        return self.decompressed
