class Compressor:
    '''
    Compression using Lempel–Ziv–Welch (LZW) Algorithm.
    '''

    def __init__(self, uncompessed_string):
        self.__dict_length = 256
        self.__uncompressed_string = uncompessed_string
        self.__string_table = {chr(ind): ind for ind in range(self.dict_size)}
        print(self.__string_table)

    @property
    def dict_size(self):
        return self.__dict_length

    def get_table_id(self, key):
        return self.__string_table[key]

    @dict_size.setter
    def __set_dict_size(self, value):
        self.__dict_length = value

    def __set_table_id(self, value):
        self.__string_table[value] = self.dict_size

    def compress(self):
        previous = ''
        compressed = []

        for next in self.__uncompressed_string:
            next = str(next)
            pattern = previous + next
            if previous + next in self.__string_table.keys():
                previous = pattern

            else:
                compressed.append(self.get_table_id(previous))
                self.__set_table_id(pattern)
                self.__set_dict_size += 1
                previous = next

        if previous:
            compressed.append(self.get_table_id(previous))

        return compressed


if __name__ == '__main__':
    # from sys import getsizeof
    # a = "gabba gabba yo gabba"
    # comp = Compressor(a)
    # print(comp.compress())
    # print(f'{304:016b}')
    pass