from helper_functions import *
class Bit_packer:
    """
    Tranlates compressed Lempel-Ziv-Welch sequence to packed stream of bytes.
    """
    __INITIAL_TABLE_LENGTH = 256
    __NEW_POINTS_INDEX = 257

    def __init__(self, initial_lenght):
        self.__code_size = initial_lenght
        self.__bits_container = []
        self.__bin_length = 8
        self.__final_byte_seq = []

    @property
    def code_size(self):
        return self.__code_size

    @code_size.setter
    def code_size(self, value):
        self.__code_size = value

    @property
    def bin_lenght(self):
        return self.__bin_length

    @bin_lenght.setter
    def bin_lenght(self, value):
        self.__bin_length = value

    @property
    def init_table_lenght(self):
        return Bit_packer.__INITIAL_TABLE_LENGTH

    @property
    def new_points_ind(self):
        return Bit_packer.__NEW_POINTS_INDEX

    def get_final_byte_seq(self):
        return self.__final_byte_seq
    def set_final_byte_seq(self, value):
        self.__final_byte_seq.append(value)

    def get_bits_container(self):
        return self.__bits_container

    def set_bits_container(self, bits):
        self.__bits_container.extend(bits)

    def define_bin_length(self):
        while self.code_size > 1 << self.bin_lenght:
            self.bin_lenght += 1

    def pack(self, codepoints):
        self.define_bin_length()

        for point in codepoints:
            bits = int_to_bit(point, self.bin_length)
            self.set_bits_container(bits)
            self.code_size += 1

            if point == self.new_points_ind:
                while len(self.get_bits_container()) % 8:
                    self.set_bits_container([0])

            while len(self.get_bits_container()) > 8:
                bits = self.get_bits_container()[:8]
                _bytes = bit_to_byte(bits)

                for byte in _bytes:
                    self.set_final_byte_seq(byte)

        if self.get_bits_container():
            _bytes = bit_to_byte(self.get_bits_container())
            for byte in _bytes:
                self.set_final_byte_seq(byte)

        return self.get_final_byte_seq()


if __nam