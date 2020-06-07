class Compressor:
    '''
    Compression using Lempel–Ziv–Welch (LZW) Algorithm.
    '''

    __INITIAL_TABLE_LENGTH = 256
    __NEW_POINTS_INDEX = 257

    def __init__(self):
        self.__MAX_CODE_SIZE = 2 ** 12
        self.__table_length = 256
        self.build_table()

    @property
    def table_size(self):
        return self.__table_length

    @property
    def init_table_lenght(self):
        return Compressor.__INITIAL_TABLE_LENGTH

    @property
    def new_points_ind(self):
        return Compressor.__NEW_POINTS_INDEX

    @property
    def max_code_size(self):
        return self.__MAX_CODE_SIZE

    def get_table_id(self, key):
        return self.__string_table[key]

    def build_table(self):
        self.__string_table = {chr(ind): ind for ind in range(self.table_size)}
        # self.__string_table[self.init_table_lenght] = self.init_table_lenght
        # self.__string_table[self.new_points_ind] = self.new_points_ind

    @table_size.setter
    def table_size(self, value):
        self.__table_length = value

    def set_table_id(self, value):
        self.__string_table[value] = self.table_size


    def compress(self, uncompressed_bytes):
        previous = ''
        compressed = []

        for next in uncompressed_bytes:
            next = str(next)
            pattern = '-'.join([previous, next])
            if pattern in self.__string_table.keys():
                previous = pattern
            else:
                compressed.append(self.get_table_id(previous))
                if self.table_size <= self.max_code_size:
                    self.set_table_id(pattern)
                    self.table_size += 1
                previous = next

        if previous in self.__string_table.keys():
            compressed.append(self.get_table_id(previous))

        return compressed



if __name__ == '__main__':
    packer = Compressor()
    packed = packer.compress([103, 97, 98])
    print(packed)




