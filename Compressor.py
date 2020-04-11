class Compressor:
    '''
    Compression using Lempel–Ziv–Welch (LZW) Algorithm.
    '''

    def __init__(self, MAX_CODE_SIZE=2**12):
        self.__dict_length = 256
        self.__string_table = {chr(ind): ind for ind in range(self.dict_size)}

    @property
    def dict_size(self):
        return self.__dict_length

    def get_table_id(self, key):
        return self.__string_table[key]

    @dict_size.setter
    def dict_size(self, value):
        self.__dict_length = value

    def set_table_id(self, value):
        self.__string_table[value] = self.dict_size

    def compress(self, uncompressed_bytes):
        previous = ''
        compressed = []

        for next in uncompressed_bytes:
            next = str(next)
            pattern = previous + next
            if previous + next in self.__string_table.keys():
                previous = pattern

            else:
                compressed.append(self.get_table_id(previous))
                self.set_table_id(pattern)
                self.dict_size += 1
                previous = next

        if previous:
            compressed.append(self.get_table_id(previous))

        return compressed




